"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python lab13.py (hoặc thêm --output <file> để lưu bảng).
TV1: PHẠM QUANG TUẤN, 2A202603824. Code A–B và phép tính hỗ trợ kế hoạch D.
Dữ liệu trong hai file CSV là giả lập; mọi chi phí dùng phút giả lập mang nhãn simulated.
Bản gốc chưa sửa nằm ở lab13_starter.py.
Nguồn công thức: docs/du_lieu_va_cong_thuc.md và hướng dẫn chi tiết Lab 13 trong repo.
"""
import argparse
import math
from pathlib import Path
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def _kiem_tra_p_k(p, k):
    if not 0 <= p <= 1:
        raise ValueError('p phải thuộc [0, 1].')
    if k is not None and (isinstance(k, bool) or not isinstance(k, int) or k < 1):
        raise ValueError('k phải là số nguyên dương hoặc None.')


def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    _kiem_tra_p_k(p, k)
    if p == 0:
        return math.inf if k is None else float(k)
    return 1 / p if k is None else ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    _kiem_tra_p_k(p, k)
    return float(p > 0) if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / thanh_cong if thanh_cong else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    if reqs.empty:
        raise ValueError('Cần ít nhất một yêu cầu để tính mô hình.')
    if max_lan_chay is not None:
        _kiem_tra_p_k(1, max_lan_chay)
    if min(gia_vao, gia_ra, gia_tool, luong_phut, he_so_xem_lai, he_so_lam_lai) < 0:
        raise ValueError('Giá và hệ số chi phí không được âm.')
    reqs = reqs.copy()
    runs = runs.loc[runs.request_id.isin(reqs.request_id)]
    if max_lan_chay is not None:
        runs = runs.loc[runs.attempt <= max_lan_chay]
        vuot = reqs.so_lan_chay > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    token = runs.tokens_in / 1000 * gia_vao + runs.tokens_out / 1000 * gia_ra
    tool = runs.tool_calls * gia_tool
    xem_lai = float(reqs.phut_xem_lai_simulated.sum() * luong_phut * he_so_xem_lai)
    lam_lai = float(reqs.phut_lam_lai_simulated.sum() * luong_phut * he_so_lam_lai)
    tong = float(token.sum() + tool.sum() + xem_lai + lam_lai)
    thanh_cong = int(reqs.ket_qua.eq('thanh_cong').sum())
    return dict(token=float(token.sum()), tool=float(tool.sum()),
                chay_lai=float((token + tool).loc[runs.attempt > 1].sum()),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong if thanh_cong else math.inf,
                hoa_don_moi_yc=float((token.sum() + tool.sum()) / len(reqs)))


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Công thức so hai tỉ lệ của lab; kết quả là số yêu cầu độc lập mỗi nhóm."""
    if not (0 < p1 < 1 and 0 < p2 < 1 and p1 != p2 and 0 < alpha < 1 and 0 < power < 1):
        raise ValueError('Hai tỉ lệ phải khác nhau và các xác suất phải thuộc (0, 1).')
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def tinh_d1():
    """Số hỗ trợ TV1 điền YAML; TV2 tiếp tục kiểm tra độc lập khi nhận bàn giao."""
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize

    n5, n6 = co_mau(0.70, 0.75), co_mau(0.70, 0.76)
    icc, c = 0.02, 20
    de75 = 1 + (75 - 1) * icc
    m = math.ceil(n6 * (1 - icc) / (c - n6 * icc))
    de = 1 + (m - 1) * icc
    power5 = NormalIndPower().power(effect_size=proportion_effectsize(0.75, 0.70),
                                    nobs1=c * m / de, alpha=0.05, ratio=1)
    return dict(n5=n5, de75=de75, n75=math.ceil(n5 * de75),
                nhan_vien_moi_nhom=math.ceil(n5 * de75 / 75),
                tran20=c / icc, tran6=6 / icc, n6=n6, m=m, de=de,
                raw_n=c * m, effective_n=c * m / de, power5=float(power5))


