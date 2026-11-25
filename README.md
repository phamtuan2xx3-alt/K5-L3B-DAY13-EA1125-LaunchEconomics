# Lab 13 — Định giá agent và lập kế hoạch pilot (LogiX-VN, Gate 2a)

AI20K K5, ngày 13 (Launch & Economics), buổi chiều. Mỗi nhóm dựng một bộ **hồ sơ launch v0** cho trợ lý hoàn phí của công ty giả định **LogiX-VN**, rồi bảo vệ hồ sơ trước một nhóm khác đóng vai hội đồng **Gate 2a**. Toàn bộ dữ liệu là **giả lập**. Lab không cần khoá API và không cần mạng trong lúc làm.

**Loại bài:** Nhóm 4 người · **Thời lượng:** 4 giờ tại lớp (14:00–18:00) · **Deadline:** lớp sáng và lớp chiều đều nộp trước 23h59 GMT+7 ngày lab ([SUBMISSION.md](SUBMISSION.md#deadline-gmt7)). Hồ sơ phải sẵn sàng lúc 17:00 để duyệt chéo tại lớp.

## Mục tiêu học tập

Bộ hồ sơ phải trả lời bốn câu hỏi:

1. **Có đáng chạy không?** Chi phí thật cho mỗi việc thành công, so với nhân viên tự làm.
2. **Nhân viên có dùng không?** Chỉ số sử dụng và danh sách event cần ghi.
3. **Khi hỏng thì sao?** Phân loại lỗi và cách khắc phục, mỗi cách có người phụ trách.
4. **Pilot thiết kế thế nào để ra được quyết định?** Có nhóm đối chứng, đủ cỡ mẫu, có luật dừng.

## Bối cảnh

LogiX-VN có 12 depot, khoảng 40 nhân viên CSKH và nhận khoảng 1.500 yêu cầu hoàn phí mỗi ngày. Trợ lý hoàn phí vừa chạy thử 2 tuần ở 6 depot. Nhóm nhận một mẫu ngẫu nhiên 1.200 yêu cầu (1.624 lần chạy của agent) để trả lời bốn câu hỏi trên. Ý nghĩa từng cột, số liệu dùng chung và sáu công thức: [docs/du_lieu_va_cong_thuc.md](docs/du_lieu_va_cong_thuc.md).

## Năm nhiệm vụ

| Giờ | Checkpoint · Nhiệm vụ | Thời gian | Sản phẩm |
| --- | --- | --- | --- |
| 14:00 | Chia nhóm, cài đặt, chạy thử file khởi đầu | 10 phút | |
| 14:10 | **CP1 · A · Mô hình chi phí mỗi việc thành công** | 40 + 3 phút | `src/lab13.py`, `report/team/bang_chi_phi.md` |
| 14:53 | **CP2 · B · Bảng độ nhạy** | 25 + 2 phút | `report/team/bang_chi_phi.md` |
| 15:35 | **CP3 · C · Bảng lỗi và cách khắc phục** | 30 + 3 phút | `report/team/bang_loi.md` |
| 16:08 | **CP4 · D · pilot_plan.yaml** | 25 + 3 phút | `report/team/pilot_plan.yaml` |
| 16:36 | **CP5 · E · Chỉ số, rủi ro kinh tế, hồ sơ launch v0** | 20 + 4 phút | `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` |
| 17:00 | **CP5 · Duyệt chéo Gate 2a**: nhóm n chấm nhóm n + 1 | 45 phút | `report/team/phieu_cham.md` |
| 17:45 | Đóng gói, commit, push | 15 phút | |

Giải lao 15:20–15:35. Chi tiết từng checkpoint: [CHECKPOINTS.md](CHECKPOINTS.md).

## Bắt đầu

**Bước 0 — tạo repo nhóm.** Nhóm trưởng fork repo này rồi đổi tên theo mẫu `K5-L3A-DAY13-TenNhom-LaunchEconomics` (lớp L3B thay `L3A` bằng `L3B`). Không fork được thì làm theo [SUBMISSION.md](SUBMISSION.md#tạo-repo-nhóm). Các thành viên clone **repo nhóm**, không làm trên repo đề bài.

**Bước 1 — cài và chạy thử.** Cần Python 3.10 trở lên. **Mọi lệnh chạy trong thư mục `src/`.**

```bash
cd src
python3 -m venv .venv
source .venv/bin/activate            # Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
python lab13.py                      # bản nhóm đã hoàn thiện A–B, D1 và E1
```

Cài đặt theo từng hệ điều hành và cách đọc dữ liệu đúng: [src/README.md](src/README.md).

## Năm quy tắc của lab

1. Qua đủ ba phép thử A1 (1,20 · 1,25 · 1,25) rồi mới làm tiếp.
2. Mọi con số tính từ hai cột `_simulated` phải ghi nhãn **simulated**.
3. Đối chiếu ngay khi slide chữa hiện lên; nhiệm vụ sau dùng lại số của nhiệm vụ trước.
4. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.
5. Không dùng từ "production": Gate 2a chỉ duyệt kế hoạch pilot.

## Đọc gì, khi nào

1. [RULES.md](RULES.md): dùng AI, liêm chính, nộp muộn.
2. [CHECKPOINTS.md](CHECKPOINTS.md): 5 checkpoint theo lịch buổi lab và cách tự kiểm tra.
3. [src/README.md](src/README.md): cài đặt, file được sửa, cách đọc dữ liệu.
4. [RUBRIC.md](RUBRIC.md): 70 điểm đối chiếu đáp án + 30 điểm hội đồng.
5. [SUBMISSION.md](SUBMISSION.md): tên repo, file phải nộp, deadline, checklist. Đọc trước khi nộp.

Trong lúc làm: [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) (hướng dẫn từng bước, số để tự đối chiếu) và [docs/README.md](docs/README.md) (đề bài gốc, slide, bài làm mẫu).

## Cấu trúc repo

| Đường dẫn | Nội dung |
| --- | --- |
| `README.md`, `RULES.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md` | Đề bài, luật, checkpoint, cách chấm, cách nộp |
| `TEAM.md` | Thông tin nhóm, thành viên, vai và đóng góp |
| `src/` | Bài làm `lab13.py` (học viên viết vào đây), bản gốc `lab13_starter.py`, hai file CSV, `requirements.txt` |
| `docs/` | Dữ liệu và công thức, hướng dẫn chi tiết, đề bài gốc (docx), slide |
| `report/team/` | Mẫu các file hồ sơ nhóm phải nộp và báo cáo từng thành viên |

## Báo cáo phải nộp

- Sáu file hồ sơ trong `report/team/`: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md`. Giữ nguyên tên file.
- `report/team/group_report.md`: báo cáo nhóm ngắn.
- Mỗi thành viên **copy** `report/team/MSSV_HoTen.md` thành file riêng đặt tên theo MSSV và họ tên không dấu, ví dụ `report/team/20241234_NguyenVanAn.md`. Giữ nguyên file mẫu để người khác còn copy.
- `TEAM.md`: điền thông tin nhóm, vai và đóng góp.

Chi tiết: [SUBMISSION.md](SUBMISSION.md).

## Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
