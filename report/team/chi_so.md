# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200; dữ liệu giả lập) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177; dữ liệu giả lập) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200; dữ liệu giả lập) |
| Dùng | Tỉ lệ yêu cầu nhóm can thiệp có gợi ý trợ lý được hiển thị | Số `request_id` có `agent_suggestion_shown` / số yêu cầu được phân vào arm can thiệp | Chưa tính được từ CSV hiện tại; đo bằng event |
| An toàn | Tỉ lệ đơn hoàn sai tiền trong mẫu kiểm toán | Số `audit_sample_checked` có `lech_vnd != 0` / tổng số đơn được kiểm toán | Chưa tính được từ CSV hiện tại; đo bằng event |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien_vnd`, `arm`, `depot`, `created_at`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `input_validation_failed` | Giao diện tiếp nhận | `request_id`, `loai_loi`, `truong_nhap`, `trace_id` | Khi khách nhập sai định dạng (khớp Ca 9) |
| `agent_run_completed` | Agent | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `pricing_version`, `trace_id` | Sau mỗi lần chạy, kể cả lần `loi` |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai_thuc_te`, `trace_id` | Khi nhân viên bấm giữ/sửa/bỏ (thay số simulated sau tuần 1) |
| `staff_rework_completed` | Nhân viên CSKH | `request_id`, `staff_id`, `phut_lam_lai_thuc_te`, `ly_do`, `trace_id` | Khi nhân viên làm lại xong ca sai (thay số simulated sau tuần 1) |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien_vnd`, `ket_qua` (`ok`/`loi`), `trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái (khớp Ca 7, Ca 20) |
| `refund_notice_sent` | Dịch vụ thông báo | `request_id`, `loai_thong_bao` (`da_hoan`/`dang_xu_ly`/`tu_choi`), `kenh`, `trace_id` | Khi gửi thông báo kết quả tới khách (đối soát Ca 7) |
| `handoff_to_staff` | Agent | `request_id`, `reason`, `loai`, `tom_tat`, `trace_id` | Khi chuyển ca cho nhân viên (khớp Ca 4) |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách hàng | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu (khớp Ca 18) |
| `audit_sample_checked` | Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `lech_vnd`, `trace_id` | Hằng tuần khi kiểm tra mẫu 100 đơn (khớp Ca 17) |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính (`% đóng trong 24h và không mở lại trong 7 ngày`):** nối qua `request_id` (và `trace_id`), tách theo `arm` và `loai` từ `refund_request_created` (`created_at`), kiểm tra `ticket_closed` (`closed_at <= created_at + 24h`) và không có `ticket_reopened` trong 7 ngày sau `closed_at`.
- **Dùng (`Tỉ lệ bỏ qua gợi ý`):** số event `staff_review_decision` có `quyet_dinh` là `sua` hoặc `bo`, chia cho tổng số lượt có quyết định ở `staff_review_decision` (khớp định nghĩa `duoc_xem_lai == 1`).
- **An toàn (`Tỉ lệ lỗi lọt đến khách`):** số `request_id` có `ticket_reopened` trong 7 ngày sau `ticket_closed`, chia cho tổng `refund_request_created` (tách riêng theo từng `arm`).
- **Dùng (dòng 4):** nối `refund_request_created.arm` với `agent_suggestion_shown` theo `request_id`; chia số yêu cầu arm can thiệp có gợi ý được hiển thị cho tổng yêu cầu arm can thiệp. CSV hiện tại không có event/arm nên chưa tính được.
- **An toàn (dòng 5):** lấy `audit_sample_checked.lech_vnd != 0` chia tổng event `audit_sample_checked`; CSV hiện tại không có mẫu kiểm toán nên chưa tính được.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS tăng 51,8%, từ 4.472 lên 6.787 đ/việc (simulated) | Tỉ lệ `lam_lai` theo tuần >7%; hiện tại 4,9% trong `noi_dia` + `hang_nang` | Thu hẹp về `noi_dia`, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | CPS 11.743 đ (0,98×); nếu làm lại trung bình 15,3 phút thì 12.415 đ (1,03×, simulated) | Tỉ lệ yêu cầu được xem lại >50% ở cuối bước rollout 0,25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ <15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định tăng thêm 1.185 đ/việc ở 45.000 yêu cầu/tháng, lên 2.370 đ/việc khi còn nửa khối lượng (simulated) | Số việc thành công theo tuần <50% kế hoạch | Không mở rộng pilot; xem lại chi phí cố định | PM trợ lý hoàn phí |
