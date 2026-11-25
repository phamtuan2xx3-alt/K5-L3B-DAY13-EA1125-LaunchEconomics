# Báo cáo nhóm · DAY13

## 1. Thông tin nhóm

**EA1125 · L3B-H202** · Repo: [K5-L3B-DAY13-EA1125-LaunchEconomics](https://github.com/phamtuan2xx3-alt/K5-L3B-DAY13-EA1125-LaunchEconomics). Bốn thành viên và mã học viên: [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Lập hồ sơ Gate 2a cho kế hoạch pilot trợ lý hoàn phí LogiX-VN, trả lời bốn câu hỏi kinh tế, sử dụng, xử lý lỗi và khả năng ra quyết định. Mẫu 1.200 yêu cầu/1.624 lần chạy đều giả lập; không có đối chứng nên chưa suy ra tác động nhân quả.

## 3. Giải pháp A–E

- **A–B:** TV1 viết mô hình, TV2 kiểm số và điền [bảng chi phí](bang_chi_phi.md); tử số tính mọi lần chạy, mẫu số chỉ việc thành công. B3 cộng thêm nhân viên làm thay, A4 tính cố định, B4 thử xem lại 100%.
- **C:** TV3 Chu Văn Nhật và TV4 Nguyễn Trọng Truyền đã nộp hai bộ nhãn 20 ca; đồng thuận 18/20=90%, quy tắc cho ca 6/13 và 5 ca khắc phục đủ 5 loại trong [bảng lỗi](bang_loi.md).
- **D:** [YAML](pilot_plan.yaml) có đủ D1/D2, ngẫu nhiên theo nhân viên, rollout, 4 luật dừng và rollback; đánh đổi MDE được ghi trước khi chạy.
- **E:** code đã tính ba chỉ số E1; [đặc tả](chi_so.md) tích hợp đề xuất TV3/TV4 thành 4 chỉ số bổ sung, 14 event và 4 rủi ro. [Hồ sơ launch](ho_so_launch_v0.md) gói đủ 7 mục.

## 4. Kết quả

Chi phí và tỷ lệ chi phí trong đoạn này đều **simulated**. CPS toàn mẫu **4.471,97 đ**, làm lại chiếm **51,8%** tổng. Trong phạm vi noi_dia+hang_nang, số liệu gốc tối đa 3 lần cho CPS có cố định **4.599,09 đ** ở 45.000 yêu cầu/tháng; nửa lưu lượng **5.784,27 đ**. Theo B3, 2 lần rẻ nhất trong ba giới hạn toàn mẫu. Đúng phạm vi pilot và **2 lần**, chi phí hệ thống là **6.385,88 đ/yêu cầu toàn công ty**, gồm làm thay, ca ngoài phạm vi và cố định ở 45.000 ca/tháng; nửa lưu lượng **7.274,77 đ**.

Bất lợi cần xử lý: xem lại 100% đẩy CPS lên **11.742,79–12.414,50 đ**; quoc_te CPS **22.515,16 đ**, chỉ **27,33%** thành công; loại quoc_te và doi_tac khỏi pilot. Trong đợt chạy thử: chính **82,83%**, bỏ qua **27,12%**, mở lại **4,25%**; đây không phải cải thiện so baseline 70%.

Thiết kế: 20 nhân viên/nhóm, MDE 6 điểm, đúng 299 ca đầu/người, 5.980 ca thô/nhóm, DE 6,96; power chỉ **0,6418** nếu hiệu ứng 5 điểm. Lịch đề xuất dành 2 tuần/bước để chờ an toàn và đủ mẫu; chờ 8 ngày từ nhận ca trước khi khóa dữ liệu **18/01/2027**, quyết định **20/01/2027**. Đề xuất cuối **Go có điều kiện**, chưa duyệt khởi động. **Duyệt chéo:** chờ hồ sơ nhóm được chấm và quyết định hội đồng thực tế trong [phiếu chấm](phieu_cham.md).

## 5. Khó khăn và cách xử lý

Nhánh TV4 `truien` chưa vào main; khi tích hợp phát sinh xung đột `TEAM.md` và `chi_so.md`. Đã giữ thông tin cả bốn người, thống nhất tên event, bổ sung sự kiện còn thiếu và phép tính E1 vào code. Phút 15,2973/ca là trung bình simulated, không phải thời gian đo thật; đã sửa cách diễn đạt. Chạy kiểm tra và bằng chứng theo từng tiêu chí: [nghiệm thu](nghiem_thu.md).

## 6. Đóng góp

TV1 Phạm Quang Tuấn: code kinh tế, kế hoạch pilot, bàn giao và tích hợp theo yêu cầu. TV2 Nguyễn Thanh Tùng: kiểm số A–B và báo cáo kiểm thử trên máy TV2. TV3 Chu Văn Nhật: bộ nhãn 1, bảng lỗi, chỉ số/event ban đầu. TV4 Nguyễn Trọng Truyền: bộ nhãn 2, hồ sơ launch, báo cáo nhóm và đặc tả bổ sung. Các đóng góp tự khai được giữ trong 4 báo cáo cá nhân; lượt rà tích hợp bằng Codex được ghi riêng, không thay xác nhận cá nhân.

## 7. Hạn chế và hướng cải thiện

Đo phút thật và kiểm toán ngay bước đầu; chốt danh sách phân nhóm trước pilot, chống chia sẻ gợi ý giữa hai nhóm. Không tăng rollout khi thiếu log, thiếu cohort an toàn trưởng thành hoặc chưa đủ mẫu. Kết quả duyệt chéo, phê duyệt các điều kiện và LMS là việc thực tế còn chờ, không suy ra từ kiểm thử code.

## 8. Nguồn

[Quy tắc](../../RULES.md), [rubric](../../RUBRIC.md), [nộp bài](../../SUBMISSION.md), [công thức](../../docs/du_lieu_va_cong_thuc.md), [hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md); code tham khảo trong repo và công cụ AI theo từng báo cáo cá nhân.
