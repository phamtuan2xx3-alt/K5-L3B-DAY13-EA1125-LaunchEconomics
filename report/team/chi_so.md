# Đặc tả chỉ số, event và rủi ro kinh tế · E1/E2

Nhóm EA1125 · L3B-H202. Chủ trì chỉ số: **Chu Văn Nhật (TV3)**; tích hợp thời gian xem lại và đối soát: **Nguyễn Trọng Truyền (TV4)**. Code tính ba chỉ số: [lab13.py](../../src/lab13.py), hàm `tinh_e1`; [output chung](TV1_ket_qua.txt). Hai CSV đều là dữ liệu giả lập của lab.

## E1 · Chỉ số trong đợt chạy thử

| Loại | Chỉ số | Tử số / mẫu số | Kết quả |
| --- | --- | --- | --- |
| Chính | Đóng trong 24 giờ, không mở lại trong 7 ngày | `dong_trong_24h == 1 AND mo_lai_trong_7_ngay == 0` / tất cả yêu cầu | 994/1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Ca được xem lại có quyết định `sua` hoặc `bo` / ca được xem lại | 48/177 = **27,12%** (41 sửa, 7 bỏ) |
| An toàn | Mở lại trong 7 ngày, chỉ báo lỗi lọt đến khách | Ca `mo_lai_trong_7_ngay == 1` / tất cả yêu cầu | 51/1.200 = **4,25%**; phạm vi pilot 39/982 = **3,97%** |
| Dùng · đề xuất TV3 | Tỷ lệ giải quyết tự động không cần người can thiệp | Ca hoàn tất hợp lệ bởi agent, không có xem lại/làm lại/chuyển nhân viên / yêu cầu can thiệp đã trưởng thành | Chưa có dữ liệu event; không suy từ việc thiếu event chuyển người |
| An toàn · đề xuất TV3 | Tỷ lệ sai tiền trong kiểm toán | Ca kiểm toán có tiền đã hoàn khác tiền chuẩn / số ca được kiểm toán ngẫu nhiên | Chưa có kiểm toán thực tế |
| Dùng · đề xuất TV4 | Phút xem lại trung bình mỗi ca | Tổng `review_duration_sec / 60` / số ca có quyết định xem lại hợp lệ | Chưa đo thật; không dùng phút simulated làm thời gian thực tế |
| An toàn · đề xuất TV4 | Số sự cố hoàn trùng hoặc báo đã hoàn khi chưa ghi sổ | Số ca có hơn 1 giao dịch thành công cho cùng `refund_operation_id`, hoặc thông báo đã hoàn không có xác nhận sổ cái trước đó | Chưa có đối soát thực tế; mục tiêu 0 sự cố |

Trong đợt chạy thử chỉ số chính là 82,83%; đây không phải mức cải thiện từ baseline 70% vì chưa có đối chứng. Mở lại là chỉ báo an toàn, không đồng nghĩa mọi ca đều sai tiền; kiểm toán bổ sung giúp phát hiện lỗi ngầm.

## Danh sách 14 event và cách nối

Mọi event có **`event_id, occurred_at, request_id, trace_id, staff_id, arm`**. `event_id` dùng khử event gửi lại; `request_id` là khóa ổn định qua mọi lần chạy. CSV hiện có trace theo từng run, nên không đếm trace như số yêu cầu; pilot phải lưu ánh xạ trace/run về request. Thời gian ghi ISO 8601 có múi giờ; báo cáo theo GMT+7.

