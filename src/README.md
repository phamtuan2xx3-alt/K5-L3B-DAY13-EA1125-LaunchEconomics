# Code và cách chạy Lab 13

Code phân tích của nhóm EA1125, dữ liệu giả lập. File nộp `lab13.py` tính **A1–A4, B1–B4, D1 và E1**; không cần API key hoặc gọi model. Giữ nguyên `lab13_starter.py`, hai CSV và mẫu báo cáo cá nhân.

## Cài đặt và chạy trong src/

Python 3.10 trở lên; cài thư viện một lần có thể cần mạng. Sau khi cài, code và kiểm thử chạy offline.

Windows PowerShell:

```powershell
cd src
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:PYTHONUTF8 = '1'
.\.venv\Scripts\python.exe lab13.py --output ../report/team/TV1_ket_qua.txt
```

macOS/Linux:

```bash
cd src
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python lab13.py --output ../report/team/TV1_ket_qua.txt
```

Không bắt buộc kích hoạt môi trường nếu gọi Python bằng đường dẫn trên. Có thể bỏ `--output` để chỉ in terminal. Code tìm CSV theo vị trí file, nên gọi từ root cũng được; lệnh ở lớp vẫn chạy trong `src/`.

## Kết quả và dữ liệu

- A1 phải in **Ba phép thử đáp án biết trước: ĐẠT** trước mọi bảng.
- A2/A3/A4 là mẫu gốc tối đa 3 lần; B1/B3 ghi rõ giới hạn 1/2/3 lần.
- Dự toán pilot riêng áp dụng noi_dia+hang_nang, tối đa 2 lần, cộng ca làm thủ công trong/ngoài phạm vi và cố định.
- D1 phân biệt mẫu thô và hiệu dụng; E1 in rõ 994/1.200, 48/177, 51/1.200. Chưa có mẫu số thì tỷ lệ là chưa có dữ liệu, không mặc định 0.
- `TV1_ket_qua.txt` giữ tên bàn giao ban đầu nhưng hiện là output chung A–E; có thể tạo lại bằng lệnh trên.
- Hai CSV là giả lập; mọi chi phí dùng `phut_xem_lai_simulated`/`phut_lam_lai_simulated` mang nhãn **simulated**, không phải phút đo thật.
- Đọc yêu cầu bằng `pd.read_csv(..., keep_default_na=False)` để giữ ô quyết định trống đúng dữ liệu.

## Kiểm thử từ root repo

Windows:

```powershell
$env:PYTHONUTF8 = '1'
.\src\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

macOS/Linux:

```bash
src/.venv/bin/python -m unittest discover -s tests -v
```

Bộ kiểm thử đối chiếu số lab, giới hạn chạy, E1, CLI/UTF-8, YAML/cỡ mẫu/ngày trưởng thành và SHA-256 nội dung gốc sau chuẩn hóa xuống dòng. Đây là bằng chứng kỹ thuật; không thay nhãn độc lập, hội đồng, xác nhận cá nhân hoặc nộp LMS. Xem [nghiệm thu](../report/team/nghiem_thu.md).
