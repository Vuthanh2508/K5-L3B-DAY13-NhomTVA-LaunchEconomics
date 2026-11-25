# Team

## Thông tin nhóm

- Tên nhóm: NhomTVA
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-NhomTVA-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/Vuthanh2508/K5-L3B-DAY13-NhomTVA-LaunchEconomics · nhánh `main` · commit chốt: (điền khi push cuối)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Vũ Thành | 2A202603930 | vuthanhdz2508@gmail.com | Vuthanh2508 | Người viết code (lượt 1: CP1–CP2) |
|   2 | Trần Đức Trung | 2A202603938 | kientrungtd135@gmail.com | kientrungtd135 | Người kiểm số + người viết code (lượt 2: CP4) |
|   3 | Đỗ Việt Anh | 2A202603973 | dovietanh240405@gmail.com | vietahnn | Người gắn nhãn 1 (kiêm rà điều kiện "Xong khi") |
|   4 | Dương Minh Chiến | 2A202603921 | duongchien1472005@gmail.com | duongchien147 | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## TranDucTrung-2A202603938

### Phần việc phụ trách

- Người kiểm số và người viết code lượt 2: đối chiếu một số liệu CP1–CP2; hoàn thiện B3–B4, D1 và tỉ lệ mở lại 7 ngày; tính ba chỉ số E1 và viết E2.

### Đóng góp cụ thể

- Tự đối chiếu hoá đơn token và tool: (245.585 + 84.000) / 1.200 = 274,65 đ/yêu cầu, làm tròn 274,7 đ.
- Hoàn thiện B3–B4 trong `report/team/bang_chi_phi.md`; chi phí toàn hệ thống thấp nhất ở giới hạn 2 lần (6.901.220 đ), còn CPS thấp nhất ở giới hạn 1 lần (4.111 đ). B4: CPS 11.743 đ với giả định 9 phút làm lại; 12.415 đ theo dữ liệu simulated.
- Bổ sung D1 a–e và tỉ lệ mở lại vào `src/lab13.py`: cỡ mẫu 1.251/nhóm cho chênh 5 điểm; 859/nhóm và 299 yêu cầu/nhân viên cho chênh 6 điểm; tỉ lệ mở lại hiện tại 4,25% toàn mẫu.
- Điền ba chỉ số E1 và ba rủi ro kinh tế E2 vào `report/team/chi_so.md`; nêu rõ hai chỉ số đề xuất chưa tính được từ CSV hiện tại.

### Bằng chứng

- Commit `2e78b7d` (B3–B4), `78262c9` (D1), `dcaf3cf` (E1–E2); các file `report/team/bang_chi_phi.md`, `src/lab13.py`, `report/team/chi_so.md` và báo cáo cá nhân `report/team/2A202603938_TranDucTrung.md`.

## DuongMinhChien-2A202603921

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ: `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md`.

### Đóng góp cụ thể

- Điền hồ sơ launch v0 đủ bảy mục và chốt đề xuất Go có điều kiện (4 điều kiện, người phụ trách, ngày kiểm tra).
- Tính độc lập các số mục 1–4, 6, 7 từ hai file CSV để đối chiếu; chạy lại `python lab13.py` trên máy riêng (ba phép thử ĐẠT, số khớp hồ sơ).
- Gắn nhãn độc lập 20 ca lỗi (đồng thuận 20/20 với Người gắn nhãn 1); cùng làm bảng khắc phục 5 ca.
- Viết `group_report.md`; rà toàn bộ hồ sơ theo checklist nộp bài (nhãn simulated, người phụ trách là một vai trò, từ cấm).

### Bằng chứng

- Commit `9f51a19` và các commit sau trên `main`; file `report/team/ho_so_launch_v0.md`, cột "Nhãn người 2" trong `report/team/bang_loi.md`.

## VuThanh-2A202603930

### Phần việc phụ trách

