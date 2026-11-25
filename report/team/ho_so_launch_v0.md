# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: NhomTVA · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** [simulated] = 4.373.585 đ ÷ 978 việc thành công, gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ). Khoản lớn nhất: làm lại 51,8% [simulated], xem lại 40,7% [simulated]. Phạm vi pilot `noi_dia` + `hang_nang` cộng cố định 40 triệu đ/tháng: 3.414 + 1.185 = **4.599 đ** [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại gấp đôi: **+51,8%** → 6.787 đ · 2. Tỉ lệ xem lại gấp đôi: **+40,7%** → 6.292 đ · 3. Lương tăng 25%: **+23,1%** → 5.506 đ [simulated]. Giá token gấp đôi chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm (12.000 đ) | Cả hệ thống (cộng 222 ca không thành công × 12.000 đ): **5.865 đ/yêu cầu = 0,49×** [simulated]. Theo loại: noi_dia 0,22× · hang_nang 0,69× · doi_tac 0,85× · quoc_te **1,88×** [simulated] → loại quoc_te, doi_tac khỏi phạm vi | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | _Chờ Người 2 tính thử (CP5, `chi_so.md`)_ | Chưa | ... |
| 5 · Bảng lỗi và cách khắc phục | Hai người gắn nhãn độc lập, đồng thuận **20/20 = 100%** (Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn 4 · Ngầm 3 ca); đã có bảng khắc phục 5 ca đủ 5 loại (ca 9, 7, 18, 4, 17) có event/ngưỡng đo được | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | _Chờ CP4 (`pilot_plan.yaml`): cách chia, cỡ mẫu, 3 luật dừng_ | Chưa | ... |
| 7 · Rủi ro kinh tế | _Chờ Người 2 (E2 trong `chi_so.md`)_ | Chưa | ... |

**Đề xuất:** _chốt ở CP5 sau khi đủ mục 4–7_ (Go · Go có điều kiện · No-go, giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...

<!-- Nguồn số mục 1–3: tính độc lập từ hai file CSV để đối chiếu, phải khớp output `python lab13.py` của Người 1 (lệch ≤ 2%) trước khi đổi trạng thái. -->
