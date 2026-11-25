# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994 / 1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` (41) hoặc `bo` (7), chia số yêu cầu được xem lại (177) | 48 / 177 = **27,12%** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51 / 1.200 = **4,25%** (trong phạm vi `noi_dia` + `hang_nang`: 39 / 982 = **3,97%**) |
| Dùng | Thời gian xem lại trung bình mỗi ca được xem lại (phút) | Tổng thời gian từ lúc nhân viên mở màn hình xem lại đến khi chốt quyết định (`giu`/`sua`/`bo`), chia số ca được xem lại | Không cần tính |
| An toàn | Số ca hoàn trùng hoặc báo "đã hoàn" khi sổ cái chưa ghi nhận | Số `trace_id` có 2 lệnh hoàn trùng mã vận đơn hoặc có event gửi thông báo "đã hoàn" nhưng không khớp `ledger_refund_confirmed` (200/OK) | Không cần tính |

Chỉ số trong đợt chạy thử là **82,83%** đóng trong 24 giờ không mở lại trong 7 ngày, tỉ lệ bỏ qua gợi ý là **27,12%** (48/177 ca xem lại), và tỉ lệ lỗi lọt đến khách là **4,25%** (51/1.200). Không kết luận trợ lý đã nâng chỉ số vì đợt chạy thử 2 tuần không có nhóm đối chứng.

## Danh sách event

Mỗi event bắt buộc mang `trace_id` để nối với trace của agent và đối soát sổ cái.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống tiếp nhận CSKH | `request_id`, `loai_yeu_cau`, `depot_id`, `staff_id`, `arm`, `created_at`, `trace_id` | Khi khách gửi yêu cầu hoàn phí và được gán nhân viên xử lý |
| `agent_suggestion_generated` | Trợ lý hoàn phí (agent) | `request_id`, `attempt`, `de_xuat_so_tien`, `price_version`, `token_in`, `token_out`, `tool_calls`, `trace_id` | Khi agent hoàn tất một lần chạy gợi ý |
| `staff_review_started` | Giao diện CSKH | `request_id`, `staff_id`, `arm`, `started_at`, `trace_id` | Khi nhân viên mở màn hình xem lại gợi ý của trợ lý |
| `staff_review_submitted` | Giao diện CSKH | `request_id`, `staff_id`, `quyet_dinh_xem_lai` (`giu`/`sua`/`bo`), `review_duration_sec`, `submitted_at`, `trace_id` | Khi nhân viên chốt giữ, sửa hoặc bỏ gợi ý |
| `ledger_refund_confirmed` | Dịch vụ sổ cái hoàn phí | `request_id`, `order_id`, `so_tien_hoan`, `idempotency_key`, `http_status`, `confirmed_at`, `trace_id` | Khi lệnh hoàn phí được ghi sổ cái thành công (200/OK) hoặc trả lỗi |
| `refund_request_closed` | Hệ thống CSKH | `request_id`, `closed_at`, `dong_trong_24h`, `handled_by` (`agent`/`staff`), `trace_id` | Khi yêu cầu hoàn phí chuyển trạng thái đóng và gửi thông báo cho khách |
| `refund_request_reopened` | Hệ thống CSKH | `request_id`, `reopened_at`, `days_since_close`, `reopen_reason`, `trace_id` | Khi khách khiếu nại mở lại yêu cầu sau khi đã đóng |

**Kiểm tra chéo:**

