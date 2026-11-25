# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: EA1125
- Lớp: L3B-H202
- Repo nhóm: `K5-L3B-DAY13-EA1125-LaunchEconomics`
- Thành viên: xem [TEAM.md](../../TEAM.md) (TV1 Phạm Quang Tuấn, TV2 Nguyễn Thanh Tùng, TV3 Chu Văn Nhật, TV4 Nguyễn Trọng Truyền).

## 2. Mục tiêu và cách tiếp cận

Xây dựng bộ **hồ sơ launch v0** cho trợ lý hoàn phí LogiX-VN tại cổng **Gate 2a** (chỉ duyệt kế hoạch pilot, không duyệt chạy chính thức) dựa trên mẫu dữ liệu giả lập 1.200 yêu cầu và 1.624 lần chạy. Nhóm phân công 4 vai rõ ràng và tách bạch người tính toán với người kiểm số, người gắn nhãn 1 với người gắn nhãn 2 độc lập, nhằm trả lời 4 câu hỏi: chi phí thật mỗi việc thành công, mức độ sử dụng và event đo lường, phân loại lỗi/khắc phục, và thiết kế pilot có đối chứng ra được quyết định.

## 3. Giải pháp

- **Nhiệm vụ A & B (Mô hình chi phí và độ nhạy):** TV1 cài đặt `src/lab13.py` và bộ kiểm thử `tests/test_lab13.py`, qua đủ 3 phép thử A1 (1,20 · 1,25 · 1,25). TV2 tự tính tay đối chiếu (độ lệch 0%), chạy 9/9 test đạt trên máy thứ hai và hoàn thiện [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Phân loại lỗi và khắc phục):** TV3 và TV4 gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, đạt đồng thuận 18/20 (90%), thống nhất quy tắc cho 2 ca bất đồng (ca 6, ca 13) và lập bảng khắc phục 5 ca đại diện đủ 5 loại trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Thiết kế pilot):** TV1 và TV2 tính cỡ mẫu cụm (D1) và kiểm tra 5 điều kiện tách tác động (D2), lập kế hoạch rollout, 4 luật dừng đủ 4 vế và quy trình rollback trong [pilot_plan.yaml](pilot_plan.yaml) (đã kiểm tra hợp lệ bằng `yaml.safe_load`, không còn dấu `?`).
- **Nhiệm vụ E (Chỉ số, event, rủi ro và hồ sơ launch v0):** Tính 3 chỉ số E1 trên 1.200 yêu cầu, bổ sung 2 chỉ số tự đề xuất, 7 event có `trace_id` và 4 rủi ro kinh tế trong [chi_so.md](chi_so.md); TV4 rà nhất quán toàn bộ số liệu và chốt hồ sơ 1 trang [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- **Kinh tế (`simulated`):** CPS toàn mẫu là **4.472 đ** (gấp 16,3× hóa đơn token+tool 274,7 đ/yêu cầu); giờ nhân viên chiếm 92,5% tổng chi (làm lại 51,8%, xem lại 40,7%). Phạm vi đề xuất `noi_dia` (2.696 đ, 0,22×) + `hang_nang` (8.221 đ, 0,69×) có CPS cộng cố định 40 triệu đ/tháng là **4.599 đ** (0,38×) ở 45.000 ca/tháng và **5.784 đ** (0,48×) ở nửa khối lượng. Loại `quoc_te` vì CPS **22.515 đ** (1,88×, thành công 27,3%) và `doi_tac` vì điều khoản riêng.
- **Độ nhạy & giới hạn (`simulated`):** 3 yếu tố nhạy nhất là làm lại (+51,8%), xem lại (+40,7%) và lương (+23,1%). Giới hạn **2 lần chạy** rẻ nhất cho toàn hệ thống (**6.901.220 đ**, 5.751 đ/yêu cầu). Nếu xem lại 100%, CPS phạm vi tăng lên **11.743–12.415 đ** (0,98–1,03× so với 12.000 đ), mất lợi thế kinh tế.
- **Chỉ số đợt chạy thử (chưa có đối chứng):** Đóng ≤24h và không mở lại 7 ngày đạt **82,83%** (994/1.200); tỉ lệ bỏ qua gợi ý **27,12%** (48/177); tỉ lệ mở lại 7 ngày **4,25%** (51/1.200; trong phạm vi **3,97%**).
- **Thiết kế pilot:** 20 nhân viên can thiệp + 20 đối chứng phân tầng theo 12 depot, chấp nhận đánh đổi **MDE 6 điểm** (n hiệu dụng 859, 5.980 ca thô/nhóm, DE=6,96) do trần cụm 20 nhân viên không đủ MDE 5 điểm (trần <1.000). Rollout 10% → 25% → 50%, khóa dữ liệu 04/01/2027, quyết định 05/01/2027.
- **Đề xuất cuối (`ho_so_launch_v0.md`):** **Go có điều kiện** cho kế hoạch pilot `noi_dia` + `hang_nang` với giới hạn 2 lần chạy và 4 điều kiện có vai trò phụ trách, hạn kiểm tra rõ ràng trước khi khởi động và sau tuần 1.
- **Kết quả duyệt chéo Gate 2a:** Chờ cập nhật sau buổi duyệt chéo thực tế 17:00–17:45 (phiếu chấm nằm tại [phieu_cham.md](phieu_cham.md)).

## 5. Khó khăn và cách xử lý

- **Xung đột Git khi làm việc song song:** Phát sinh merge conflict tại `TEAM.md` khi kéo nhánh `main` về máy TV4 do cập nhật danh sách thành viên đồng thời. Nhóm dùng `git stash`, đối chiếu trực tiếp giữ bản đầy đủ thông tin từ `origin/main` và kiểm tra lại trạng thái sạch trước khi tổng hợp hồ sơ.
- **Thiếu file `chi_so.md` khi đến bước tổng hợp:** Trước khi chốt `ho_so_launch_v0.md`, TV4 phát hiện `chi_so.md` còn trống; nhóm chạy kiểm tra trực tiếp trên `src/logix_requests.csv` để lấy 3 chỉ số E1 và ghép bảng rủi ro kinh tế từ `TV1_ban_giao.md` nhằm đảm bảo tính nhất quán 100% giữa các file hồ sơ.
- **Đánh đổi cỡ mẫu cụm:** Với 40 nhân viên (20 mỗi nhóm), trần cỡ mẫu hiệu dụng dưới 1.000 không đủ cho MDE 5 điểm (cần 1.251). Nhóm ghi nhận rõ đánh đổi sang MDE 6 điểm (power 64,2% nếu hiệu ứng thật 5 điểm) và đưa vào điều kiện cần Giám đốc vận hành phê duyệt trước pilot.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp thực tế, bằng chứng commit/file và trạng thái nộp LMS của từng thành viên nằm trong [TEAM.md](../../TEAM.md) và 4 báo cáo cá nhân trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu phút nhân viên là giả lập (`simulated`):** Toàn bộ kết luận chi phí phụ thuộc vào `phut_xem_lai_simulated` và `phut_lam_lai_simulated`; cần đo thời gian thật ngay tuần đầu rollout 10% qua cặp event `staff_review_started`/`staff_review_submitted` để hiệu chỉnh lại mô hình.
- **Rủi ro lan truyền (spillover) trong cùng depot:** Nhân viên can thiệp và đối chứng làm việc cùng depot có thể trao đổi gợi ý; cần khóa quyền truy cập theo tài khoản, log `staff_id`/`arm`/`trace_id` và kiểm toán chéo định kỳ.
- **Chưa kiểm chứng trên nhóm `quoc_te` và `doi_tac`:** Chỉ nên đánh giá lại hai nhóm này ở giai đoạn sau khi đã cải thiện nguồn dữ liệu chặng quốc tế và quy tắc hợp đồng đối tác.

## 8. Tài liệu tham khảo

- Bộ đề và hướng dẫn Lab 13: `README.md`, `RULES.md`, `RUBRIC.md`, `SUBMISSION.md`, `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359).
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com).
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`).