def tong_hop(runs, reqs):
    """Tính A–B từ CSV, không thay dữ liệu đầu vào; thêm D1 và baseline phục vụ YAML."""
    goc = mo_hinh(runs, reqs)
    pham_vi = reqs.loc[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    trong_pham_vi = mo_hinh(runs, pham_vi)
    a3 = []
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        nhom = reqs.loc[reqs.loai.eq(loai)]
        kq = mo_hinh(runs, nhom)
        a3.append(dict(loai=loai, so_yc=len(nhom),
                       thanh_cong_pct=kq['thanh_cong'] / len(nhom) * 100,
                       lan_chay=len(runs.loc[runs.request_id.isin(nhom.request_id)]) / len(nhom),
                       cps=kq['cps'], so_voi_baseline=kq['cps'] / BASELINE))
    a4 = []
    for khoi_luong in [45000, 22500]:
        # 45.000 là toàn công ty: mẫu số là cả 1.200 yêu cầu, không phải riêng 982.
        so_viec = khoi_luong * trong_pham_vi['thanh_cong'] / len(reqs)
        co_dinh = 40000000 / so_viec
        a4.append(dict(yc_thang=khoi_luong, thanh_cong_thang=so_viec,
                       co_dinh_moi_viec=co_dinh, cps=trong_pham_vi['cps'] + co_dinh,
                       so_voi_baseline=(trong_pham_vi['cps'] + co_dinh) / BASELINE))
    kich_ban = [
        ('Token x2', dict(gia_vao=52, gia_ra=260)),
        ('Token x0.5', dict(gia_vao=13, gia_ra=65)),
        ('Xem lai x2', dict(he_so_xem_lai=2)),
        ('Xem lai x0.5', dict(he_so_xem_lai=0.5)),
        ('Lam lai x2', dict(he_so_lam_lai=2)),
        ('Lam lai x0.5', dict(he_so_lam_lai=0.5)),
        ('Luong +25%', dict(luong_phut=2500)),
        ('Toi da 2 lan', dict(max_lan_chay=2)),
        ('Toi da 1 lan', dict(max_lan_chay=1)),
    ]
    b1 = []
    for ten, tham_so in kich_ban:
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        b1.append(dict(kich_ban=ten, cps=cps, thay_doi_pct=(cps / goc['cps'] - 1) * 100))
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    b3 = []
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        that_bai = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + that_bai * BASELINE
        b3.append(dict(gioi_han=k, tong_tro_ly=kq['tong'], khong_thanh_cong=that_bai,
                       tong_he_thong=he_thong, he_thong_moi_yc=he_thong / len(reqs), cps=kq['cps']))
    scope_runs = runs.loc[runs.request_id.isin(pham_vi.request_id)]
    so_ok = scope_runs.loc[scope_runs.status.eq('ok'), 'request_id'].nunique()
    so_lam_lai = int(pham_vi.ket_qua.eq('lam_lai').sum())
    phut_tb = float(reqs.loc[reqs.ket_qua.eq('lam_lai'), 'phut_lam_lai_simulated'].mean())
    b4 = []
    for phut in [9.0, phut_tb]:
        tien_may = trong_pham_vi['token'] + trong_pham_vi['tool']
        tien_lam_lai = so_lam_lai * phut * LUONG_PHUT
        tong = tien_may + so_ok * 5 * LUONG_PHUT + tien_lam_lai
        cps = tong / trong_pham_vi['thanh_cong']
        b4.append(dict(phut_lam_lai=phut, so_xem_lai=so_ok, so_lam_lai=so_lam_lai,
                       tong=tong, cps=cps, so_voi_baseline=cps / BASELINE,
                       phut_xem_hoa_von=(trong_pham_vi['thanh_cong'] * BASELINE
                                         - tien_may - tien_lam_lai) / (so_ok * LUONG_PHUT)))
    ok_theo_lan = (runs.assign(ok=runs.status.eq('ok'))
                  .merge(reqs[['request_id', 'loai']], on='request_id', validate='many_to_one')
                  .groupby(['loai', 'attempt']).ok.mean().mul(100).unstack())
    return dict(a2=goc, a3=a3, a4=a4, scope=trong_pham_vi,
                b1=b1, b2_cps=cap['cps'], b2_pct=(cap['cps'] / goc['cps'] - 1) * 100,
                b3=b3, b4=b4, ok_theo_lan=ok_theo_lan,
                d1=tinh_d1(), so_yc=len(reqs), so_runs=len(runs),
                scope_so_yc=len(pham_vi),
                mo_lai=int(reqs.mo_lai_trong_7_ngay.sum()),
                scope_mo_lai=int(pham_vi.mo_lai_trong_7_ngay.sum()))


def bao_cao(kq):
    """Bảng bàn giao TV2–TV4; không điền thay hồ sơ của các thành viên khác."""
    def bang(ten, rows):
        return ten + '\n' + pd.DataFrame(rows).to_string(index=False, float_format=lambda x: f'{x:,.3f}')

    a2, d = kq['a2'], kq['d1']
    a2_rows = [dict(khoan=ten, gia_tri=a2[ten], nhan=nhan) for ten, nhan in [
        ('token', 'trace'), ('tool', 'trace'), ('chay_lai', 'trace, da nam trong token+tool'),
        ('xem_lai', 'simulated'), ('lam_lai', 'simulated'), ('tong', 'simulated'),
        ('thanh_cong', 'CSV'), ('cps', 'simulated'), ('hoa_don_moi_yc', 'trace')]]
    sections = [
        'TV1: PHẠM QUANG TUẤN — 2A202603824. Dữ liệu giả lập của lab; chi phí có phút giả lập ghi simulated.',
        f'Dữ liệu: {kq["so_yc"]} yêu cầu, {kq["so_runs"]} lần chạy.',
        'A1: 1.20 / 1.25 / 1.25',
        bang('A2 · Chi phí từ mọi lần chạy (đồng)', a2_rows),
        f'A2 · CPS / hóa đơn mỗi yêu cầu = {a2["cps"] / a2["hoa_don_moi_yc"]:.3f} lần (simulated); '
        f'làm lại chiếm {a2["lam_lai"] / a2["tong"] * 100:.3f}% (simulated).',
        bang('A3 · Theo loại: cps và so_voi_baseline là simulated', kq['a3']),
        'A3 · Tỉ lệ ok (%) theo lần thử:\n' + kq['ok_theo_lan'].to_string(float_format=lambda x: f'{x:.3f}'),
        bang('A4 · Cộng cố định 40 triệu/tháng trong phạm vi noi_dia + hang_nang (simulated)', kq['a4']),
        bang('B1 · 9 kịch bản (simulated)', kq['b1']),
        f'B2 · Token x2 và xem lại x2: {kq["b2_cps"]:,.3f} đ, {kq["b2_pct"]:+.3f}% (simulated).',
        'B2 · Xếp hạng: 1. Làm lại; 2. Xem lại; 3. Lương nhân viên.',
        bang('B3 · Cộng 12.000 đ cho mỗi yêu cầu không thành công theo quy ước lab (simulated)', kq['b3']),
        'B3 · Giới hạn 2 lần rẻ nhất cho cả hệ thống; giới hạn 1 lần có CPS thấp nhất.',
        bang('B4 · Xem lại 100%, 5 phút/ca, phạm vi noi_dia + hang_nang (simulated)', kq['b4']),
        'D1 · Hỗ trợ YAML của TV1; TV2 cần kiểm lại độc lập:',
        f'a) {d["n5"]} yêu cầu độc lập/nhóm; b) DE={d["de75"]:.2f}, {d["n75"]} yêu cầu, '
        f'{d["nhan_vien_moi_nhom"]} nhân viên/nhóm; c) trần {d["tran20"]:.0f}; d) trần {d["tran6"]:.0f}.',
        f'e) MDE 6 điểm: {d["n6"]} hiệu dụng/nhóm; 20 nhân viên x {d["m"]} yêu cầu = {d["raw_n"]} thô/nhóm; '
        f'DE={d["de"]:.2f}, hiệu dụng={d["effective_n"]:.3f}. Power nếu hiệu ứng thật 5 điểm: {d["power5"]:.4f}.',
        f'Baseline mở lại: {kq["mo_lai"]}/{kq["so_yc"]} = {kq["mo_lai"] / kq["so_yc"]:.4%}; '
        f'trong phạm vi {kq["scope_mo_lai"]}/{kq["scope_so_yc"]} = {kq["scope_mo_lai"] / kq["scope_so_yc"]:.4%}.',
        'Phạm vi: đề xuất noi_dia + hang_nang; quoc_te thiếu hiệu quả, doi_tac có điều khoản riêng.',
        'Chưa xác nhận: kiểm tra trên máy TV2, hai bộ nhãn độc lập, duyệt chéo và phê duyệt pilot.',
    ]
    return '\n'.join(line.rstrip() for line in '\n\n'.join(sections).splitlines())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Lưu bảng UTF-8 để bàn giao cho nhóm.')
    args = parser.parse_args()
    kiem_tra_dap_an_biet_truoc()
    thu_muc = Path(__file__).resolve().parent
    runs = pd.read_csv(thu_muc / 'logix_runs.csv')
    reqs = pd.read_csv(thu_muc / 'logix_requests.csv', keep_default_na=False)
    text = bao_cao(tong_hop(runs, reqs))
    print(text)
    if args.output:
        args.output.write_text('Ba phép thử đáp án biết trước: ĐẠT\n\n' + text + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
