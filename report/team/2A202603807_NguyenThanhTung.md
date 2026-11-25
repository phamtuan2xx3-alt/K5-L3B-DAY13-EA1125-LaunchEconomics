# Báo cáo cá nhân — NGUYỄN THANH TÙNG — 2A202603807

## 1. Thông tin thành viên

- Họ tên: NGUYỄN THANH TÙNG.
- MSSV: 2A202603807.
- Lớp/nhóm theo repo: L3B / EA1125.
- Email: 26ai.tungnt7@vinuni.edu.vn
- Vai trong nhóm: TV2 — Kiểm số; điền bảng chi phí A–B; kiểm tra bản tích hợp và chạy kiểm chứng trên máy khác.

## 2. Phần việc phụ trách

- Đọc dữ liệu, công thức; tự tính tay độc lập ít nhất một con số để đối chiếu chéo với TV1.
- Trực tiếp điền và hoàn thiện toàn bộ file `report/team/bang_chi_phi.md` (nhiệm vụ A và B), gồm:
  - Bảng A1 (3 phép thử biết trước).
  - Bảng A2 (9 dòng chi phí từ trace), kiểm tra nhãn `simulated` và trả lời 2 câu hỏi có số liệu.
  - Bảng A3 (4 loại yêu cầu) và câu trả lời loại bỏ `quoc_te`.
  - Bảng A4 (chi phí cố định 40 triệu/tháng ở 2 mức khối lượng).
  - Bảng B1 (9 kịch bản độ nhạy).
  - Bảng B2 (kịch bản cặp và xếp hạng 3 yếu tố nhạy nhất).
  - Bảng B3 (giới hạn chạy lại và chi phí cả hệ thống).
  - Bảng B4 (kịch bản xem lại 100% với 9 phút và 15,3 phút thực tế).
- Kiểm tra tính toán độc lập bộ kiểm thử tự động của nhóm (`tests/test_lab13.py`) trên máy TV2.
- Chuẩn bị tiếp nhận quyền sửa code `src/lab13.py` sau giải lao cho nhiệm vụ D1 và E1.

## 3. Đóng góp cụ thể trong phiên làm việc

- **Kiểm toán số liệu độc lập:**
  - Tự tính tay kiểm chứng: Tiền tool = 5.600 lần gọi × 15 đ = 84.000 đ; Tiền xem lại = 890 phút × 2.000 đ = 1.780.000 đ [simulated].
  - Đối chiếu toàn bộ kết quả của TV1 bàn giao (`TV1_ket_qua.txt`, `TV1_ban_giao.md`): mọi con số khớp 100%, độ lệch 0% (đạt tiêu chuẩn $\le 2\%$).
- **Hoàn thành hồ sơ `report/team/bang_chi_phi.md`:**
  - Điền đầy đủ 100% các bảng A1–A4 và B1–B4.
  - Gắn nhãn `simulated` cho toàn bộ các con số có nguồn gốc từ cột giả lập (`phut_xem_lai_simulated`, `phut_lam_lai_simulated`).
  - Mọi câu trả lời giải thích kinh tế đều ngắn gọn ($\le 3$ dòng), có số liệu thực chứng và không dùng từ cấm "production".
- **Chạy kiểm chứng trên máy khác (nghiệm thu kỹ thuật):**
  - Đã chạy toàn bộ test suite `python -m unittest discover -s ..\tests -v` trên máy TV2: **9/9 bài kiểm thử ĐẠT 100%**.
  - Xác nhận tính toàn vẹn của code `src/lab13.py` do TV1 bàn giao.

## 4. Bằng chứng

- File hồ sơ trực tiếp sở hữu và điền: [bang_chi_phi.md](bang_chi_phi.md).
- File nghiệm thu kỹ thuật và kết quả TV1: [TV1_ban_giao.md](TV1_ban_giao.md), [TV1_ket_qua.txt](TV1_ket_qua.txt).
- Kiểm thử tự động đã chạy trên máy TV2: [test_lab13.py](../../tests/test_lab13.py) (9 test ĐẠT).
- File báo cáo cá nhân: `report/team/2A202603807_NguyenThanhTung.md`.
- Nhánh: `main`.

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI hỗ trợ rà soát định dạng Markdown, kiểm tra chéo các bảng số liệu với rubric, quét từ cấm ("production") và soát lỗi quy cách nhãn `simulated`.
- Tự kiểm tra của Tùng: Tự đối chiếu số liệu tính tay với output, tự chạy lệnh `unittest` trong terminal máy của mình, xác nhận giải thích kinh tế (vì sao giới hạn 2 lần rẻ nhất toàn công ty dù 1 lần có CPS trợ lý thấp nhất).

## 6. Tự đánh giá

- Hoàn thành trọn vẹn 100% trách nhiệm của TV2 cho CP1 và CP2.
- Số liệu kiểm toán khớp với TV1, hồ sơ chi phí sạch đẹp, sẵn sàng cho khâu tiếp quản code sau giải lao và nộp bài. Chưa xác nhận nộp LMS (chờ duyệt chéo Gate 2a).
