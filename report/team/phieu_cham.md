# Phiếu chấm hội đồng Gate 2a

**Trạng thái: Đã đánh giá hồ sơ repo và ghi nhận câu trả lời của đội trình do Phạm Quang Tuấn chuyển lại; chờ xác nhận điểm/quyết định của hội đồng EA1125.** Câu trả lời được ghi riêng với hồ sơ commit gốc, không suy ra nhóm được chấm đã cập nhật YAML.

- Nhóm chấm: **EA1125 · L3B-H202**.
- Người phụ trách ghi theo phân công: **Nguyễn Trọng Truyền — 2A202603868 — TV4**.
- Người cùng kiểm theo phân công: Phạm Quang Tuấn (kinh tế), Nguyễn Thanh Tùng (số liệu/cỡ mẫu), Chu Văn Nhật (lỗi/chỉ số).
- Nhóm được chấm: **TenNhomLab13 · L3B**; repo [K5-L3B-DAY13-TenNhomLab13-LaunchEconomics](https://github.com/sontpm/K5-L3B-DAY13-TenNhomLab13-LaunchEconomics).
- Bản được chấm: nhánh `main`, commit [`217ec78`](https://github.com/sontpm/K5-L3B-DAY13-TenNhomLab13-LaunchEconomics/commit/217ec78c7e0f42a584c7f2d543f04b12880f3343); ngày kiểm tra hồ sơ và nhận nội dung trả lời **25/11/2026 (GMT+7)**. Giờ trao đổi chưa được cung cấp.
- Chỉ chấm **C6, C7, C8**, mỗi tiêu chí nhận **0, 5 hoặc 10 điểm**, tổng **30 điểm**, theo [RUBRIC.md](../../RUBRIC.md). Không gộp 70 điểm C1–C5 của trợ giảng vào phiếu này.
- Hỗ trợ rà soát: Codex đối chiếu hồ sơ và chạy `src/lab13.py` của nhóm được chấm; code chạy hết, ba phép thử A1 đạt và YAML đọc được. Sau khi nhận câu trả lời, đã kiểm lại phép tính lưu lượng và số ngày; điểm cần được hội đồng EA1125 xác nhận.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm theo hồ sơ | Lý do và bằng chứng |
| --- | --- | --- | --- | --- | --- |
| C6 — Đề xuất khớp bằng chứng | Mâu thuẫn số của nhóm | Khớp nhưng bỏ qua số bất lợi | Khớp, nêu số bất lợi và xử lý | **10** | [Hồ sơ launch][launch] đề xuất Go có điều kiện, nêu CPS 4.472 đ/việc, bất lợi xem lại 100% là 11.743–12.415 đ, bằng 0,98–1,03× nhân viên tự làm (simulated); thừa nhận power chỉ 0,64 nếu tác động thật 5 điểm. Có điều kiện sửa chống hoàn trùng, chấp nhận MDE 6 điểm và đo phút thật. |
| C7 — Số giả lập và phạm vi | Không nhãn, phạm vi mọi yêu cầu | Có nhãn hoặc thu hẹp phạm vi | Đủ nhãn và thu hẹp có lý do bằng số | **10** | [Bảng chi phí][cost] và [hồ sơ launch][launch] gắn nhãn simulated cho số kinh tế; chọn noi_dia và hang_nang có CPS 2.696 đ và 8.221 đ (simulated), loại quoc_te có CPS 22.515 đ = 1,88× (simulated), tỉ lệ thành công 27,3%; loại doi_tac có điều khoản riêng. |
| C8 — Pilot ra được quyết định | Không đối chứng hoặc thiếu mẫu | Đủ mẫu, luật dừng chung chung | Tách tác động, đủ mẫu, ngưỡng/thời hạn/quyền dừng rõ | **5** | [Pilot plan][pilot] có đối chứng đồng thời, ngẫu nhiên theo nhân viên, 20 cụm/nhóm; 299 yêu cầu/người cho 5.980 yêu cầu thô/nhóm, DE 6,96, n hiệu dụng khoảng 859,2, đủ mục tiêu 859 ở MDE 6 điểm. Câu trả lời bổ sung đã nêu 10 ngày thu mẫu ở bước 0.50 và phương án lùi lịch. Vẫn cần xác nhận đủ 299 ca cho từng nhân viên và thời điểm kết thúc theo dõi; luật chi phí/sử dụng thiếu vai trò thực thi, điều kiện dừng hoàn trùng còn mơ hồ. |
| **Tổng /30** | | | | **25/30** | Sau khi ghi nhận câu trả lời: 10 + 10 + 5; chờ hội đồng EA1125 xác nhận. |

**Đề xuất quyết định để hội đồng chốt:** **Go có điều kiện.**

**Lý do có số:** Phạm vi noi_dia + hang_nang có cơ sở kinh tế, nhưng xem lại 100% làm chi phí lên 0,98–1,03× mức 12.000 đ (simulated), nên chưa bảo đảm tiết kiệm. Cỡ mẫu tính đúng cho MDE 6 điểm; câu trả lời đã giải thích tốc độ thu mẫu và lịch dự kiến. Cần đưa lịch vào kế hoạch, kiểm đủ mẫu thực tế và cửa sổ theo dõi, cùng luật dừng rõ trước khi khởi động pilot.

**Điều kiện cần nhóm được chấm hoàn thiện:**

1. Tích hợp lịch đã giải trình vào YAML. Chỉ chốt mẫu khi từng nhân viên trong 20 người/nhóm có ít nhất 299 yêu cầu hợp lệ; lưu lượng bình quân không bảo đảm mỗi người đều đạt. Xác định 7 ngày được tính từ lúc nhận yêu cầu hay lúc đóng ticket; nếu từ lúc đóng, các ca nhận cuối 28/12 có thể đóng 29/12 và phải theo dõi sang 05/01, nên chưa thể khóa dữ liệu 04/01. Chốt giờ khóa/ngày quyết định sau khi ca cuối đủ thời gian theo dõi; thiếu mẫu hoặc chưa trưởng thành thì lùi lịch, không chỉ lùi khi sửa lỗi chậm.
2. Chỉ định vai trò thực thi luật dừng chi phí và sử dụng; tách hoàn trùng thành điều kiện dừng ngay khi xác nhận 1 ca, thống nhất với [bảng lỗi][errors]. Làm rõ vế KHÔNG THÌ và điều kiện cho phép tăng rollout.
3. Trong [đặc tả chỉ số][metrics], dùng thời gian xem lại trung bình để đối chiếu hòa vốn: 5,1 phút với làm lại 9 phút hoặc 4,8 phút với thời lượng làm lại trong dữ liệu (simulated). Tách tỷ lệ hoàn trùng toàn hệ thống và tỷ lệ sai tiền trong mẫu kiểm toán để tránh sai mẫu số, đếm trùng.

**Một câu hỏi cho đội trình:** Với rollout 4 → 10 → 20 nhân viên dùng trợ lý, nhóm bố trí lịch thế nào để thu đủ 5.980 yêu cầu mỗi nhóm (299 yêu cầu/người, 20 người/nhóm) và theo dõi đủ 7 ngày trước ngày quyết định 05/01/2027?

**Câu trả lời của đội trình — nội dung do Phạm Quang Tuấn chuyển lại:**

> Tốc độ thu mẫu ở bước 0.50: Toàn công ty có 1.500 yêu cầu/ngày cho 40 nhân viên; phạm vi noi_dia + hang_nang chiếm 982/1.200 = 81,8%, tức khoảng 1.228 yêu cầu/ngày (614 yêu cầu/ngày/nhóm ở bước 0.50, hay ~30,7 yêu cầu/nhân viên/ngày). Để đạt m ≥ 299 yêu cầu/nhân viên (5.980 yêu cầu/nhóm), bước 0.50 cần 10 ngày thu mẫu (299 / 30,7 ≈ 9,7 ngày).
>
> Lịch bố trí cụ thể (31 ngày chạy + 9 ngày chuẩn bị trước 05/01/2027):
>
> 26/11 – 04/12/2026: Hoàn tất điều kiện tiên quyết (sửa khoá chống trùng ca 7, 20 và bật đủ event trace_id).
>
> Tuần 1 (05/12 – 11/12, 7 ngày): Rollout 0.10 (4 NV trợ lý) — chỉ theo dõi an toàn & kiểm tra log, chưa tính vào mẫu chính.
>
> Tuần 2 (12/12 – 18/12, 7 ngày): Rollout 0.25 (10 NV trợ lý) — kiểm tra an toàn & rà tỉ lệ xem lại.
>
> 19/12 – 28/12 (10 ngày): Rollout 0.50 (20 NV trợ lý vs 20 NV đối chứng) — thu đủ ≥ 5.980 yêu cầu/nhóm cho chỉ số chính.
>
> 29/12/2026 – 04/01/2027 (7 ngày): Khoá tập mẫu đánh giá để chờ đủ cửa sổ 7 ngày (mo_lai_trong_7_ngay) cho các ca cuối cùng, rồi chốt quyết định vào 05/01/2027.
>
> Phương án dự phòng: Nếu việc sửa lỗi ca 7, 20 kéo dài quá 04/12/2026, nhóm không cắt ngắn cửa sổ 7 ngày mà sẽ dời decision_date lùi tương ứng (giữ nguyên tối thiểu 14 ngày ramp-up + 10 ngày thu mẫu + 7 ngày theo dõi = 31 ngày).

**Nhận xét sau câu trả lời:** Đã giải trình giai đoạn lấy mẫu chính và phương án giữ nguyên thời gian theo dõi khi điều kiện tiên quyết chậm. Tính lại từ tỷ trọng chưa làm tròn cho 1.227,5 ca/ngày toàn công ty trong phạm vi, 613,75 ca/ngày/nhóm và 30,6875 ca/người/ngày; 299 / 30,6875 ≈ 9,74 ngày, làm tròn lên 10 ngày là đúng. Các khoảng lịch cũng đúng số ngày đã nêu: 9 ngày chuẩn bị và 31 ngày pilot. Đây là dự toán theo giả định lưu lượng/phân bổ ổn định; chưa chứng minh đã đủ mẫu hoặc đã theo dõi thực tế. Giữ C8 ở 5/10 do các điểm về luật dừng và điều kiện chốt dữ liệu vẫn chưa được giải quyết đầy đủ.

**Việc còn chờ:** Hội đồng EA1125 xác nhận điểm/quyết định và giờ trao đổi; nhóm được chấm làm rõ các điều kiện còn lại. Nếu bổ sung hồ sơ thì ghi commit mới và xem lại C8. Điểm 25/30 này là EA1125 chấm TenNhomLab13; điểm mà EA1125 nhận từ nhóm khác vẫn chưa được cung cấp, ghi riêng trong [báo cáo nhóm](group_report.md).

[launch]: https://github.com/sontpm/K5-L3B-DAY13-TenNhomLab13-LaunchEconomics/blob/217ec78c7e0f42a584c7f2d543f04b12880f3343/report/team/ho_so_launch_v0.md
[cost]: https://github.com/sontpm/K5-L3B-DAY13-TenNhomLab13-LaunchEconomics/blob/217ec78c7e0f42a584c7f2d543f04b12880f3343/report/team/bang_chi_phi.md
[pilot]: https://github.com/sontpm/K5-L3B-DAY13-TenNhomLab13-LaunchEconomics/blob/217ec78c7e0f42a584c7f2d543f04b12880f3343/report/team/pilot_plan.yaml
[metrics]: https://github.com/sontpm/K5-L3B-DAY13-TenNhomLab13-LaunchEconomics/blob/217ec78c7e0f42a584c7f2d543f04b12880f3343/report/team/chi_so.md
[errors]: https://github.com/sontpm/K5-L3B-DAY13-TenNhomLab13-LaunchEconomics/blob/217ec78c7e0f42a584c7f2d543f04b12880f3343/report/team/bang_loi.md
