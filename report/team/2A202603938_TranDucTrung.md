# Báo cáo cá nhân — Trần Đức Trung (2A202603938)

## 1. Thông tin thành viên

- Họ tên: Trần Đức Trung
- MSSV: 2A202603938
- Email: kientrungtd135@gmail.com
- Vai trong nhóm: Người kiểm số + người viết code (lượt 2: CP4)

## 2. Phần việc phụ trách

- CP1–CP2: Tính tay đối chiếu ít nhất một con số và tham gia hoàn thiện bảng chi phí A–B.
- CP3: Hoàn thiện B3, B4 trong `report/team/bang_chi_phi.md`.
- CP4: Viết phần tính cỡ mẫu D1 (a–e) và tính tỉ lệ mở lại 7 ngày trong `src/lab13.py`.
- CP5: Tính thử ba chỉ số E1 và viết bảng rủi ro kinh tế E2 trong `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

- Đối chiếu tay hoá đơn token và tool: (245.585 + 84.000) / 1.200 = 274,65 đ/yêu cầu, làm tròn 274,7 đ.
- Hoàn thiện B3: giới hạn 2 lần có chi phí toàn hệ thống thấp nhất, 6.901.220 đ; giới hạn 1 lần có CPS thấp nhất, 4.111 đ.
- Hoàn thiện B4: xem lại 100% có CPS 11.743 đ ở giả định làm lại 9 phút; theo thời lượng làm lại trung bình trong dữ liệu, CPS là 12.415 đ (simulated).
- Bổ sung D1 a–e vào `src/lab13.py`: cỡ mẫu 1.251 yêu cầu/nhóm cho mức chênh 5 điểm; với 20 nhân viên/nhóm, mức chênh 6 điểm cần 859 yêu cầu/nhóm và 299 yêu cầu/nhân viên.
- Tính tỉ lệ mở lại 7 ngày: 51/1.200 = 4,25% toàn mẫu; 39/982 = 3,97% trong phạm vi `noi_dia` và `hang_nang`.
- Hoàn thiện E1 với ba chỉ số tính thử (82,83%, 27,12%, 4,25%) và đề xuất thêm một chỉ số dùng, một chỉ số an toàn; ghi rõ hai chỉ số đề xuất chưa tính được từ CSV hiện tại.
- Hoàn thiện E2 với ba rủi ro kinh tế, tác động định lượng, dấu hiệu theo dõi, hành động và vai trò phụ trách.

## 4. Bằng chứng

- `report/team/bang_chi_phi.md`: bảng B3, B4 và phép tính đối chiếu CP1–CP2.
- `src/lab13.py`: phần tính cỡ mẫu D1 và tỉ lệ mở lại 7 ngày.
- `report/team/chi_so.md`: các chỉ số E1 và bảng rủi ro E2.
- Commit: `2e78b7d` (B3/B4), `78262c9` (D1), `dcaf3cf` (E1/E2).

## 5. Công cụ AI đã dùng

- Kiểm tra bằng cách chạy `lab13.py`, xác nhận ba phép thử A1 đạt và đối chiếu các kết quả D1 với công thức cỡ mẫu; tự tính tay hoá đơn token/tool để kiểm chứng con số 274,7 đ/yêu cầu.

## 6. Tự đánh giá

- Hoàn thành các phần được phân công và có đối chiếu số liệu với dữ liệu, công thức và kết quả chạy chương trình.
