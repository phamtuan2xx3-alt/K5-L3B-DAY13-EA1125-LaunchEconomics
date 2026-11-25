"""Kiểm tra số đối chiếu của lab, giới hạn chạy lại và tính nhất quán YAML.

Chạy từ root: src/.venv/Scripts/python.exe -m unittest discover -s tests -v
"""
import hashlib
import math
from datetime import date, timedelta
from pathlib import Path
import sys
import unittest

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
import lab13


class Lab13Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runs = pd.read_csv(ROOT / 'src/logix_runs.csv')
        cls.reqs = pd.read_csv(ROOT / 'src/logix_requests.csv', keep_default_na=False)
        cls.kq = lab13.tong_hop(cls.runs, cls.reqs)

    def test_a1_known_answers_and_boundaries(self):
        lab13.kiem_tra_dap_an_biet_truoc()
        self.assertEqual(lab13.so_lan_chay_ky_vong(0, 3), 3)
        self.assertEqual(lab13.ti_le_thanh_cong(0, 3), 0)
        self.assertTrue(math.isinf(lab13.he_so_chi_phi_moi_viec_thanh_cong(0, 3)))
        self.assertEqual(lab13.he_so_chi_phi_moi_viec_thanh_cong(1, 3), 1)
        for p, k in [(-0.1, 2), (1.1, 2), (0.8, 0), (0.8, 1.5)]:
            with self.subTest(p=p, k=k), self.assertRaises(ValueError):
                lab13.so_lan_chay_ky_vong(p, k)

    def test_a2_matches_authoritative_reference(self):
        expected = dict(token=245585.132, tool=84000, chay_lai=93804.488,
                        xem_lai=1780000, lam_lai=2264000, tong=4373585.132, thanh_cong=978)
        for key, value in expected.items():
            with self.subTest(key=key):
                self.assertAlmostEqual(self.kq['a2'][key], value, places=5)
        self.assertAlmostEqual(self.kq['a2']['cps'], 4471.9684376, places=4)

    def test_subset_filters_runs_and_retry_does_not_mutate_inputs(self):
        runs_before, reqs_before = self.runs.copy(deep=True), self.reqs.copy(deep=True)
        subset = self.reqs.loc[self.reqs.loai.eq('noi_dia')]
        all_runs = lab13.mo_hinh(self.runs, subset)
        filtered = lab13.mo_hinh(self.runs.loc[self.runs.request_id.isin(subset.request_id)], subset)
        self.assertEqual(all_runs, filtered)
        self.assertAlmostEqual(all_runs['cps'], 2695.642, places=2)
        lab13.mo_hinh(self.runs, self.reqs, max_lan_chay=1)
        pd.testing.assert_frame_equal(self.runs, runs_before)
        pd.testing.assert_frame_equal(self.reqs, reqs_before)
        no_success = self.reqs.assign(ket_qua='chuyen_nhan_vien')
        self.assertTrue(math.isinf(lab13.mo_hinh(self.runs, no_success)['cps']))

    def test_a4_uses_total_company_volume(self):
        full, half = self.kq['a4']
        self.assertEqual(full['thanh_cong_thang'], 33750)
        self.assertAlmostEqual(full['cps'], 4599.089, places=2)
        self.assertAlmostEqual(half['co_dinh_moi_viec'], full['co_dinh_moi_viec'] * 2)

    def test_b1_b2_linear_sensitivity(self):
        self.assertEqual(len(self.kq['b1']), 9)
        base = self.kq['a2']['cps']
        for up, down in [(0, 1), (2, 3), (4, 5)]:
            self.assertAlmostEqual(self.kq['b1'][up]['cps'] - base,
                                   2 * (base - self.kq['b1'][down]['cps']))
        self.assertAlmostEqual(self.kq['b2_cps'] - base,
                               self.kq['b1'][0]['cps'] + self.kq['b1'][2]['cps'] - 2 * base)

    def test_b3_system_optimum_differs_from_cps_optimum(self):
        rows = self.kq['b3']
        self.assertEqual([r['khong_thanh_cong'] for r in rows], [319, 234, 222])
        self.assertAlmostEqual(rows[1]['tong_he_thong'], 6901220.230, places=3)
        self.assertEqual(min(rows, key=lambda r: r['tong_he_thong'])['gioi_han'], 2)
        self.assertEqual(min(rows, key=lambda r: r['cps'])['gioi_han'], 1)

    def test_b4_counts_requests_instead_of_successful_runs(self):
        base, stress = self.kq['b4']
        self.assertEqual(base['so_xem_lai'], 948)
        self.assertEqual(base['so_lam_lai'], 48)
        self.assertAlmostEqual(base['cps'], 11742.7925267, places=4)
        self.assertLess(base['cps'], lab13.BASELINE)
        self.assertGreater(stress['cps'], lab13.BASELINE)
        self.assertAlmostEqual(stress['phut_lam_lai'], 1132 / 74)

    def test_d1_and_yaml_contract(self):
        d = self.kq['d1']
        self.assertEqual([d['n5'], d['n75'], d['nhan_vien_moi_nhom'], d['n6'], d['m']],
                         [1251, 3103, 42, 859, 299])
        self.assertAlmostEqual(d['de'], 6.96)
        self.assertAlmostEqual(d['power5'], 0.642, delta=0.001)
        self.assertEqual((self.kq['mo_lai'], self.kq['scope_mo_lai']), (51, 39))
        text = (ROOT / 'report/team/pilot_plan.yaml').read_text(encoding='utf-8')
        self.assertNotIn('?', '\n'.join(line for line in text.splitlines() if not line.lstrip().startswith('#')))
        pilot = yaml.safe_load(text)['pilot']
        for field in ['owner', 'scope', 'assignment', 'rollout', 'primary_metric', 'identifiability',
                      'stop_rules', 'interim_looks', 'rollback', 'decision_date', 'simulated_inputs']:
            self.assertTrue(pilot[field], field)
        metric = pilot['primary_metric']
        self.assertEqual(metric['raw_n_per_arm'], d['raw_n'])
        self.assertAlmostEqual(metric['effective_n_per_arm'], d['effective_n'])
        self.assertEqual(metric['n_per_arm'], d['n6'])
        last_enrollment = date.fromisoformat(pilot['rollout_schedule'][-1]['end'])
        mature = date.fromisoformat(metric['maturity_date'])
        self.assertGreaterEqual(mature, last_enrollment + timedelta(days=8))
        self.assertGreater(date.fromisoformat(pilot['decision_date']), mature)
        self.assertGreaterEqual(len(pilot['stop_rules']), 3)
        for rule in pilot['stop_rules']:
            for token in ['NẾU', 'TRONG', 'THÌ', 'KHÔNG THÌ']:
                self.assertIn(token, rule)

    def test_source_data_starter_and_individual_template_unchanged(self):
        expected = {
            'src/logix_runs.csv': 'e6283a153b2385eaef25468e1c849a4139b130c2d287ed899b71e3cc2604049f',
            'src/logix_requests.csv': '6849c1397777db5bbf5b6503f282eaa895455d900677ad04282c5a7ed0ad42fa',
            'src/lab13_starter.py': '8369e1b69b2c91a9b14f8ce2dc34da08e943b072a8ba35b26bfc166f2089de6f',
            'report/team/MSSV_HoTen.md': '6ca77111a0c9ea6c27a0e9c9217fe4f95f770ee21794f4f659da24fc6d381887',
        }
        for path, digest in expected.items():
            with self.subTest(path=path):
                # Git có thể checkout CRLF trên Windows và LF trên Linux/macOS.
                canonical = (ROOT / path).read_bytes().replace(b'\r\n', b'\n')
                self.assertEqual(hashlib.sha256(canonical).hexdigest(), digest)


if __name__ == '__main__':
    unittest.main()
