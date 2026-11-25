# Rà soát tích hợp DAY13 · 25/11/2026

Nhóm EA1125 · L3B-H202. Nguồn nghiệm thu: [rubric](../../RUBRIC.md), [checkpoints](../../CHECKPOINTS.md), [quy tắc](../../RULES.md), [nộp bài](../../SUBMISSION.md). Bản tích hợp nhận main `cf78f04` và nhánh TV4 `f9dd0b0` qua merge `8f86b35`; không bỏ lịch sử hoặc sửa hai bộ nhãn.

## Bằng chứng kỹ thuật

Windows, Python 3.12.10, môi trường `src/.venv`, `PYTHONUTF8=1`. Từ root chạy:

```powershell
$env:PYTHONUTF8 = '1'
.\src\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Từ `src/` chạy:

```powershell
.\.venv\Scripts\python.exe lab13.py --output ../report/team/TV1_ket_qua.txt
```

13 kiểm thử gồm 9 kiểm thử ban đầu và 4 kiểm thử E1/mẫu số/CLI/dự toán pilot mới. Các kiểm thử mới đã được chạy thất bại vì thiếu hành vi, sau đó bổ sung code và chạy đạt. Kết quả bản tích hợp: **13 đạt, 0 lỗi, 0 bỏ qua**, exit 0; CLI từ `src/` exit 0, output khớp bản lưu. Kiểm tra độc lập đã chạy lại sau khi làm rõ cohort an toàn.

| Tiêu chí | Bằng chứng và cách kiểm | Trạng thái |
| --- | --- | --- |
| A1 | 1,20 / 1,25 / 1,25 đạt trước khi in bảng | Đã kiểm tra |
| A2–A4 | 9 dòng A2, 4 loại A3, 2 lưu lượng A4; số code khớp tài liệu trong dung sai 2% | Đã kiểm tra |
| B1–B4 | 9 kịch bản; cặp tuyến tính; B3 chọn 2 lần; B4 948 xem/48 làm lại, CPS 11.742,79–12.414,50 đ (simulated) | Đã kiểm tra |
| Dự toán pilot | Đúng phạm vi, 2 lần: 892 thành công/982; 90 làm thay, 218 ngoài phạm vi; hệ thống toàn công ty có cố định 6.385,88 đ/yêu cầu (simulated) | Đã kiểm tra |
| C · file và số | Hai bộ nhãn ghi tên Nhật/Truyền; 18/20 trùng, 2 bất đồng, 5 ca đủ loại; giữ nguyên cột nhãn thành viên đã nộp | Đã đối chiếu file; quy trình gắn độc lập theo tự khai TV3/TV4 |
| D1/D2 | 1.251 độc lập/nhóm; DE 2,48 ở m75; 42 nhân viên/nhóm không đủ; trần 1.000/300; MDE 6 cần 859 hiệu dụng, 299 ca/người | Đã kiểm tra |
| YAML | Parse được, đủ trường, không dấu hỏi, 4 luật dừng; tối đa 2 lần; 20 cụm/nhóm, đúng 299 ca đầu/người; lịch có đủ cửa sổ | Đã kiểm tra cấu trúc/kế hoạch; chưa chạy pilot |
| E1 | Code `tinh_e1`: 994/1.200, 48/177, 51/1.200; thiếu mẫu số trả chưa có dữ liệu; unreviewed không vào mẫu số bỏ qua | Đã kiểm tra |
| Event/rủi ro | 14 event có trace/request/time; 4 chỉ số đề xuất; 4 rủi ro từ code; đo phút thật và khử trùng giao dịch riêng | Đặc tả hoàn thiện, chưa phải log đã triển khai |
| Hồ sơ nhóm | Launch đủ 7 mục, 3 trạng thái đúng mẫu, có vai trò/ngày kiểm tra và đề xuất cuối; báo cáo nhóm 8 mục | Đã rà nội dung và định dạng Markdown |
| File/nguồn | Đủ 6 file hồ sơ, 4 báo cáo cá nhân; giữ nguyên CSV/starter/template, không secret/venv trong Git | Đã kiểm bằng diff/hash/file list |
| Cá nhân và kiểm máy khác | Tùng tự khai 9/9 test của bản TV1 ban đầu trên máy TV2; bản tích hợp 13 test có E1/dự toán mới chưa được TV2 xác nhận lại; tự kiểm của Tuấn còn chờ | Không coi lượt chạy Codex là máy thứ hai hoặc xác nhận cá nhân |
| Hội đồng và LMS | Phiếu có tên người ghi/theo đúng rubric, chưa ghi điểm giả; không có quyết định thực tế hoặc biên nhận LMS | **Chưa xác nhận** |

## Các sửa đổi có ý nghĩa

- Gộp nhánh TV4 và giữ phần TV3, khôi phục đủ 4 danh tính; sửa bảng lịch TEAM thừa cột.
- E1 trước chỉ có con số trong Markdown, nay tính và in từ code cùng output A–D.
- Tên event hai nhánh trước khác nhau, có chỉ số gọi event chưa được liệt kê; nay thống nhất 14 event, trường thời gian/khóa nối/khử trùng, cả run lỗi và sự kiện làm lại/chuyển người/thông báo/kiểm toán.
- B4 trước gọi phút simulated là thực tế; đã sửa. Tổng A2 không cộng lặp phần chạy lại; tỷ lệ dẫn xuất mang nhãn simulated.
- Dự toán pilot tách đúng phạm vi 2 lần khỏi số gốc 3 lần; cộng đầy đủ ca làm thủ công và cố định với cùng mẫu số toàn công ty.
- Lịch dự kiến dành 2 tuần/bước thay vì chuyển bước trước khi cohort trưởng thành; thu chính 28/12/2026–10/01/2027, khóa sau 23:59 ngày 18/01, quyết định 20/01 (GMT+7). Thiếu điều kiện thì giữ bước và No-go mở rộng, không giả đủ mẫu.

## Giới hạn nghiệm thu

Chưa có bằng chứng để chốt trọn bài nhóm: bản tích hợp mới chưa có xác nhận chạy trên máy TV2; hội đồng chưa ghi điểm/quyết định thực tế; Tuấn chưa tự xác nhận kiểm bài; chưa có xác nhận mỗi người nộp LMS; điều kiện khởi động pilot là dự kiến. Không dùng kiểm thử tự động hoặc báo cáo này làm bằng chứng các hoạt động đó đã diễn ra. Không tự cho điểm 30/30 hội đồng.

**Kết quả kiểm tra độc lập cuối:** **Technical PASS**, không còn lỗi bắt buộc sửa mức P0–P2. Đối chiếu CSV bằng phép tính độc lập xác nhận A–B, E1 và dự toán pilot; YAML, lịch, nhãn và output đã được kiểm. **Full-course GAPS_FOUND** cho các phần thực tế nêu trên; quy trình gắn nhãn độc lập chỉ được xác nhận qua báo cáo của hai người, không thể chứng minh cách thực hiện chỉ bằng kiểm file. Không chốt hoàn tất toàn bài hoặc điểm hội đồng từ kết quả kỹ thuật này.