| Event | Nguồn | Thuộc tính riêng ngoài trường chung | Khi ghi |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống CSKH | `loai, depot_id, so_tien_vnd, assigned_arm` | Tiếp nhận, lưu nhóm phân ban đầu |
| `input_validation_failed` | Hệ thống nhận đầu vào | `field, reason` | Kiểm tra mã/loại thất bại |
| `agent_run_completed` | Agent | `run_id, attempt, tokens_in, tokens_out, tool_calls, status, price_version` | Mọi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `run_id, suggestion_id, so_tien_de_xuat` | Gợi ý thật sự hiện trên màn hình |
| `staff_review_started` | Giao diện CSKH | `review_id, suggestion_id` | Bắt đầu xem lại |
| `staff_review_decision` | Giao diện CSKH | `review_id, quyet_dinh_xem_lai, review_duration_sec, is_final` | Giữ/sửa/bỏ; thời gian đo thật |
| `staff_rework_completed` | Nhân viên CSKH | `rework_id, rework_duration_sec, reason` | Làm lại xong; thời gian đo thật |
| `refund_ledger_write` | Dịch vụ sổ cái | `refund_operation_id, transaction_id, order_id, idempotency_key, so_tien, status, http_status` | Mỗi yêu cầu ghi sổ, gồm thành công/lỗi |
| `handoff_to_staff` | Agent/CSKH | `reason, summary` | Chuyển nhân viên |
| `customer_notification_sent` | Dịch vụ thông báo | `notification_id, message_type, refund_operation_id` | Đã gửi thông báo, gồm loại `refund_confirmed` |
| `ticket_closed` | Hệ thống ticket | `closed_at, handled_by, resolution_status` | Đóng lần đầu và người xử lý |
| `ticket_reopened` | Hệ thống ticket | `reopened_at, reason` | Mở lại, không giới hạn chỉ trong 7 ngày |
| `audit_sample_checked` | Kế toán trưởng | `audit_id, refund_operation_id, so_tien_da_hoan, so_tien_chuan, price_version` | Kiểm tra mẫu ngẫu nhiên |
| `event_window_finalized` | Hệ thống giám sát | `window_end, sources_complete, missing_sources` | Khóa cửa sổ sau khi xác nhận đủ log mọi nguồn |

Chỉ số và luật dừng dùng tên chuẩn trên; các tên `staff_review_submitted`, `ledger_refund_confirmed`, `refund_request_closed/reopened` trong bản nháp TV4 được thống nhất về `staff_review_decision`, `refund_ledger_write`, `ticket_closed/reopened`. Event hoàn tất cửa sổ là điều kiện kiểm tra độ đầy đủ log, chưa được coi là đã triển khai.

## Kiểm tra chéo và cửa sổ đo

- **Chính:** mẫu số là tất cả request đúng phạm vi, nhận ở bước 0.50, đã qua 8 ngày từ tiếp nhận (24 giờ đóng + 7 ngày theo dõi). Nối created–closed–reopened theo `request_id`; ca không đóng hoặc chuyển người vẫn nằm trong mẫu số theo nhóm ban đầu. Tử số đóng lần đầu trong 24 giờ và không có lần mở lại trong 7 ngày sau đóng.
- **Bỏ qua:** đếm mỗi request được xem lại một lần, lấy quyết định cuối `is_final` của `staff_review_decision`; tử số sửa/bỏ, mẫu số mọi quyết định hợp lệ gồm giữ. Đối chiếu với `staff_review_started`; ca đã mở nhưng chưa quyết định được báo riêng, không mặc định là giữ.
- **Mở lại:** đếm request duy nhất có ít nhất một `ticket_reopened` trong 7 ngày sau đóng, chia tất cả request trong cohort đã khóa theo ngày nhận, chọn theo thứ tự thời gian và đủ ≥100 ca/arm khi ra quyết định. Chờ đủ 7 ngày sau đóng với ca đóng muộn; ca chưa đóng/thiếu log ghi chưa có kết quả, không chọn bỏ ngày lỗi. Chưa hoàn chỉnh cohort quyết định thì chưa tăng rollout; các ca mới ở cohort khác báo riêng, không làm cohort cũ mất trưởng thành. Hoàn trùng được kiểm ngay trên mọi ca.
- **Tự động hóa:** nối created, shown và closed (`handled_by=agent, resolution_status=thanh_cong`), loại request có review/rework/handoff. Chỉ tính sau `event_window_finalized.sources_complete=true`; thiếu log thì chỉ số là chưa đo được, không tăng giả tỷ lệ tự động.
- **Sai tiền kiểm toán:** lấy từng `audit_id` hợp lệ của mẫu chọn ngẫu nhiên; đếm request có tiền khác chuẩn, chia số request được kiểm toán. Không dùng mẫu thuận tiện để suy tỷ lệ toàn bộ.
- **Phút xem lại:** nối started/decision bằng `review_id`, cộng thời gian đo thật của các lượt trong từng request rồi lấy trung bình trên số request đã xem lại xong; trường hợp đo thiếu/âm báo riêng, không thay bằng 0.
- **Hoàn trùng/lệch sổ:** khử event theo `event_id`, giao dịch theo `transaction_id`; hai event nhắc lại cùng giao dịch không phải hoàn trùng. Hai giao dịch thành công khác nhau cho cùng `refund_operation_id` là sự cố. Nối thông báo `refund_confirmed` với giao dịch thành công cùng thao tác và thời điểm ghi sổ trước thông báo; HTTP 200 đơn thuần không đủ nếu `status` chưa xác nhận thành công.
- **Chi phí/luật dừng:** token/tool từ mọi run, xem lại/làm lại từ thời gian đo thật, chuyển người từ handoff; không trộn phút simulated. Ngưỡng an toàn dùng đúng cohort đủ theo dõi và mẫu tối thiểu trong [YAML](pilot_plan.yaml); mọi thống kê phân theo arm và staff, không khẳng định hiệu quả giữa kỳ.

