# Team · DAY13 · Phân công 4 người

## Thông tin nhóm

- Tên nhóm theo tên repo: EA1125.
- Lớp theo tên repo: L3B.
- Repo nhóm: `K5-L3B-DAY13-EA1125-LaunchEconomics`.
- URL: https://github.com/phamtuan2xx3-alt/K5-L3B-DAY13-EA1125-LaunchEconomics
- Nhánh nộp, commit chốt: main
- TV1 đã xác nhận: PHẠM QUANG TUẤN — MSSV 2A202603824.
- TV2 đã xác nhận: NGUYỄN THANH TÙNG — MSSV 2A202603807.
- TV3 đã xác nhận: CHU VĂN NHẬT — MSSV 2A202603848.
Tên và thông tin TV4 bổ sung sau. Các mục dưới đây là kế hoạch, chưa phải bằng chứng đã hoàn thành.

## Thành viên và trách nhiệm chính

| Mã | Họ tên | MSSV | Email | GitHub | Vai trò |
| --- | --- | --- | --- | --- | --- |
| TV1 | PHẠM QUANG TUẤN | 2A202603824 | Bổ sung sau | Bổ sung sau | Viết code trước giải lao; phụ trách kinh tế và kế hoạch pilot |
| TV2 | NGUYỄN THANH TÙNG | 2A202603807 | Bổ sung sau | Bổ sung sau | Kiểm số; viết code sau giải lao; kiểm tra bản tích hợp |
| TV3 | Chu Văn Nhật | 2A202603848 | Bổ sung sau | Bổ sung sau | Gắn nhãn độc lập 1; phụ trách bảng lỗi và đặc tả chỉ số |
| TV4 | Bổ sung sau | Bổ sung sau | Bổ sung sau | Bổ sung sau | Gắn nhãn độc lập 2; giữ hồ sơ, ghi duyệt chéo và tổng hợp báo cáo |

## Việc cụ thể và điều kiện bàn giao

### TV1 · PHẠM QUANG TUẤN · Code kinh tế A–B và kế hoạch pilot D

1. **CP1:** cài môi trường; viết ba hàm A1 và `mo_hinh` trong `src/lab13.py`; in bảng A2, A3 theo đủ 4 loại và A4 có chi phí cố định 40 triệu đồng/tháng ở 2 mức khối lượng.
2. **CP2:** viết 9 kịch bản B1, kịch bản cặp B2, bảng B3 giới hạn 1/2/3 lần và B4 xem lại 100% trong phạm vi `noi_dia` + `hang_nang`; bàn giao output cho TV2.
3. **Sau giải lao:** bàn giao quyền sửa `src/lab13.py` cho TV2; cùng kiểm lại B3/B4 trong lúc TV3 và TV4 gắn nhãn độc lập.
4. **CP4:** chủ trì điền `report/team/pilot_plan.yaml`, lấy D1 từ TV2; viết D2, phạm vi, rollout, đối chứng, luật dừng, rollback, ngày quyết định và `simulated_inputs`. TV3 góp ý an toàn, TV4 kiểm tra tính nhất quán với hồ sơ.
5. **CP5:** cung cấp cho TV3 ít nhất 2 rủi ro kinh tế có số từ bảng độ nhạy; cung cấp cho TV4 kết luận kinh tế và điều kiện đề xuất.
6. **Duyệt chéo:** giải thích tử số/mẫu số chi phí, phần việc chuyển nhân viên, chi phí cố định và B4; kiểm tra bằng chứng kinh tế của nhóm được chấm.

**Bàn giao:** A1 đạt đủ 1,20 · 1,25 · 1,25 trước khi tính tiếp; output A/B đủ bảng; YAML đọc được, không còn dấu hỏi ngoài chú thích; ít nhất 3 luật dừng an toàn/chi phí/sử dụng đủ NẾU–TRONG–THÌ–KHÔNG THÌ. Cách chia cụm có ít nhất 20 cụm mỗi nhóm hoặc nêu rõ đánh đổi.

### TV2 · Kiểm số, bảng chi phí và code D1/E1

