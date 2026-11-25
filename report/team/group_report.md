# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: NhomTVA
- Lớp: L3B
- Repo: https://github.com/Vuthanh2508/K5-L3B-DAY13-NhomTVA-LaunchEconomics
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có chạy pilot hay không. Hồ sơ trả lời bốn câu: có đáng chạy, nhân viên có dùng, khi hỏng thì sao, pilot thiết kế thế nào. Toàn bộ dữ liệu là giả lập (1.200 yêu cầu, 1.624 lần chạy).

Nhóm dùng một mô hình chi phí duy nhất trong `src/lab13.py` và gọi lại nó cho từng loại yêu cầu và từng kịch bản độ nhạy. Hai người gắn nhãn lỗi độc lập rồi mới so. Cỡ mẫu được tính trước khi chọn cách chia pilot. Người giữ hồ sơ điền `ho_so_launch_v0.md` dần từ đầu buổi.

## 3. Giải pháp

Nhiệm vụ A ([bang_chi_phi.md](bang_chi_phi.md)): nhóm viết ba hàm A1 (qua ba phép thử 1,20 · 1,25 · 1,25) và hàm `mo_hinh` trong `src/lab13.py`. Tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm việc thành công. Hàm được gọi lại theo từng `loai` (A3), và chi phí cố định được cộng cho phạm vi pilot (A4).

Nhiệm vụ B ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại `mo_hinh` cho 9 kịch bản, một cặp, ba giới hạn chạy lại và kịch bản xem lại 100%.

Nhiệm vụ C ([bang_loi.md](bang_loi.md)): hai người gắn nhãn ngồi tách, gắn độc lập 20 ca trong 8 phút rồi mới so, sau đó chọn 5 ca (mỗi loại một ca) để làm bảng khắc phục.

Nhiệm vụ D ([pilot_plan.yaml](pilot_plan.yaml)): tính năm câu D1 trước, rồi mới chọn chia theo nhân viên 20 + 20 và ghi rõ đánh đổi.

Nhiệm vụ E ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): tính thử ba chỉ số, lập 12 event có `trace_id` và ba dòng rủi ro kinh tế; người giữ hồ sơ ghép A–D thành một trang.

## 4. Kết quả

Chi phí mỗi việc thành công là 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu; giờ nhân viên chiếm 92,5% tổng chi phí [simulated]. Tính cả hệ thống, chi phí bằng 0,49× so với nhân viên tự làm [simulated]. `quoc_te` (1,88×) và `doi_tac` (0,85×) [simulated] bị loại khỏi phạm vi.

Ba yếu tố nhạy nhất là làm lại +51,8%, xem lại +40,7% và lương +23,1% [simulated]. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống, 6.901.220 đ [simulated].

Bảng lỗi đạt đồng thuận 20/20 = 100%. Pilot chia theo nhân viên 20 + 20, chấp nhận MDE 6 điểm (859/nhóm); nếu tác động thật là 5 điểm thì power chỉ còn 0,64. Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%.

Đề xuất cuối là Go có điều kiện cho `noi_dia` + `hang_nang`, với 4 điều kiện có người phụ trách và ngày kiểm tra.

Kết quả duyệt chéo từ hội đồng: _(ghi sau buổi 17:25)_

## 5. Khó khăn và cách xử lý

Hồ sơ cần số từ code trong khi code chưa xong. Người giữ hồ sơ tính độc lập từ hai file CSV để điền nháp, rồi đối chiếu lại khi `lab13.py` hoàn thành; số khớp 100%.

Hai người gắn nhãn sửa cùng các dòng trong `bang_loi.md` nên bị conflict git. Nhóm gộp tay thành một bảng đủ hai cột, không sửa nhãn nào của hai bộ độc lập.

Với 40 nhân viên, nhóm không đủ mẫu để thấy mức chênh 5 điểm. Nhóm chọn chia theo nhân viên và ghi rõ đánh đổi; chia theo depot bị loại vì chỉ có 6 cụm.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Phút xem lại và làm lại là số giả lập, cần thay bằng phút đo thật từ event sau tuần 1 của pilot. Đợt chạy thử không có đối chứng nên chưa kết luận được tác động của trợ lý. Ở mức chênh 5 điểm, power chỉ 0,64, nên nếu tác động thật nhỏ thì pilot có thể không thấy được. Hai chỉ số tự đề xuất chưa tính được từ CSV hiện tại và cần bật event trước khi chạy pilot.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu statsmodels, `NormalIndPower`
- Đề bài, slide và hướng dẫn chi tiết Lab 13 trong `docs/`
