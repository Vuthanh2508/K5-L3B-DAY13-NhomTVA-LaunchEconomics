# Báo cáo cá nhân: DuongMinhChien-2A202603921

## 1. Thông tin thành viên

- Họ tên: Dương Minh Chiến
- MSSV: 2A202603921
- Email: duongchien1472005@gmail.com
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

Tôi giữ hồ sơ `report/team/ho_so_launch_v0.md`: điền dần từ đầu buổi cho đủ bảy mục rồi chốt đề xuất cuối. Ở CP3, tôi gắn nhãn độc lập 20 ca lỗi (cột "Nhãn người 2" trong `report/team/bang_loi.md`) và cùng Người gắn nhãn 1 làm bảng khắc phục 5 ca. Tôi cũng phụ trách `report/team/group_report.md` và `TEAM.md`.

## 3. Đóng góp cụ thể

Trong CP1–CP2, tôi điền mục 1–3 của hồ sơ. Chi phí mỗi việc thành công là 4.472 đ [simulated], gấp 16,3 lần hoá đơn token; tính cả hệ thống thì bằng 0,49× so với 12.000 đ [simulated]. Ba yếu tố nhạy nhất là làm lại +51,8%, xem lại +40,7% và lương +23,1% [simulated].

Ở CP3, tôi gắn nhãn 20 ca trong 8 phút, không trao đổi với Người gắn nhãn 1. Hai bộ nhãn đồng thuận 20/20 = 100%. Khi hai người sửa cùng dòng trong `bang_loi.md` và bị conflict git, tôi gộp lại mà không sửa nhãn nào.

Ở CP4–CP5, tôi điền mục 4–7 từ `chi_so.md` và `pilot_plan.yaml`, rồi chốt đề xuất Go có điều kiện cho `noi_dia` + `hang_nang`. Đề xuất nêu hai con số bất lợi (xem lại 100% là 0,98–1,03×; power 0,64 ở mức chênh 5 điểm) và 4 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra.

Vì không viết code, tôi là người chạy lại `cd src && python lab13.py` trên máy riêng; ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25). Tôi viết mục 2–8 của `group_report.md` và rà hồ sơ theo checklist nộp bài.

## 4. Bằng chứng

- Commit `9f51a19` trên `main` (hồ sơ mục 1–3, 5; nhãn người 2; khung TEAM.md, group_report) và các commit hoàn thiện sau đó.
- File `report/team/ho_so_launch_v0.md`, cột "Nhãn người 2" trong `report/team/bang_loi.md`, `report/team/group_report.md`.

## 5. Công cụ AI đã dùng

Tôi dùng Claude Code để đọc cấu trúc repo và đề bài, giải thích vai trò và các khái niệm (năm loại lỗi Google PAIR, hệ số thiết kế, cỡ mẫu hiệu dụng), soạn nháp các ô trong hồ sơ và group_report, và gộp conflict git.

Để tự kiểm tra, tôi đối chiếu mọi số trong hồ sơ với output `python lab13.py` của nhóm và với số tính lại độc lập từ hai file CSV; hai nguồn khớp 100%. Nhãn 20 ca do tôi tự gắn, AI chỉ chép vào bảng. Tôi chạy lệnh `grep -rni` theo checklist nộp bài để rà từ cấm trong `report/team` và `TEAM.md`.

## 6. Tự đánh giá

Tôi điền hồ sơ từ sớm nên đến 17:00 đã đủ bảy mục, và đề xuất nêu cả con số bất lợi lẫn cách xử lý. Điểm cần cải thiện: phần của tôi phụ thuộc vào tiến độ file của thành viên khác, nên mục 6 phải chờ `pilot_plan.yaml` hoàn thiện. Lần sau tôi sẽ chốt sớm với nhóm hạn nộp từng file.
