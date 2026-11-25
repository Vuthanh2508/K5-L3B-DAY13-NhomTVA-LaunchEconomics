# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: NhomTVA · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** [simulated] = 4.373.585 đ ÷ 978 việc thành công, gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ). Khoản lớn nhất: làm lại 51,8% [simulated], xem lại 40,7% [simulated]. Phạm vi pilot `noi_dia` + `hang_nang` cộng cố định 40 triệu đ/tháng: 3.414 + 1.185 = **4.599 đ** [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại gấp đôi: **+51,8%** → 6.787 đ · 2. Tỉ lệ xem lại gấp đôi: **+40,7%** → 6.292 đ · 3. Lương tăng 25%: **+23,1%** → 5.506 đ [simulated]. Giá token gấp đôi chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm (12.000 đ) | Cả hệ thống (cộng 222 ca không thành công × 12.000 đ): **5.865 đ/yêu cầu = 0,49×** [simulated]. Theo loại: noi_dia 0,22× · hang_nang 0,69× · doi_tac 0,85× · quoc_te **1,88×** [simulated] → loại quoc_te, doi_tac khỏi phạm vi | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (chưa có đối chứng): chính **82,83%** (994/1.200 đóng trong 24 giờ, không mở lại 7 ngày) · dùng: bỏ qua gợi ý **27,12%** (48/177) · an toàn: mở lại 7 ngày **4,25%** (51/1.200; 3,97% trong phạm vi pilot). 12 event đều có `trace_id`, mỗi chỉ số đã nối với event tính ra nó | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Hai người gắn nhãn độc lập, đồng thuận **20/20 = 100%** (Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn 4 · Ngầm 3 ca); đã có bảng khắc phục 5 ca đủ 5 loại (ca 9, 7, 18, 4, 17) có event/ngưỡng đo được | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo **nhân viên, 20 + 20**, bốc thăm phân tầng theo depot; chỉ `noi_dia` + `hang_nang`. Theo yêu cầu cần 1.251/nhóm, nhưng 20 cụm chỉ đạt tối đa 20 ÷ 0,02 = **1.000** → chấp nhận MDE **6 điểm** (859/nhóm, m ≥ 299 yc/người, DE 6,96; bước 0,50 chạy ≥ 8–10 ngày + 7 ngày theo dõi); **power chỉ 0,64** nếu tác động thật là 5 điểm. 3 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: **+51,8%** → 6.787 đ · Xem lại 100%: **11.743 đ = 0,98×** (12.415 đ = 1,03× với 15,3 phút làm lại) · Khối lượng còn một nửa: cố định **+2.370 đ/việc** [simulated]. Mỗi rủi ro có dấu hiệu theo dõi và người phụ trách | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang` (loại `quoc_te` 1,88× và `doi_tac` 0,85× [simulated]). Con số bất lợi đã nêu: xem lại 100% gần như không tiết kiệm (0,98–1,03×), và pilot chỉ đủ mẫu cho mức chênh 6 điểm.

| Điều kiện | Người phụ trách | Ngày kiểm tra |
| --- | --- | --- |
| Sửa khoá chống hoàn trùng (`idempotency_key`) và đối soát sổ cái mỗi giờ (ca 7, 20), ngưỡng 0 ca trước ngày bắt đầu | Kỹ sư trưởng agent | 2026-12-04 |
| Ký chấp nhận MDE 6 điểm, power 0,64 ở mức 5 điểm và kéo dài bước 0,50 tối thiểu 8–10 ngày để đủ m ≥ 299 đơn/người (đã chốt `pilot_plan.yaml`) | Giám đốc vận hành | 2026-12-04 |
| Bật đủ 12 event có `trace_id`; thay phút xem lại, làm lại [simulated] bằng phút đo thật từ `staff_review_decision`, `staff_rework_completed` | PM trợ lý hoàn phí | 2026-12-14 (sau tuần 1) |
| Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; mỗi lần xem lại ≤ 5,1 phút mới hoà vốn (B4) | Trưởng nhóm CSKH | 2026-12-28 (cuối bước 0,25) |

<!-- Nguồn số mục 1–3: output `cd src && python lab13.py`, Người 4 chạy lại trên máy riêng; khớp 100% với số tính độc lập từ hai file CSV. -->