## E2 · Rủi ro kinh tế

Nguồn: [bảng chi phí](bang_chi_phi.md), [output code](TV1_ket_qua.txt). Tác động B1 tính trên toàn mẫu 1.200 yêu cầu, B4/A4 trong phạm vi `noi_dia + hang_nang`; mọi số chi phí và tỷ lệ chi phí dưới đây là **simulated**. Ngưỡng hành động là đề xuất, chưa hiệu chỉnh bằng dữ liệu thật.

| Rủi ro | Tác động đã tính (simulated) | Dấu hiệu theo dõi | Hành động | Vai trò |
| --- | --- | --- | --- | --- |
| Làm lại ×2 | CPS 4.471,97→6.786,90 đ (+51,8%) | Tỷ lệ làm lại >7%/tuần; mẫu hiện tại 48/982=4,89% | Rà 20 trace; sau giai đoạn xem lại 100%, CPS >8.000 đ và đủ 100 thành công/tuần trong 2 tuần thì thu hẹp về noi_dia | PM trợ lý hoàn phí |
| Xem lại ×2 hoặc 100% kéo dài | CPS 6.292,01 đ (+40,7%); xem 100%: 11.742,79–12.414,50 đ (0,979–1,035× baseline) | Cuối bước 0.25 vẫn xem >50%, hoặc trung bình xem >4,803 phút khi làm lại 15,2973 phút/ca | Đo review_started/decision, rút thao tác; chỉ giảm 100%→50%→25% khi sửa+bỏ <15% và kiểm toán 100 ca/tuần không sai tiền/hoàn trùng | Trưởng nhóm CSKH |
| Lương +25% | CPS 5.505,71 đ (+23,1%); giờ người chiếm 92,5% tổng | Đơn giá đạt hoặc vượt 2.500 đ/phút | Ưu tiên giảm làm lại và phút xem thay vì chỉ giảm giá token | Giám đốc vận hành |
| Lưu lượng giảm nửa | Cố định/việc 1.185,19→2.370,37 đ; CPS có cố định 4.599,09→5.784,27 đ | Số thành công trong phạm vi <16.875/tháng | Tính lại phân bổ 40 triệu/tháng theo lưu lượng thực; chưa mở rộng khi kinh tế chưa đạt | PM trợ lý hoàn phí |
