# Báo cáo cá nhân — ChuVanNhat-2A202603848

## 1. Thông tin thành viên

- Họ tên: Chu Văn Nhật
- MSSV: 2A202603848
- Email: chưa bổ sung.
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1

## 2. Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi ở Nhiệm vụ C (CP3) theo 5 loại lỗi của Google PAIR (Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống, Ngầm).
- Đối chiếu nhãn với Người gắn nhãn 2, tính tỉ lệ đồng thuận (mục tiêu >= 80%) và thống nhất quy tắc phân biệt cho các ca không trùng.
- Cùng Người gắn nhãn 2 chọn 5 ca lỗi đại diện đủ 5 loại để lập bảng khắc phục (có cách phát hiện đo được và vai trò phụ trách cụ thể).
- Theo dõi các điều kiện nghiệm thu ("Xong khi"), rà soát tuân thủ quy tắc hồ sơ (kiểm tra nhãn `simulated`, đảm bảo chỉ duyệt kế hoạch pilot thay vì chạy chính thức, kiểm tra dấu `?` trong `pilot_plan.yaml`).

## 3. Đóng góp cụ thể

- Hoàn thành bộ nhãn người 1 cho 20 ca lỗi trong `report/team/bang_loi.md`, đạt tỉ lệ đồng thuận 90% (18/20 ca) với Người 2.
- Phối hợp thống nhất quy tắc cho các ca không trùng và hoàn thiện bảng khắc phục 5 ca lỗi đại diện.
- Hoàn thành file `report/team/chi_so.md`: tính toán 3 chỉ số trong đợt chạy thử (82,83% chính, 27,12% dùng, 4,25% an toàn), đề xuất 2 chỉ số mới, xây dựng danh sách 8 event có `trace_id` cùng ánh xạ kiểm tra chéo, và tích hợp 3 rủi ro kinh tế có số liệu từ bảng độ nhạy.
- Rà soát các quy tắc liêm chính, nhãn `simulated`, đảm bảo chỉ duyệt kế hoạch pilot và tuân thủ checklist của nhóm.

## 4. Bằng chứng

- Cột "Nhãn người 1", quy tắc phân biệt và bảng khắc phục trong `report/team/bang_loi.md`.
- Bảng đặc tả chỉ số, danh sách 8 event có `trace_id` và bảng rủi ro kinh tế trong `report/team/chi_so.md`.
- Lịch sử commit trên repo nhóm.

## 5. Công cụ AI đã dùng

- Công cụ: Antigravity Assistant.
- Mục đích: Tìm hiểu và làm rõ định nghĩa 5 loại lỗi theo hướng dẫn Google PAIR (Errors + Graceful Failure), hỗ trợ rà soát quy tắc phân biệt cho các ca lỗi dễ nhầm lẫn.
- Cách tự kiểm tra kết quả: Đọc hiểu chi tiết ngữ cảnh của từng ca khiếu nại hoàn phí trong dữ liệu LogiX-VN, gắn nhãn độc lập hoàn toàn mà không trao đổi trước với Người gắn nhãn 2 để kiểm chứng tỷ lệ đồng thuận thực tế.

## 6. Tự đánh giá

- Hoàn thành đầy đủ trách nhiệm của Người gắn nhãn 1, phối hợp chặt chẽ với các thành viên trong nhóm, đảm bảo tính liêm chính học thuật và tuân thủ các quy định của buổi lab.

**Ghi chú tích hợp:** các con số 8 event và 3 rủi ro ở trên mô tả bản TV3 đã nộp. Bản cuối kết hợp đóng góp TV4 thành 14 event, 4 chỉ số đề xuất và 4 rủi ro; giữ bộ nhãn gốc của Nhật. Lượt rà bằng Codex không thay xác nhận cá nhân hoặc kết quả hội đồng.