- **% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày (Chính):** tính từ `refund_request_created` (mẫu số đủ 8 ngày trưởng thành), `refund_request_closed` (`closed_at - created_at <= 24h`) và không có `refund_request_reopened` với `days_since_close <= 7` cùng `trace_id`.
- **Tỉ lệ bỏ qua gợi ý (Dùng):** tử số là số `staff_review_submitted` có `quyet_dinh_xem_lai` thuộc `{sua, bo}`; mẫu số là tổng số `staff_review_submitted`.
- **Tỉ lệ lỗi lọt đến khách (An toàn):** tử số là số `refund_request_reopened` có `days_since_close <= 7`; mẫu số là tổng số `refund_request_created` đã qua cửa sổ 8 ngày.
- **Thời gian xem lại trung bình (Dùng, tự đề xuất):** tính trực tiếp từ `review_duration_sec` (hoặc chênh `submitted_at - started_at`) giữa `staff_review_started` và `staff_review_submitted` cùng `trace_id`.
- **Số ca hoàn trùng / lệch sổ cái (An toàn, tự đề xuất):** đối soát `ledger_refund_confirmed` (đếm trùng `order_id` hoặc thiếu trạng thái `200/OK`) với `refund_request_closed` cùng `trace_id`.

## E2 · Rủi ro kinh tế

Số liệu lấy từ bảng độ nhạy ([bang_chi_phi.md](bang_chi_phi.md)) và đầu vào bàn giao của TV1 ([TV1_ban_giao.md](TV1_ban_giao.md)). Mọi con số chi phí dùng phút giả lập đều mang nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS toàn mẫu tăng từ 4.472 đ lên **6.787 đ** (**+51,8%**, `simulated`); làm lại hiện đã chiếm 51,8% tổng chi phí | Tỉ lệ ca làm lại theo tuần trong phạm vi vượt 7% (mẫu chạy thử: 48/982 = 4,89%) hoặc phút làm lại thực tế vượt 15 phút/ca | Rà 20 trace làm lại gần nhất, sửa nguyên nhân gốc, cập nhật mô hình chi phí bằng phút đo thật; nếu CPS biến đổi > 8.000 đ trong 2 tuần thì thu hẹp về `noi_dia` và giới hạn 2 lần chạy | PM trợ lý hoàn phí |
| Tỉ lệ xem lại tăng gấp đôi hoặc giữ ở mức 100% kéo dài | Xem lại ×2 đẩy CPS toàn mẫu lên **6.292 đ** (**+40,7%**, `simulated`). Xem lại 100% trong phạm vi `noi_dia` + `hang_nang` đẩy CPS lên **11.743 đ** (0,98×, giả định làm lại 9 phút) đến **12.415 đ** (1,03×, trung bình dữ liệu 15,3 phút) (`simulated`), triệt tiêu lợi ích so với 12.000 đ | Tỉ lệ xem lại vẫn > 50% cuối bước rollout 25%, hoặc thời gian xem lại trung bình đo thật > 4,8 phút/ca | Đo thời gian xem lại thật qua `staff_review_started`/`submitted`, cải thiện giao diện để rút phút xem lại, và chỉ giảm tỉ lệ xem lại theo bậc 100% → 50% → 25% khi tỉ lệ sửa+bỏ < 15% và kiểm toán 100 ca/tuần không sai tiền | Trưởng nhóm CSKH |
| Chi phí lương nhân viên tăng 25% | CPS toàn mẫu tăng từ 4.472 đ lên **5.506 đ** (**+23,1%**, `simulated`) do giờ nhân viên chiếm 92,5% tổng chi | Đơn giá giờ công CSKH tăng vượt 2.500 đ/phút | Ưu tiên giảm ca làm lại và rút ngắn thao tác xem lại (hiệu quả hơn tối ưu giá token vốn chỉ tác động +5,6% khi ×2) | Giám đốc vận hành LogiX-VN |
| Lưu lượng giảm một nửa so với giả định 45.000 yêu cầu/tháng | Chi phí cố định phân bổ tăng gấp đôi từ 1.185 đ lên **2.370 đ/việc**; CPS cộng cố định trong phạm vi tăng từ **4.599 đ** (0,38×) lên **5.784 đ** (0,48×) (`simulated`) | Số việc thành công trong phạm vi < 16.875 việc/tháng (< 50% giả định 33.750) | Cập nhật lại mức phân bổ cố định 40 triệu đ/tháng theo lưu lượng thực tế và đánh giá lại ngưỡng hòa vốn trước khi mở rộng phạm vi | PM trợ lý hoàn phí |