- Người viết code (lượt 1: CP1–CP2): `src/lab13.py` (A1–B4), `report/team/bang_chi_phi.md` (A1–A4, B1–B2), danh sách event & kiểm tra chéo trong `report/team/chi_so.md`, hoàn thiện `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Tạo repo nhóm `K5-L3B-DAY13-NhomTVA-LaunchEconomics`, xử lý merge conflict và điều phối đồng bộ Git cho nhóm.
- Cài đặt các hàm A1 (`1,20 · 1,25 · 1,25`), `mo_hinh`, A3, A4 và độ nhạy B1–B4 trong `src/lab13.py`; điền A1–A4 và B1–B2 vào `bang_chi_phi.md`.
- Thiết kế 12 event có `request_id` + `trace_id` khớp `bang_loi.md` và 5 dòng kiểm tra chéo E1 trong `chi_so.md`.
- Hoàn thiện toàn bộ trường còn `?` và chỉnh 3 `stop_rules` trong `pilot_plan.yaml`; cập nhật mục 6 ở `ho_so_launch_v0.md`

### Bằng chứng

- Các commit `51236d5`, `52f2445`, `6cf712c`, `503a47a`, `159b1bd`, `d9f9251` trên `main`; file `src/lab13.py`, `report/team/chi_so.md`, `report/team/pilot_plan.yaml`, `report/team/2A202603930_VuThanh.md`.

## DoVietAnh-2A202603973

### Phần việc phụ trách

- Người gắn nhãn 1 (kiêm rà điều kiện "Xong khi"): đọc đề và đối chiếu điều kiện hoàn thành các checkpoint (CP1–CP5); gắn nhãn độc lập 20 ca lỗi (CP3) và lập bảng khắc phục 5 ca (`report/team/bang_loi.md`); trả lời 5 câu D2, đánh đổi và viết 3 luật dừng 4 vế trong `report/team/pilot_plan.yaml` (CP4); cập nhật mục 5 `report/team/ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Theo dõi điều kiện "Xong khi" xuyên suốt CP1–CP4: kiểm tra nhãn `simulated`, giới hạn độ dài câu trả lời (≤ 3 dòng có số), quy tắc không dùng từ cấm và người phụ trách là một vai trò cụ thể.
- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (cột "Nhãn người 1" trong `report/team/bang_loi.md`), đạt đồng thuận **20/20 = 100%** với Người gắn nhãn 2 (`Dương Minh Chiến`).
- Hoàn thiện bảng khắc phục 5 ca đại diện đủ 5 loại lỗi (Ca 9, 7, 18, 4, 17) với cách phát hiện có event/ngưỡng/tần suất đo được và vai trò phụ trách rõ ràng; cập nhật mục 5 trong `report/team/ho_so_launch_v0.md` sang trạng thái `Xong, có bằng chứng`.
- Soạn 5 câu trả lời D2 ("tách được tác động"), đánh đổi MDE 6 điểm (`n = 859/nhóm`, `m >= 299`, `DE = 6,96`, power còn `~0,64` nếu tác động thật 5 điểm), ngưỡng an toàn từ nền `mo_lai_trong_7_ngay` (`4,25%` toàn mẫu, `3,97%` phạm vi pilot), khối `identifiability` và 3 luật dừng đủ 4 vế (`NẾU – TRONG – THÌ – KHÔNG THÌ`) trong `report/team/pilot_plan.yaml`, đồng bộ tên event (`ticket_reopened`, `refund_ledger_write`, `agent_suggestion_shown`, `staff_review_decision`) với `report/team/chi_so.md`.

### Bằng chứng

- Các commit `70f2849`, `00a890c`, `29fd8b1`, `bbac621` trên `main`; file `report/team/bang_loi.md` (cột "Nhãn người 1" và bảng khắc phục 5 ca), `report/team/pilot_plan.yaml` (D2, `identifiability`, `stop_rules`), `report/team/ho_so_launch_v0.md` (mục 5) và báo cáo cá nhân `report/team/2A202603973_DoVietAnh.md`.
