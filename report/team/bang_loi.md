# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Chu Văn Nhật (2A202603848) · Người gắn nhãn 2: Nguyễn Trọng Truyền (2A202603868) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | :---: | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Hệ thống | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = 90%

Giữ nguyên hai cột nhãn đã được TV3/TV4 nộp qua commit `79d7c81` và `f9dd0b0`; lượt tích hợp không thay nhãn gốc hoặc giả làm người gắn nhãn. Tỷ lệ được kiểm lại bằng 18 dòng trùng/20 dòng; cột thống nhất khớp 20/20 nhãn tham chiếu trong hướng dẫn lab. Định nghĩa và bằng chứng tự khai nằm trong báo cáo của Nhật và Truyền.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 6 (Do người dùng vs Hệ thống):** Nguyên nhân gốc là khách chọn sai phân loại (hàng vỡ nhưng chọn giao trễ); việc bot chưa hỗ trợ phát hiện nội dung là tính năng cần cải tiến, không phải nguyên nhân gốc gây ra lỗi nên quy về "Do người dùng".
- **Ca 13 (Giới hạn hệ thống vs Hệ thống):** Yêu cầu hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi xử lý được thiết kế của trợ lý; khi tác vụ ngoài phạm vi thì bản chất là "Giới hạn hệ thống", kể cả khi câu trả lời từ chối của trợ lý chưa khéo léo.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi quá 2% số yêu cầu/ngày | Tự động nhận diện định dạng mã sàn TMĐT và tra cứu sang mã vận đơn nội bộ LogiX; nếu không tra cứu được thì hiển thị hướng dẫn kèm hình ảnh minh họa vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Mỗi giờ nối `customer_notification_sent` loại `refund_confirmed` với `refund_ledger_write` theo `request_id` và `refund_operation_id`; ≥1 ca thiếu xác nhận thành công trước thông báo thì cảnh báo | Chỉ thông báo khi sổ cái xác nhận thành công; mã HTTP 200 đơn thuần chưa đủ. Quá giới hạn 2 lần chạy pilot thì báo đang xử lý và chuyển nhân viên; giữ cùng idempotency_key khi thử lại | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Hằng tuần, số request `ticket_reopened.reason=so_tien` được kiểm toán xác nhận đúng chính sách / số request trưởng thành; ≥2% thì rà nội dung, thiếu mẫu báo riêng | Mẫu tin nhắn ghi cách tính rõ, ví dụ phí 30.000 đ ×50% =15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Thống kê hằng ngày `handoff_to_staff.reason=thieu_du_lieu` theo loại; ≥1 ca quoc_te được bật trợ lý trong pilot thì báo cấu hình sai | Chuyển nhân viên kèm tóm tắt; loại quoc_te khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra đối soát ngẫu nhiên 100 đơn/tuần so với bảng giá hiện hành trên cơ sở dữ liệu; ngưỡng cảnh báo: lệch từ 1% số đơn | Tự động xóa cache cấu hình giá khi có sự kiện cập nhật bảng giá mới; đồng thời ghi rõ phiên bản bảng giá (price_version) vào trace của mỗi lượt chạy | Kế toán trưởng |

Các ngưỡng là đề xuất cho pilot, không phải sự kiện đã quan sát. Danh sách event, thời gian và khóa nối chuẩn nằm ở [chi_so.md](chi_so.md); `audit_sample_checked` dùng tiền chuẩn và price_version để bắt lỗi ngầm, không chỉ dựa vào khiếu nại của khách.
