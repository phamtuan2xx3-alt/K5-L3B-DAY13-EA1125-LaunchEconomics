# TV1 · Bàn giao kinh tế và kế hoạch pilot

**PHẠM QUANG TUẤN — 2A202603824 · EA1125 · L3B-H202.** Phần A–B, bản đề xuất D và đầu vào rủi ro kinh tế được triển khai với Codex. TV2 đã nộp kiểm số và báo cáo máy thứ hai; TV3/TV4 đã nộp nhãn và hồ sơ qua các nhánh. Bản tích hợp hiện có thêm E1 và dự toán pilot đúng giới hạn 2 lần. Chưa có kết quả duyệt chéo hoặc phê duyệt pilot.

## 1. Chạy lại và kiểm tra

Trong `src/`, sau khi cài `requirements.txt` vào `.venv`:

```powershell
$env:PYTHONUTF8 = '1'
.\.venv\Scripts\python.exe lab13.py --output ../report/team/TV1_ket_qua.txt
```

Từ root repo:

```powershell
.\src\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Output chung A–E giữ tên [TV1_ket_qua.txt](TV1_ket_qua.txt). Code: [lab13.py](../../src/lab13.py). Kiểm thử: [test_lab13.py](../../tests/test_lab13.py). Bản TV1 ban đầu đạt 9 kiểm thử; TV2 tự khai đã chạy 9/9 trên máy mình. Lượt tích hợp bổ sung kiểm thử E1/CLI/dự toán và ghi kết quả mới ở [nghiệm thu](nghiem_thu.md); không thay lời tự xác nhận của thành viên.

## 2. Số bàn giao TV2 điền bảng A–B

Toàn bộ CSV là dữ liệu giả lập của lab. Mọi số chi phí dùng hai cột phút `_simulated` dưới đây mang nhãn **simulated**. Số làm tròn chỉ để trình bày; code giữ số đầy đủ.

| Phần | Kết quả chính | Nhãn |
| --- | --- | --- |
| A1 | 1,20 · 1,25 · 1,25; cả 3 phép thử đạt | Công thức |
| A2 | 1.200 yêu cầu; 1.624 lần chạy; 978 việc thành công | CSV |
| A2 | Token 245.585,13 đ; tool 84.000 đ; trong đó chạy lại 93.804,49 đ đã nằm trong hai khoản trên | Trace giả lập |
| A2 | Xem lại 1.780.000 đ; làm lại 2.264.000 đ; tổng 4.373.585,13 đ | simulated |
| A2 | CPS 4.471,97 đ, gấp 16,282 lần hóa đơn token+tool/yêu cầu; làm lại chiếm 51,765% tổng | simulated |
| A3 | CPS noi_dia 2.695,64 đ; hang_nang 8.220,74 đ; quoc_te 22.515,16 đ; doi_tac 10.214,87 đ | simulated |
| A4 | Phạm vi noi_dia + hang_nang: 900 thành công/982 yêu cầu; CPS biến đổi 3.413,90 đ | simulated |
| A4 | 45.000 yêu cầu toàn công ty/tháng: 33.750 thành công trong phạm vi; CPS cộng cố định 4.599,09 đ; nửa lưu lượng: 5.784,27 đ | simulated |
| B1/B2 | 9 kịch bản trong output; xếp hạng làm lại, xem lại, lương; token x2 + xem lại x2: 6.543,12 đ, tăng 46,314% | simulated |
| B3 | Tổng hệ thống khi tối đa 1/2/3 lần: 7.449.780,64 / 6.901.220,23 / 7.037.585,13 đ | simulated |
| B3 | Giới hạn 2 lần rẻ nhất cho công ty; 1 lần có CPS thấp nhất | simulated |
| B4 | Xem lại 100% trong phạm vi: 948 ca xem, 48 ca làm lại; CPS 11.742,79 đ với 9 phút làm lại/ca | simulated |
| B4 | Dùng trung bình 1.132/74=15,2973 phút làm lại/ca: CPS 12.414,50 đ; ngưỡng hòa vốn xem lại 4,803 phút | simulated |

**Cách giải thích A2:** tử số tính tiền mọi lần chạy, kể cả lỗi; mẫu số chỉ có 978 việc thành công. Khoản chạy lại là phần nằm trong token+tool, không cộng lần nữa.

**Cách so với nhân viên:** theo quy ước B3, cộng thêm 12.000 đ cho cả 222 yêu cầu không thành công ở giới hạn 3 lần; chi phí hệ thống là 5.864,65 đ/yêu cầu (simulated), chưa có cố định. CPS 4.471,97 đ dùng mẫu số khác, không thay cho chi phí hệ thống/yêu cầu.

**Lưu ý A4:** 45.000 là tổng lưu lượng công ty nên số thành công trong phạm vi là `45.000 × 900/1.200`, không phải `45.000 × 900/982`. CPS cộng cố định là chỉ số mỗi việc thành công, chưa cộng nhân viên làm thay.

**Lưu ý B4:** code dùng trung bình phút đầy đủ, không làm tròn 15,2973 thành 15,3 trước khi tính. Khác biệt nhỏ so với số làm tròn trong hướng dẫn nằm trong dung sai 2%.

## 3. Bàn giao kế hoạch pilot D

[pilot_plan.yaml](pilot_plan.yaml) đã điền đủ trường D1, D2, rollout, 4 luật dừng và rollback; trạng thái là bản đề xuất chờ nhóm rà soát.

- MDE 5 điểm cần 1.251 yêu cầu độc lập/nhóm; 20 nhân viên/nhóm có trần hiệu dụng dưới 1.000 nên không đủ.
- Đề xuất ngẫu nhiên 20+20 nhân viên, MDE 6 điểm, 299 yêu cầu/người: 5.980 thô/nhóm, DE 6,96, hiệu dụng 859,195. Power ở hiệu ứng thật 5 điểm là 0,6418.
- Baseline mở lại 51/1.200=4,25%; trong phạm vi 39/982=3,9715%. Luật dừng dùng chênh +2 điểm với đối chứng hoặc vượt 6%, cùng cửa sổ và mẫu tối thiểu đã ghi.
- Rollout dự kiến 4→10→20 nhân viên. Bước cuối kéo dài 2 tuần vì một tuần chỉ ước khoảng 4.296 yêu cầu/nhóm, chưa đủ 5.980; thiếu 299 ca ở bất kỳ cụm nào thì chưa đủ điều kiện phân tích theo thiết kế.
- Lịch tích hợp dự kiến bắt đầu 30/11/2026, dành 2 tuần/bước để đủ cửa sổ an toàn; kết thúc thu mẫu 10/01/2027. Tính 24 giờ đóng cộng 7 ngày theo dõi, khóa sau 23:59 ngày 18/01/2027, quyết định 20/01/2027 (GMT+7). Giữ đúng 299 ca hợp lệ đầu tiên/nhân viên; ca không đóng vẫn nằm trong mẫu số và tính thất bại. Nếu thiếu mẫu hoặc trưởng thành thì No-go mở rộng. Đây là lịch đề xuất, chưa phê duyệt.

TV2 kiểm độc lập D1 và baseline; TV3 kiểm luật an toàn sau khi gắn nhãn thực tế; TV4 kiểm lịch, phạm vi và đề xuất cuối khớp hồ sơ launch.

## 4. Rủi ro kinh tế bàn giao TV3

Các ngưỡng theo dõi/hành động là đề xuất cho kế hoạch; tác động chi phí lấy từ output code. B1 bên dưới tính trên toàn mẫu 1.200 yêu cầu, B4 tính trong phạm vi pilot.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi đề xuất | Hành động đề xuất | Vai trò phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại gấp đôi | CPS toàn mẫu từ 4.471,97 lên 6.786,90 đ, +51,765% (simulated) | Tỷ lệ làm lại theo tuần trong phạm vi >7%; mẫu hiện tại 48/982=4,89% | Rà 20 trace làm lại, cập nhật chi phí theo phút đo thật; cân nhắc thu hẹp về noi_dia | PM trợ lý hoàn phí |
| Tỷ lệ xem lại gấp đôi | CPS toàn mẫu lên 6.292,01 đ, +40,699% (simulated) | Tỷ lệ xem lại vẫn >50% cuối bước 0.25 | Thử giảm theo bậc chỉ khi kiểm toán và tỷ lệ sửa+bỏ đạt điều kiện YAML | Trưởng nhóm CSKH |
| Xem lại 100% kéo dài | CPS phạm vi 11.742,79–12.414,50 đ, tương đương 0,979–1,035 lần baseline 12.000 đ (simulated) | Phút xem lại trung bình >4,803 khi làm lại khoảng 15,2973 phút/ca | Giữ quyết định mở rộng ở trạng thái chờ; đo phút thực tế và thiết kế lại thao tác xem lại | Trưởng nhóm CSKH |
| Lưu lượng giảm một nửa | Cố định/việc tăng từ 1.185,19 lên 2.370,37 đ; CPS có cố định tăng 4.599,09→5.784,27 đ (simulated) | Số thành công/tháng <50% giả định 33.750 | Tính lại phân bổ theo lưu lượng thực, rà cam kết chi phí trước khi tăng phạm vi | PM trợ lý hoàn phí |

## 5. Kết luận và việc cần nhóm xác nhận

Đề xuất kinh tế để TV4 xem xét là **Go có điều kiện cho kế hoạch pilot noi_dia + hang_nang**. quoc_te chỉ thành công 27,33%, CPS 1,876 lần baseline (simulated), tỷ lệ ok ở lần 3 chỉ 2,151%; doi_tac có điều khoản riêng nên để ngoài phạm vi.

Điều kiện trước khi khởi động: Giám đốc vận hành duyệt đánh đổi MDE 6 điểm; Kỹ sư trưởng agent chứng minh chống hoàn trùng, sổ cái và rollback; bật event có `trace_id`; Trưởng nhóm CSKH có kế hoạch đo phút và giảm xem lại an toàn. Mốc kiểm tra đề xuất trước 30/11/2026; đo lại chi phí sau tuần 1 trước 07/12/2026.

Đã nhận hồ sơ TV2/TV3/TV4 và tích hợp, giữ nguồn đóng góp theo Git. Phần dự toán cuối [bảng chi phí](bang_chi_phi.md) tính riêng phạm vi pilot tối đa 2 lần: hệ thống/yêu cầu toàn công ty có cố định 6.385,88 đ ở 45.000 ca/tháng, 7.274,77 đ ở nửa lưu lượng (simulated); không dùng CPS gốc 3 lần thay chỉ số này.

Chưa xác nhận kết quả hội đồng, phê duyệt điều kiện pilot, cá nhân Tuấn tự kiểm và nộp LMS. Không dùng kiểm thử code làm bằng chứng các bước này đã hoàn thành.

Nguồn: [dữ liệu/công thức](../../docs/du_lieu_va_cong_thuc.md), [hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), [checkpoints](../../CHECKPOINTS.md), [rubric](../../RUBRIC.md).
