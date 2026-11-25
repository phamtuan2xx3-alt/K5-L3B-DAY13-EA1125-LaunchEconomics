# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng [lab13.py](../../src/lab13.py), đối chiếu [output](TV1_ket_qua.txt). Hai CSV đều giả lập của lab. Mọi chi phí, tỷ trọng chi phí và tỷ lệ so baseline có dùng phút `_simulated` trong các bảng/giải thích dưới đây đều là **simulated**; số lượng và tỷ lệ kết quả lấy trực tiếp CSV. A2–A4/B4 dùng mẫu gốc tối đa 3 lần; B1/B3 ghi rõ từng giới hạn; dự toán pilot 2 lần nằm cuối file.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại; không cộng lại dòng chạy thứ 2/3 | simulated |
| Số việc thành công | 978 | `ket_qua` == 'thanh_cong' | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | tổng chi phí ÷ số việc thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (token + tool) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Chi phí mỗi việc thành công (4.472 đ [simulated]) gấp 16,3 lần so với hoá đơn token và tool chia cho số yêu cầu (274,7 đ).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? Khoản làm lại chiếm tỉ trọng lớn nhất với 51,8% (2.264.000 đ [simulated]), tiếp theo là xem lại 40,7% (1.780.000 đ [simulated]); tổng giờ nhân viên chiếm 92,5% chi phí.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? Loại quoc_te không đáng để trợ lý xử lý vì chi phí 22.515 đ [simulated] (1,88× so với 12.000 đ) và tỉ lệ thành công chỉ 27,3%. Chạy lại tới 3 lần không giúp vì tỉ lệ thành công giảm sâu qua từng lần chạy (30% ở lần 1, 11,4% ở lần 2, 2,2% ở lần 3), chỉ tốn thêm tiền.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Chi phí cố định có đổi kết luận không? CPS có cố định vẫn dưới 12.000 đ ở 45.000 và 22.500 yêu cầu/tháng (4.599 và 5.784 đ, simulated). Đây là CPS trợ lý, chưa tính người làm thay; muốn kết luận cho công ty phải dùng chi phí hệ thống/yêu cầu như dự toán cuối file. Số thành công/tháng là `lưu lượng toàn công ty × 900/1.200`, không dùng mẫu số 982.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ [simulated] (+46,3%), đúng bằng tổng hai tác động riêng (+5,6% và +40,7%) do mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%). (Giá token ít nhạy nhất: +5,6%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | 4.111 đ [simulated] |
| 2 lần | 4.093.220 đ [simulated] | 234 | 6.901.220 đ [simulated] | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ [simulated]), không trùng với giới hạn cho CPS trợ lý thấp nhất (1 lần: 4.111 đ [simulated]). Giới hạn 1 lần đẩy thêm 85 việc sang nhân viên thủ công (319 vs 234 ca), làm tăng chi phí toàn hệ thống thêm 548.561 đ.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: 948 ca xem lại ×5 phút và 48 ca làm lại ×9 phút cho CPS 11.742,79 đ (0,979×, simulated). Thay 9 bằng trung bình **simulated** `1.132/74 = 15,2973` phút/ca cho CPS **12.414,50 đ** (1,035×, simulated); đây chưa phải phút đo thật.
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% triệt tiêu lợi ích kinh tế vì chi phí xem lại chiếm 90% tổng chi. Pilot cần học được tỉ lệ xem lại an toàn có thể hạ xuống bao nhiêu % và thời gian xem lại có rút ngắn được dưới 4,8–5,1 phút hay không để giữ mức sinh lời.

## Dự toán cho phạm vi pilot và giới hạn 2 lần

Đề xuất dùng `noi_dia + hang_nang`, tối đa 2 lần. Quy ước chi phí làm thay theo B3, cơ cấu mẫu giữ nguyên khi ngoại suy; toàn bộ số chi phí dưới đây là **simulated**.

| Khoản | Cách tính | Giá trị |
| --- | --- | ---: |
| Số yêu cầu trong phạm vi / thành công / phải làm thay | `mo_hinh(..., max_lan_chay=2)` | 982 / 892 / 90 |
| Số yêu cầu ngoài phạm vi làm thủ công | 1.200−982 | 218 |
| Chi phí trợ lý trong phạm vi | Token/tool mọi lần ≤2 + phút xem/làm lại theo quy ước lab | 2.900.391,39 đ |
| Chi phí cả hệ thống trong phạm vi | 2.900.391,39 +90×12.000 | 3.980.391,39 đ |
| Chi phí cả công ty trên mẫu | 3.980.391,39 +218×12.000 | 6.596.391,39 đ |
| Chi phí hệ thống/yêu cầu toàn công ty, có cố định ở 45.000 ca/tháng | 6.596.391,39/1.200 +40.000.000/45.000 | **6.385,88 đ** |
| Cùng chỉ số ở 22.500 ca/tháng | 6.596.391,39/1.200 +40.000.000/22.500 | **7.274,77 đ** |

Hai dự toán cuối đều dưới baseline 12.000 đ/yêu cầu (simulated), nhưng phụ thuộc phút giả lập và chưa chứng minh hiệu quả thật. Đo phút thật, tính lại cùng mẫu số và giữ luật dừng trước khi đề xuất mở rộng.