1. **CP1:** đọc dữ liệu/công thức; tự tính tay ít nhất 1 con số để đối chiếu TV1. Điền A1–A4 trong `report/team/bang_chi_phi.md`, gồm A2 đủ 9 dòng, A3 đủ 4 loại và A4 đủ 2 mức khối lượng.
2. **CP2:** điền B1 đủ 9 dòng, B2 kịch bản cặp và xếp hạng 3 yếu tố, B3 chi phí cả hệ thống, B4 cả giả định làm lại 9 phút và độ nhạy theo phút trong dữ liệu; kiểm tra nhãn `simulated` và câu trả lời tối đa 3 dòng có số.
3. **Sau giải lao:** nhận quyền sửa `src/lab13.py`; cùng TV1 chốt B, rồi viết phép tính cho đủ 5 câu D1 và 3 chỉ số E1. Bảo đảm script in các bảng từ đầu đến cuối.
4. **CP4:** bàn giao số D1, hệ số thiết kế, cỡ mẫu hiệu dụng và đánh đổi cho TV1; cung cấp tỉ lệ mở lại hiện tại trước khi đặt luật an toàn.
5. **CP5:** bàn giao tử số/mẫu số của 3 chỉ số cho TV3; chạy bản tích hợp trên máy khác trong nhóm, lưu lệnh và output làm bằng chứng. Kiểm tra YAML bằng `yaml.safe_load`.
6. **Duyệt chéo:** kiểm số chi phí, cỡ mẫu và chỉ số trong hồ sơ nhóm được chấm; trả lời phần cỡ mẫu khi bảo vệ hồ sơ của nhóm.

**Bàn giao:** `bang_chi_phi.md` đầy đủ A–B; số tự tính lệch không quá 2% so với số đối chiếu; đủ D1 a–e; 3 chỉ số có phép tính; script chạy hết và YAML parse thành công. Nếu chưa chạy trên máy khác thì ghi rõ chưa đạt bước đó.

### TV3 · Chu Văn Nhật · Nhãn độc lập 1, bảng lỗi và chỉ số/event

1. **Trước CP3:** chuẩn bị khung `bang_loi.md`, định nghĩa 5 loại lỗi và dự thảo công thức chỉ số/event trong `chi_so.md`. Để phần nhãn tham khảo trong hướng dẫn đến sau bước gắn nhãn độc lập.
2. **CP3, 8 phút đầu:** tự gắn nhãn đủ 20 ca từ đề bài DOCX; không trao đổi hoặc xem nhãn TV4. Lưu bộ nhãn gốc trước khi so.
3. **CP3, sau khi so:** chủ trì nhập hai bộ nhãn vào `report/team/bang_loi.md`, tính đồng thuận, ghi nhãn thống nhất ở cột riêng và quy tắc cho ca bất đồng. Cùng TV4 chọn 5 ca đủ 5 loại, mỗi ca có cách phát hiện đo được, khắc phục và 1 vai trò phụ trách.
4. **CP4:** góp ý luật dừng an toàn từ bảng lỗi và số mở lại do TV2 tính; kiểm tra quyền dừng và cách phục vụ khách khi rollback.
5. **CP5:** hoàn thiện `report/team/chi_so.md`: 3 chỉ số tính thử từ TV2, thêm 1 chỉ số dùng và 1 chỉ số an toàn; ít nhất 6 event có `trace_id`; ánh xạ từng chỉ số với event; nhập ít nhất 2 rủi ro kinh tế từ TV1.
6. **Duyệt chéo:** kiểm bảng lỗi, event và an toàn của nhóm được chấm; trả lời phần lỗi và chỉ số khi bảo vệ hồ sơ.

**Bàn giao:** giữ nguyên 2 bộ nhãn độc lập; đồng thuận tối thiểu 16/20, nếu thấp hơn phải ghi định nghĩa đã viết lại trước khi đi tiếp; 5 ca khắc phục đủ 5 loại. `chi_so.md` có 5 chỉ số, ít nhất 6 event và 2 rủi ro có số.

### TV4 · Nhãn độc lập 2, hồ sơ launch và tổng hợp nộp

1. **Từ CP1:** giữ `TEAM.md` và điền dần `report/team/ho_so_launch_v0.md` từ số TV1/TV2 bàn giao; chuẩn bị khung báo cáo nhóm và checklist nộp.
2. **CP3, 8 phút đầu:** tự gắn nhãn đủ 20 ca, độc lập với TV3; lưu nhãn gốc. Sau đó so kết quả và cùng xây dựng bảng khắc phục; không sửa nhãn gốc sau khi so.
3. **CP4:** rà kế hoạch pilot với TV1: chỉ số, phạm vi, cỡ mẫu, đánh đổi, rollout, ngày quyết định và điều kiện dừng phải khớp hồ sơ launch.
4. **Trước 17:00:** chốt `ho_so_launch_v0.md` trong 1 trang đủ 7 mục; mỗi mục có số chính, trạng thái hợp lệ và người phụ trách là vai trò. Ghi điều kiện/ngày kiểm tra trước dòng cuối là đề xuất Go / Go có điều kiện / No-go.
5. **17:00–17:45:** ghi `report/team/phieu_cham.md` khi nhóm chấm nhóm khác; ghi điểm, lý do có số, quyết định, câu hỏi và câu trả lời thực tế. Điều phối phần trình bày hồ sơ của nhóm và ghi phản hồi nhận được.
6. **17:45–18:00:** tổng hợp `report/team/group_report.md` tối đa 2 trang; thu báo cáo cá nhân, cập nhật đóng góp thực tế và bằng chứng trong `TEAM.md`; tích hợp, commit, push và kiểm tra quyền truy cập repo. Nhắc từng người tự nộp cùng link trên LMS.

