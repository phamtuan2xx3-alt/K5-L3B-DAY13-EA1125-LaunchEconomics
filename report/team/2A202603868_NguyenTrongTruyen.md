# Báo cáo cá nhân — NguyenTrongTruyen-2A202603868

## 1. Thông tin thành viên

- Họ tên: Nguyễn Trọng Truyền
- MSSV: 2A202603868
- Email: trongtruyen04@gmail.com
- GitHub: truien
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): TV4 — Người gắn nhãn độc lập 2; giữ hồ sơ launch v0, rà nhất quán kế hoạch pilot, ghi duyệt chéo và tổng hợp báo cáo nhóm.

## 2. Phần việc phụ trách

- Tham gia gắn nhãn độc lập 20 ca lỗi ở Nhiệm vụ C (CP3) cùng TV3, giữ nguyên hai bộ nhãn gốc, thống nhất quy tắc cho các ca bất đồng và bảng khắc phục 5 ca.
- Rà soát tính nhất quán giữa `pilot_plan.yaml`, `bang_chi_phi.md`, `bang_loi.md` và `chi_so.md` trước cổng Gate 2a.
- Hoàn thiện hồ sơ 1 trang `report/team/ho_so_launch_v0.md` đủ 7 mục, đúng nhãn trạng thái (`Xong, có bằng chứng` / `Giả lập` / `Chưa`), người phụ trách là vai trò cụ thể và đề xuất cuối khớp bằng chứng.
- Hỗ trợ hoàn thiện `report/team/chi_so.md` (tính 3 chỉ số E1 từ `src/logix_requests.csv`, đặc tả 7 event có `trace_id`, ánh xạ kiểm tra chéo và ghép 4 rủi ro kinh tế từ `TV1_ban_giao.md`) để đảm bảo đủ bằng chứng cho mục 4 và mục 7 của hồ sơ.
- Tổng hợp báo cáo nhóm `report/team/group_report.md`, cập nhật thông tin và đóng góp thực tế trong `TEAM.md`, chuẩn bị `report/team/phieu_cham.md` cho buổi duyệt chéo Gate 2a và rà checklist trước khi nộp.

## 3. Đóng góp cụ thể

- Xử lý xung đột Git (`TEAM.md`) khi đồng bộ nhánh `main` và kiểm tra toàn bộ đầu ra của TV1, TV2, TV3.
- Cập nhật tên Người gắn nhãn 2 trong `report/team/bang_loi.md` (đồng thuận 18/20 = 90%).
- Hoàn thiện `report/team/chi_so.md` với 3 chỉ số E1 tính từ `src/logix_requests.csv` (82,83% · 27,12% · 4,25%), 2 chỉ số tự đề xuất, 7 event có `trace_id`, kiểm tra chéo và 4 rủi ro kinh tế có nhãn `simulated`.
- Hoàn thiện `report/team/ho_so_launch_v0.md` đủ 7 mục trên 1 trang, nêu rõ cả con số bất lợi (xem lại 100% lên 11.743–12.415 đ, `quoc_te` 22.515 đ, đánh đổi MDE 6 điểm) và đề xuất **Go có điều kiện** kèm 4 điều kiện có vai trò phụ trách và ngày kiểm tra.
- Hoàn thiện `report/team/group_report.md` (8 mục, ≤ 2 trang) và cập nhật bảng thành viên, đóng góp, checklist trong `TEAM.md`.
- Giữ nguyên `report/team/phieu_cham.md` để ghi nhận trung thực kết quả buổi duyệt chéo Gate 2a (không bịa số liệu).

## 4. Bằng chứng

- Hồ sơ launch v0: [ho_so_launch_v0.md](ho_so_launch_v0.md)
- Báo cáo nhóm: [group_report.md](group_report.md)
- Đặc tả chỉ số, event và rủi ro kinh tế: [chi_so.md](chi_so.md)
- Cập nhật Người gắn nhãn 2: [bang_loi.md](bang_loi.md)
- Cập nhật thông tin nhóm và đóng góp: [TEAM.md](../../TEAM.md)
- Báo cáo cá nhân: `report/team/2A202603868_NguyenTrongTruyen.md`

## 5. Công cụ AI đã dùng

- Công cụ: Antigravity Assistant.
- Dùng vào việc gì: Hỗ trợ giải thích và xử lý merge conflict Git, chạy lệnh Python tính kiểm chứng 3 chỉ số E1 từ `src/logix_requests.csv`, kiểm tra cú pháp `pilot_plan.yaml` bằng `yaml.safe_load`, tổng hợp văn bản cho `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md` và quét kiểm tra từ cấm/nhãn `simulated`.
- Cách tự kiểm tra kết quả: Tự đối chiếu lại mọi con số trong `ho_so_launch_v0.md` và `group_report.md` với `bang_chi_phi.md`, `TV1_ket_qua.txt`, `bang_loi.md` và `pilot_plan.yaml`; xác nhận tuân thủ quy tắc 5 của `README.md`, mọi con số từ cột `_simulated` đều có nhãn `simulated`, và `phieu_cham.md` không điền khống trước buổi duyệt chéo.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần tổng hợp hồ sơ, báo cáo nhóm, báo cáo cá nhân và rà soát nhất quán trước giờ duyệt chéo Gate 2a.
- Việc còn lại: ghi nhận kết quả thực tế vào `report/team/phieu_cham.md` trong buổi duyệt chéo 17:00–17:45, cập nhật mục kết quả duyệt chéo trong `group_report.md`, commit/push bản cuối và tự nộp link repo trên LMS trước 23:59 GMT+7.
