# Báo cáo cá nhân — PHẠM QUANG TUẤN — 2A202603824

## 1. Thông tin thành viên

- Họ tên: PHẠM QUANG TUẤN.
- MSSV: 2A202603824.
- Lớp/nhóm: L3B-H202 / EA1125.
- Email: chưa bổ sung.
- Vai: TV1 — viết code A–B, phụ trách kinh tế và kế hoạch pilot D.

## 2. Phần việc phụ trách

- Triển khai ba hàm A1, mô hình A2, phân tích A3 và cố định A4.
- Tính 9 kịch bản B1, cặp B2, chi phí hệ thống B3 và xem lại 100% B4.
- Soạn YAML pilot cùng đầu vào cỡ mẫu/baseline để TV2 kiểm độc lập.
- Bàn giao rủi ro kinh tế và đề xuất có điều kiện cho TV3/TV4.

## 3. Đóng góp cụ thể trong phiên làm việc

Code và bản nháp được triển khai trong workspace với trợ giúp Codex theo phân công TV1. `src/lab13.py` chạy A–B, in D1 hỗ trợ YAML và lưu output; chưa thay cho việc TV2 kiểm độc lập hoặc tự chạy trên máy khác.

Kết quả chính: A1 đạt 1,20/1,25/1,25; CPS toàn mẫu 4.471,97 đ (simulated); giới hạn 2 lần có chi phí hệ thống thấp nhất 6.901.220,23 đ (simulated). B4 dùng phút làm lại trung bình đầy đủ cho CPS 12.414,50 đ (simulated), vượt baseline 12.000 đ.

YAML đề xuất 20 cụm nhân viên mỗi nhóm, 299 yêu cầu/cụm, MDE 6 điểm; ghi rõ power chỉ 0,6418 nếu hiệu ứng thật 5 điểm. Nhóm và vai trò phê duyệt chưa xác nhận kế hoạch này.

## 4. Bằng chứng

- [Code](../../src/lab13.py), [output](TV1_ket_qua.txt), [YAML](pilot_plan.yaml), [bản bàn giao](TV1_ban_giao.md).
- [Kiểm thử](../../tests/test_lab13.py): 9 kiểm thử tự động đã chạy đạt trên Windows/Python 3.12.10 trong workspace.
- Hai CSV, starter và mẫu báo cáo cá nhân được đối chiếu SHA-256 để xác nhận giữ nguyên.
- Nhánh: `main`; commit phần triển khai xem lịch sử Git của các file trên sau khi đóng gói.

## 5. Công cụ AI đã dùng

Codex hỗ trợ đọc yêu cầu, chia việc, viết code, soạn bản nháp YAML/bàn giao và chạy kiểm tra. Kiểm tra tự động đối chiếu số tham chiếu trong repo, tính tuyến tính độ nhạy, phạm vi dữ liệu, giới hạn chạy lại, cỡ mẫu, cấu trúc YAML và dữ liệu gốc.

Phần tự kiểm tra của cá nhân Tuấn: **chờ xác nhận**. Cần tự chạy lệnh ở bản bàn giao, giải thích vì sao cộng mọi lần chạy nhưng chia số thành công, vì sao B3 chọn 2 lần và vì sao 20 cụm/nhóm không đủ cho MDE 5 điểm. Các kiểm tra do Codex chạy không được ghi thành đã chạy trên máy thành viên khác.

## 6. Cập nhật tích hợp toàn nhóm

Sau khi nhận thêm yêu cầu rà và hoàn thiện, đã pull main TV2/TV3, gộp nhánh TV4 `truien`, giữ danh tính và đóng góp của cả 4 người. Codex hỗ trợ bổ sung phép tính E1 (994/1.200, 48/177, 51/1.200), dự toán đúng phạm vi pilot tối đa 2 lần, thống nhất 14 event, rà báo cáo và lịch mẫu. Chi phí hệ thống có cố định toàn công ty là 6.385,88 đ/yêu cầu (simulated) ở 45.000 yêu cầu/tháng. Kiểm thử và phần chờ thực tế ghi tại [nghiệm thu](nghiem_thu.md).

## 7. Tự đánh giá

Bản nhóm đã nhận báo cáo kiểm số/máy TV2 và nhãn TV3/TV4, tích hợp theo công việc đã giao. Cần Tuấn đọc, tự kiểm tra và bổ sung nhận xét cá nhân; hội đồng thực hiện duyệt chéo. Chưa xác nhận nộp LMS.