**Bàn giao:** hồ sơ 7 mục sẵn sàng lúc 17:00; phiếu chấm phản ánh buổi duyệt thực tế; đủ file theo `SUBMISSION.md`. Từng người tự xác nhận đã nộp LMS trước 23:59 GMT+7 ngày lab; hạn gia hạn theo thông báo của coach nếu có.

## Lịch phối hợp theo checkpoint

Các giờ dưới đây theo lịch mẫu buổi chiều; nếu lớp học giờ khác, giữ thứ tự và thời lượng theo coach. Giải lao 15:20–15:35.

| Mốc | TV1 | TV2 | TV3 | TV4 |
| --- | --- | --- | --- | --- | --- |
| 14:00–14:10 | Chuẩn bị môi trường và code | Kiểm dữ liệu, giá, công thức | Chuẩn bị khung lỗi/chỉ số | Điền thông tin nhóm, khung hồ sơ |
| 14:10–14:53 · CP1 | Viết và chạy A1–A4 | Tính tay, đối chiếu, điền bảng A | Chuẩn bị công thức và event E1 | Cập nhật hồ sơ từ bảng A |
| 14:53–15:20 · CP2 | Viết và chạy B1–B4 | Kiểm số và điền bảng B | Tiếp tục đặc tả event/an toàn | Chuẩn bị checklist và hồ sơ |
| 15:35–16:08 · CP3 | Bàn giao code; cùng TV2 chốt B | Nhận code; chốt B và chuẩn bị D1 | Gắn nhãn 1 độc lập, rồi tổng hợp C | Gắn nhãn 2 độc lập, rồi cùng chốt C |
| 16:08–16:36 · CP4 | Chủ trì YAML và D2 | Code D1, tính baseline an toàn/E1 | Góp ý luật an toàn, chuẩn bị E | Kiểm kế hoạch, cập nhật hồ sơ |
| 16:36–17:00 · CP5 | Rủi ro kinh tế, kiểm YAML | Chốt output và số chỉ số | Chốt `chi_so.md` | Chốt hồ sơ launch 7 mục |
| 17:00–17:45 | Đánh giá/bảo vệ kinh tế | Đánh giá/bảo vệ số liệu và mẫu | Đánh giá/bảo vệ lỗi và event | Ghi phiếu chấm, điều phối trình bày |
| 17:45–18:00 | Rà phạm vi/đề xuất; báo cáo cá nhân | Chạy bản tích hợp trên máy khác; báo cáo cá nhân | Rà lỗi/event; báo cáo cá nhân | Tổng hợp, báo cáo cá nhân, commit/push |

## Bàn giao file và tránh sửa chồng

| File | Người trực tiếp sửa | Người kiểm tra |
| --- | --- | --- |
| `src/lab13.py` | TV1 trước giải lao; TV2 sau giải lao | Người còn lại trong cặp TV1–TV2 |
| `report/team/bang_chi_phi.md` | TV2 | TV1 |
| `report/team/bang_loi.md` | TV3 sau khi có đủ 2 bộ nhãn | TV4 |
| `report/team/pilot_plan.yaml` | TV1 | TV2 kiểm mẫu/YAML; TV3 kiểm an toàn; TV4 kiểm nhất quán |
| `report/team/chi_so.md` | TV3 | TV2 kiểm số; TV1 kiểm rủi ro kinh tế |
| `report/team/ho_so_launch_v0.md` | TV4 | TV1–TV3 kiểm phần bằng chứng mình phụ trách |
| `report/team/phieu_cham.md` | TV4 ghi kết quả thảo luận thực tế | TV1–TV3 xác nhận |
| `report/team/group_report.md`, `TEAM.md` | TV4 tổng hợp đóng góp thực tế | Từng người xác nhận phần của mình |
| Báo cáo cá nhân | Mỗi người tự tạo và điền file riêng | TV4 kiểm đủ file và đúng tên |

Luồng bàn giao: **output A/B → bảng chi phí → phạm vi pilot và rủi ro; D1 + bảng lỗi + baseline an toàn → YAML; A–D + chỉ số → hồ sơ launch → duyệt chéo → đóng gói**. Gửi số và nội dung cho người giữ file để tích hợp; chỉ 1 người sửa `lab13.py` tại mỗi thời điểm.

## Checklist chung trước khi nộp

