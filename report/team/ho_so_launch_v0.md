# Hồ sơ launch v0 · LogiX-VN · Gate 2a

**EA1125 · L3B-H202 · 25/11/2026.** Phạm vi đề xuất: `noi_dia + hang_nang`, tối đa 2 lần chạy. Mọi chi phí và tỷ lệ chi phí là **simulated**, chưa chứng minh hiệu quả của pilot tương lai.

| Mục | Bằng chứng chính | Trạng thái | Vai trò phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu **4.471,97 đ**, gấp 16,3× hóa đơn/yêu cầu. Phạm vi: CPS 3.413,90 đ; có cố định 40 triệu/tháng: **4.599,09 đ** ở 45.000 yêu cầu/tháng, nửa lưu lượng **5.784,27 đ** (simulated; số gốc tối đa 3 lần). | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: **+51,8%**; xem lại ×2: **+40,7%**; lương +25%: **+23,1%** lên CPS (simulated). | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Baseline 12.000 đ/yêu cầu. Chỉ chạy phạm vi pilot, tối đa **2 lần**: **6.385,88 đ/yêu cầu toàn công ty**, gồm người làm thay, ca ngoài phạm vi và cố định ở 45.000 ca/tháng; nửa lưu lượng **7.274,77 đ** (simulated). B4 xem 100%: CPS **11.742,79–12.414,50 đ** (simulated), có thể mất lợi thế. | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số | Chạy thử chưa có đối chứng: chính **994/1.200=82,83%**; bỏ qua **48/177=27,12%**; mở lại **51/1.200=4,25%**. Đủ đặc tả 4 chỉ số đề xuất và **14 event**, chưa phải log đã triển khai. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 5 · Lỗi và khắc phục | Hai bộ nhãn TV3/TV4 đã nộp: đồng thuận **18/20=90%**, 2 quy tắc bất đồng, 5 ca đủ 5 loại với cách đo và vai trò phụ trách. | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | Ngẫu nhiên **20+20 nhân viên**, phân tầng depot; **MDE 6 điểm**, 299 ca/người, 5.980 ca thô/nhóm, DE 6,96. Nếu hiệu ứng 5 điểm, power **0,6418**. Rollout 4→10→20 người, dự kiến 2 tuần/bước, 4 luật dừng; khóa 18/01/2027, quyết định 20/01/2027; chưa khởi động. | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | **4 rủi ro** có số/owner trong `chi_so.md`: làm lại, xem lại, lương, lưu lượng. Loại `quoc_te`: CPS **22.515,16 đ**, thành công **27,33%**; `doi_tac` có điều khoản riêng (chi phí simulated). | Giả lập | PM trợ lý hoàn phí |

**Điều kiện cần kiểm tra:** trước **30/11/2026**, Giám đốc vận hành duyệt MDE 6 điểm và mẫu; Kỹ sư trưởng agent chứng minh chống trùng, ghi sổ trước thông báo, đủ event và rollback ≤30 phút; PM cấu hình tối đa 2 lần chạy. Trước **07/12/2026**, Trưởng nhóm CSKH kiểm số phút đo thật và kế hoạch hạ xem lại, chỉ hạ khi sửa+bỏ <15% và kiểm toán 100 ca/tuần không sai tiền/hoàn trùng. Mọi điều kiện đang chờ bằng chứng thực hiện.

Nguồn: [chi phí](bang_chi_phi.md) · [lỗi](bang_loi.md) · [chỉ số/event](chi_so.md) · [pilot](pilot_plan.yaml). Hồ sơ đã tổng hợp; hội đồng chưa ra quyết định và từng thành viên chưa xác nhận nộp LMS.

**Đề xuất: Go có điều kiện** cho kế hoạch pilot `noi_dia + hang_nang`, tối đa 2 lần chạy; thiếu điều kiện, mẫu hoặc dữ liệu trưởng thành thì **No-go mở rộng**.
