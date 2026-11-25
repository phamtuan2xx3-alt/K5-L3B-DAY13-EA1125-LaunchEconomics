# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200 ca trong đợt chạy thử) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177 ca trong đợt chạy thử) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200 ca trong đợt chạy thử) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ tự động hóa không cần can thiệp | Số yêu cầu không phát sinh event `handoff_to_staff`, chia tổng số yêu cầu | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền phát hiện qua kiểm toán | Số đơn có lệch tiền qua `audit_sample_checked`, chia tổng số đơn kiểm tra mẫu hàng tuần | Không cần tính |

*Ghi chú:* Chỉ số trong đợt chạy thử 2 tuần là 82,83% (chính), 27,12% (bỏ qua gợi ý), và 4,25% (lỗi lọt đến khách). Không khẳng định trợ lý đã nâng chỉ số do đợt chạy thử chưa có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng | `request_id`, `loai`, `so_tien_vnd`, `arm`, `trace_id` | Khi khách hàng bắt đầu gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý (Agent) | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần trợ lý chạy xong một lượt (kể cả lượt lỗi) |
| `staff_review_decision` | Nhân viên CSKH | `staff_id`, `quyet_dinh_xem_lai` (`giu`/`sua`/`bo`), `phut_xem_lai_simulated`, `trace_id` | Khi nhân viên hoàn thành xem lại và gửi quyết định |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id`, `phut_lam_lai_simulated`, `ly_do`, `trace_id` | Khi nhân viên xử lý làm lại xong yêu cầu bị sai |
| `refund_ledger_written` | Dịch vụ sổ cái | `idempotency_key`, `so_tien_vnd`, `status` (`OK`/`FAIL`), `trace_id` | Khi giao dịch hoàn tiền được ghi nhận vào sổ cái tài chính |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `dong_trong_24h`, `trace_id` | Khi yêu cầu được xử lý xong và đóng lại |
| `ticket_reopened` | Khách hàng | `reopened_at`, `mo_lai_trong_7_ngay`, `ly_do`, `trace_id` | Khi khách hàng mở lại khiếu nại trong vòng 7 ngày |
| `audit_sample_checked` | Kế toán / Kiểm toán | `so_tien_da_hoan`, `so_tien_chuan`, `lech_tien`, `trace_id` | Định kỳ hàng tuần khi kiểm tra ngẫu nhiên mẫu đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24h & không mở lại trong 7 ngày):** Đo bằng cách lọc các yêu cầu có event `ticket_closed` với thuộc tính `dong_trong_24h == 1` và không có event `ticket_reopened` với thuộc tính `mo_lai_trong_7_ngay == 1` cùng `trace_id`.
- **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** Đếm số event `staff_review_decision` có thuộc tính `quyet_dinh_xem_lai` mang giá trị `sua` hoặc `bo`, chia cho tổng số event `staff_review_decision` phát sinh.
- **Chỉ số an toàn (Tỉ lệ lỗi lọt đến khách):** Đếm số event `ticket_reopened` có thuộc tính `mo_lai_trong_7_ngay == 1`, chia cho tổng số event `refund_request_created`.
- **Chỉ số dùng đề xuất (Tự động hóa không cần can thiệp):** Đếm số `trace_id` không xuất hiện event `handoff_to_staff`, chia cho tổng số event `refund_request_created`.
- **Chỉ số an toàn đề xuất (Tỉ lệ hoàn sai tiền qua kiểm toán):** Đếm số event `audit_sample_checked` có `lech_tien != 0`, chia cho tổng số event `audit_sample_checked` được ghi nhận.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công (CPS) toàn mẫu tăng từ 4.471,97 đ lên 6.786,90 đ (+51,8%) [simulated] | Tỉ lệ làm lại theo tuần trong phạm vi > 7% (đợt chạy thử hiện là 48/982 = 4,89%) | Rà soát 20 trace làm lại, cập nhật chi phí theo phút đo thật; cân nhắc thu hẹp phạm vi về `noi_dia` | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | CPS phạm vi pilot là 11.742,79 – 12.414,50 đ, xấp xỉ 0,98× – 1,03× so với nhân viên tự làm (12.000 đ) [simulated] | Tỉ lệ xem lại vẫn còn > 50% ở cuối bước rollout 0.25 (10 nhân viên) | Giảm tỷ lệ xem lại theo bậc khi tỷ lệ sửa + bỏ < 15%; thiết kế lại thao tác xem lại của nhân viên | Trưởng nhóm CSKH |
| Khối lượng yêu cầu giảm một nửa | Chi phí cố định (40 triệu đ/tháng) mỗi việc tăng từ 1.185,19 đ lên 2.370,37 đ; CPS có cố định tăng từ 4.599,09 đ lên 5.784,27 đ [simulated] | Số việc thành công thực tế đạt < 50% giả định kế hoạch (dưới 16.875 việc/tháng) | Đàm phán lại chi phí cố định hạ tầng, tạm dừng mở rộng quy mô cho đến khi lưu lượng phục hồi | PM trợ lý hoàn phí |