- [ ] TV2 xác nhận A1 đạt cả 3 phép thử; script chạy hết trong `src/` trên máy khác trong nhóm; số đối chiếu trong sai số 2%.
- [ ] TV1/TV2 xác nhận mọi số lấy từ phút giả lập, kể cả tổng chi phí và tỉ lệ dẫn xuất, có nhãn `simulated`; số do code nhóm tính hoặc tính tay có cách tính.
- [ ] TV3/TV4 giữ đủ 2 bộ nhãn độc lập, quy tắc bất đồng và 5 ca khắc phục có cách đo cùng vai trò phụ trách.
- [ ] TV1/TV2 xác nhận D1/D2 đủ, YAML parse được, không còn dấu hỏi ngoài chú thích và có ít nhất 3 luật dừng đủ 4 vế.
- [ ] TV3 xác nhận mỗi chỉ số tính được từ danh sách event có `trace_id`; mô tả số trong đợt chạy thử, không suy diễn tác động nhân quả khi chưa có đối chứng.
- [ ] TV4 xác nhận hồ sơ 1 trang đủ 7 mục, trạng thái đúng mẫu, dòng cuối là đề xuất; điều kiện có vai trò phụ trách và ngày kiểm tra.
- [ ] TV4 rà thuật ngữ theo quy tắc 5 của `README.md`, đúng tên và vị trí 6 file hồ sơ, có báo cáo nhóm và 4 báo cáo cá nhân.
- [ ] TV4 xác nhận giữ nguyên 2 CSV, `lab13_starter.py` và mẫu `MSSV_HoTen.md`; không đưa `.venv/`, `.env` hoặc secret vào commit.
- [ ] TV4 ghi nhánh/commit nộp, push và kiểm tra repo mở được cho người chấm; từng thành viên xác nhận đã nộp link LMS trước hạn.

## Báo cáo cá nhân và đóng góp thực tế

Mỗi người copy `report/team/MSSV_HoTen.md` thành `report/team/<MSSV>_<HoTenKhongDau>.md`, giữ nguyên file mẫu. Tự ghi phần đã làm, file/commit/output làm bằng chứng, công cụ AI và cách tự kiểm tra. Không dùng kế hoạch ở trên thay cho đóng góp thực tế.

| Thành viên | Phần đã làm | File/commit/output làm bằng chứng | Xác nhận nộp LMS |
| --- | --- | --- | --- |
| TV1 · PHẠM QUANG TUẤN · 2A202603824 | Triển khai với Codex: A–B, phép tính hỗ trợ D1, bản đề xuất pilot và rủi ro kinh tế; chờ nhóm kiểm độc lập | `src/lab13.py`; `report/team/TV1_ket_qua.txt`; `report/team/pilot_plan.yaml`; `report/team/TV1_ban_giao.md`; `tests/test_lab13.py`; báo cáo `2A202603824_PhamQuangTuan.md` | Chưa xác nhận |
| TV2 · NGUYỄN THANH TÙNG · 2A202603807 | Kiểm số độc lập (đối chiếu 0% lệch), hoàn thiện bảng chi phí A–B, chạy nghiệm thu 9/9 test trên máy TV2 | `report/team/bang_chi_phi.md`; `tests/test_lab13.py` (9 tests pass); báo cáo `report/team/2A202603807_NguyenThanhTung.md` | Chưa xác nhận |
| TV3 · Chu Văn Nhật · 2A202603848 | Gắn nhãn độc lập 20 ca lỗi ở Nhiệm vụ C, đồng thuận 90%, viết quy tắc phân biệt và bảng khắc phục 5 ca; hoàn thiện báo cáo cá nhân | `report/team/bang_loi.md`; báo cáo `2A202603848_ChuVanNhat.md` | Chưa xác nhận |
| TV4 | Bổ sung sau khi làm | Bổ sung sau | Chưa xác nhận |

## Nguồn yêu cầu

- [README.md](README.md), [CHECKPOINTS.md](CHECKPOINTS.md): vai trò, checkpoint, mốc 17:00 và đổi người viết code sau giải lao.
- [RULES.md](RULES.md): số liệu, hai bộ nhãn độc lập, dữ liệu gốc và khai báo AI.
- [RUBRIC.md](RUBRIC.md): 70 điểm A–E và 30 điểm hội đồng; điều kiện nghiệm thu.
- [SUBMISSION.md](SUBMISSION.md): file nộp, tên repo, quyền truy cập và hạn LMS.
- [src/README.md](src/README.md), [dữ liệu và công thức](docs/du_lieu_va_cong_thuc.md), [hướng dẫn chi tiết](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), [mẫu báo cáo](report/team/README.md): cách tính, cấu trúc đầu ra và trách nhiệm điền hồ sơ.
