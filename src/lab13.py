"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000  # đồng mỗi tháng (vận hành, giám sát, cập nhật chính sách)
KHOI_LUONG_THANG = 45_000           # yêu cầu toàn công ty mỗi tháng (1.500/ngày × 30)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not (0 < p <= 1):
        raise ValueError('p phải nằm trong (0, 1]')
    if k is not None and k < 1:
        raise ValueError('k phải >= 1')
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not (0 < p <= 1):
        raise ValueError('p phải nằm trong (0, 1]')
    if k is not None and k < 1:
        raise ValueError('k phải >= 1')
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = float((tien_token + tien_tool)[runs['attempt'] > 1].sum())

    token = float(tien_token.sum())
    tool = float(tien_tool.sum())
    xem_lai = float(reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai)
    lam_lai = float(reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai)
    tong = token + tool + xem_lai + lam_lai

    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong else math.inf
    hoa_don_moi_yc = (token + tool) / len(reqs) if len(reqs) else 0.0

    return {
        'token': token,
        'tool': tool,
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': cps,
        'hoa_don_moi_yc': hoa_don_moi_yc,
    }


# ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
def phan_tich_theo_loai(runs, reqs, thu_tu=('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac')):
    """Tính mô hình chi phí theo từng giá trị cột loai và tỉ lệ status == 'ok' theo từng lần chạy."""
    bang_loai = []
    for loai in thu_tu:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        bang_loai.append({
            'loai': loai,
            'so_yeu_cau': len(sub),
            'ti_le_thanh_cong': kq['thanh_cong'] / len(sub) if len(sub) else 0.0,
            'lan_chay_tb': float(sub['so_lan_chay'].mean()) if len(sub) else 0.0,
            'cps': kq['cps'],
            'so_voi_baseline': kq['cps'] / BASELINE,
        })

    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id', how='inner')
    runs_loai['ok'] = runs_loai['status'] == 'ok'
    ok_theo_lan = (
        runs_loai.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
        .reindex(list(thu_tu))
    )
    return bang_loai, ok_theo_lan


# ---------- Nhiệm vụ A4 · Chi phí cố định ----------
def tinh_chi_phi_co_dinh(
    runs,
    reqs,
    pham_vi=('noi_dia', 'hang_nang'),
    chi_phi_thang=CHI_PHI_CO_DINH_THANG,
    khoi_luong_thang=KHOI_LUONG_THANG,
):
    """Cộng chi phí cố định hàng tháng vào CPS phạm vi pilot ở 100% và 50% khối lượng."""
    reqs_pv = reqs[reqs['loai'].isin(pham_vi)]
    kq_pv = mo_hinh(runs, reqs_pv)
    ti_le_tc_tren_mau = kq_pv['thanh_cong'] / len(reqs)

    dong_ket_qua = []
    for nhan, kl in [(f'{khoi_luong_thang:,} yc/tháng', khoi_luong_thang),
                     ('Một nửa khối lượng', khoi_luong_thang / 2)]:
        viec_tc_thang = kl * ti_le_tc_tren_mau
        co_dinh_moi_viec = chi_phi_thang / viec_tc_thang
        tong_moi_viec = kq_pv['cps'] + co_dinh_moi_viec
        dong_ket_qua.append({
            'khoi_luong': nhan,
            'viec_tc_thang': viec_tc_thang,
            'co_dinh_moi_viec': co_dinh_moi_viec,
            'cps_pham_vi': kq_pv['cps'],
            'tong_moi_viec': tong_moi_viec,
            'so_voi_baseline': tong_moi_viec / BASELINE,
        })
    return dong_ket_qua


# ---------- Nhiệm vụ B · Bảng độ nhạy, giới hạn chạy lại, xem lại 100% ----------
def phan_tich_do_nhay(runs, reqs):
    """Tính CPS cho 9 kịch bản đổi đơn lẻ (B1) và 1 kịch bản đổi cặp (B2)."""
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban_don = [
        ('Giá token gấp đôi', dict(gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2)),
        ('Giá token giảm một nửa', dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2)),
        ('Tỉ lệ xem lại gấp đôi', dict(he_so_xem_lai=2.0)),
        ('Tỉ lệ xem lại giảm một nửa', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại gấp đôi', dict(he_so_lam_lai=2.0)),
        ('Số ca làm lại giảm một nửa', dict(he_so_lam_lai=0.5)),
        ('Lương nhân viên tăng 25%', dict(luong_phut=LUONG_PHUT * 1.25)),
        ('Chỉ cho chạy tối đa 2 lần', dict(max_lan_chay=2)),
        ('Chỉ cho chạy 1 lần', dict(max_lan_chay=1)),
    ]
    bang_b1 = []
    for ten, kw in kich_ban_don:
        cps = mo_hinh(runs, reqs, **kw)['cps']
        bang_b1.append({'kich_ban': ten, 'cps': cps, 'thay_doi_pct': (cps / goc - 1) * 100})

    cps_cap = mo_hinh(runs, reqs, gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2, he_so_xem_lai=2.0)['cps']
    cap_doi = {'kich_ban': 'Giá token ×2 và xem lại ×2', 'cps': cps_cap, 'thay_doi_pct': (cps_cap / goc - 1) * 100}
    return goc, bang_b1, cap_doi


def phan_tich_gioi_han_chay_lai(runs, reqs, cac_gioi_han=(1, 2, 3)):
    """So sánh chi phí cả hệ thống và CPS ở các giới hạn chạy lại 1, 2, 3 lần (B3)."""
    ket_qua = []
    for k in cac_gioi_han:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        chi_phi_he_thong = kq['tong'] + khong_tc * BASELINE
        ket_qua.append({
            'gioi_han': k,
            'tong_tro_ly': kq['tong'],
            'khong_thanh_cong': khong_tc,
            'chi_phi_he_thong': chi_phi_he_thong,
            'cps': kq['cps'],
        })
    return ket_qua


def khao_sat_xem_lai_100_phan_tram(runs, reqs, pham_vi=('noi_dia', 'hang_nang'), phut_xem_lai=5.0):
    """Tính CPS khi xem lại 100% ca ok trong phạm vi pilot (B4), với 9 phút và mức trung bình thực tế."""
    pv = reqs[reqs['loai'].isin(pham_vi)]
    kq_pv = mo_hinh(runs, pv)
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    ok_ids = set(runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'])

    so_ca_ok = int(pv['request_id'].isin(ok_ids).sum())
    so_ca_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    so_tc = kq_pv['thanh_cong']
    token_tool = kq_pv['token'] + kq_pv['tool']
    tien_xem_lai = so_ca_ok * phut_xem_lai * LUONG_PHUT

    tb_lam_lai_thuc_te = float(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean())
    ket_qua = []
    for nhan, phut_ll in [('Giả định đề bài (9 phút/ca)', 9.0),
                          (f'Trung bình dữ liệu ({tb_lam_lai_thuc_te:.1f} phút/ca)', tb_lam_lai_thuc_te)]:
        tien_lam_lai = so_ca_lam_lai * phut_ll * LUONG_PHUT
        tong = token_tool + tien_xem_lai + tien_lam_lai
        cps = tong / so_tc
        xem_lai_hoa_von = (BASELINE * so_tc - token_tool - tien_lam_lai) / (so_ca_ok * LUONG_PHUT)
        ket_qua.append({
            'muc_lam_lai': nhan,
            'so_ca_ok': so_ca_ok,
            'so_ca_lam_lai': so_ca_lam_lai,
            'token_tool': token_tool,
            'tien_xem_lai': tien_xem_lai,
            'tien_lam_lai': tien_lam_lai,
            'tong': tong,
            'cps': cps,
            'so_voi_baseline': cps / BASELINE,
            'xem_lai_hoa_von_phut': xem_lai_hoa_von,
        })
    return ket_qua


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    print('\n--- A1 · Kết quả 3 phép thử (p=0.8) ---')
    print(f'so_lan_chay_ky_vong(0.8, 2)             = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'so_lan_chay_ky_vong(0.8)                = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'he_so_chi_phi_moi_viec_thanh_cong(0.8,3)= {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    print('\n--- A2 · Mô hình chi phí từ trace ---')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        fmt = f'{gia_tri:>14,.1f}' if ten == 'hoa_don_moi_yc' else f'{gia_tri:>14,.0f}'
        print(f'{ten:15s} {fmt}')
    print(f"phut_xem_lai_simulated = {reqs['phut_xem_lai_simulated'].sum():,.0f} phút")
    print(f"phut_lam_lai_simulated = {reqs['phut_lam_lai_simulated'].sum():,.0f} phút")
    print(f"tool_calls             = {runs['tool_calls'].sum():,.0f} lần")
    print(f"CPS / hóa đơn mỗi yc   = {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.2f}x")
    print(f"Tỉ trọng làm lại [sim] = {ket_qua['lam_lai'] / ket_qua['tong'] * 100:.1f}%")
    print(f"Tỉ trọng xem lại [sim] = {ket_qua['xem_lai'] / ket_qua['tong'] * 100:.1f}%")
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f"Chi phí cả hệ thống/yc = {he_thong_moi_yc:,.0f} đ ({he_thong_moi_yc / BASELINE:.2f}x của {BASELINE:,} đ) [simulated]")

    # Nhiệm vụ A3: tách theo từng giá trị của cột loai
    bang_loai, ok_theo_lan = phan_tich_theo_loai(runs, reqs)
    print('\n--- A3 · Tách theo loại yêu cầu (CPS là số simulated) ---')
    print(f"{'Loại':10s} {'Số YC':>7s} {'Thành công':>11s} {'Lần chạy/YC':>12s} {'CPS [sim]':>12s} {'So 12k':>8s}")
    for r in bang_loai:
        print(
            f"{r['loai']:10s} {r['so_yeu_cau']:>7,d} {r['ti_le_thanh_cong']*100:>10.1f}% "
            f"{r['lan_chay_tb']:>12.2f} {r['cps']:>10,.0f} đ {r['so_voi_baseline']:>7.2f}x"
        )
    print('\nTỉ lệ status == ok theo từng lần chạy (attempt):')
    print((ok_theo_lan * 100).round(1).astype(str) + '%')

    # Nhiệm vụ A4: chi phí cố định (phạm vi noi_dia + hang_nang)
    bang_co_dinh = tinh_chi_phi_co_dinh(runs, reqs)
    print('\n--- A4 · Chi phí cố định 40tr/tháng (phạm vi noi_dia + hang_nang, simulated) ---')
    print(f"CPS chưa cố định trong phạm vi = {bang_co_dinh[0]['cps_pham_vi']:,.0f} đ [simulated]")
    print(f"{'Khối lượng':20s} {'Việc TC/tháng':>14s} {'Cố định/việc':>13s} {'CPS+CĐ [sim]':>13s} {'So 12k':>8s}")
    for r in bang_co_dinh:
        print(
            f"{r['khoi_luong']:20s} {r['viec_tc_thang']:>14,.0f} {r['co_dinh_moi_viec']:>11,.0f} đ "
            f"{r['tong_moi_viec']:>11,.0f} đ {r['so_voi_baseline']:>7.2f}x"
        )

    # Nhiệm vụ B · Độ nhạy, giới hạn chạy lại và xem lại 100%
    goc_cps, bang_b1, cap_b2 = phan_tich_do_nhay(runs, reqs)
    print(f'\n--- B1 · Bảng độ nhạy (CPS gốc = {goc_cps:,.0f} đ [simulated]) ---')
    print(f"{'Kịch bản':30s} {'CPS [sim]':>12s} {'Thay đổi':>10s}")
    for r in bang_b1:
        print(f"{r['kich_ban']:30s} {r['cps']:>10,.0f} đ {r['thay_doi_pct']:>+9.1f}%")
    print('\n--- B2 · Đổi một cặp ---')
    print(f"{cap_b2['kich_ban']:30s} {cap_b2['cps']:>10,.0f} đ {cap_b2['thay_doi_pct']:>+9.1f}%")

    bang_b3 = phan_tich_gioi_han_chay_lai(runs, reqs)
    print('\n--- B3 · Chi phí cả hệ thống theo giới hạn chạy lại (simulated) ---')
    print(f"{'Giới hạn':8s} {'Tổng trợ lý [sim]':>18s} {'Không TC':>10s} {'Cả hệ thống [sim]':>18s} {'CPS [sim]':>12s}")
    for r in bang_b3:
        print(
            f"{str(r['gioi_han']) + ' lần':8s} {r['tong_tro_ly']:>16,.0f} đ "
            f"{r['khong_thanh_cong']:>10,d} {r['chi_phi_he_thong']:>16,.0f} đ {r['cps']:>10,.0f} đ"
        )

    bang_b4 = khao_sat_xem_lai_100_phan_tram(runs, reqs)
    print('\n--- B4 · Xem lại 100% phạm vi noi_dia + hang_nang (simulated) ---')
    print(f"Số ca ok xem lại = {bang_b4[0]['so_ca_ok']}, số ca lam_lai = {bang_b4[0]['so_ca_lam_lai']}, token+tool = {bang_b4[0]['token_tool']:,.0f} đ")
    for r in bang_b4:
        print(
            f"{r['muc_lam_lai']:35s} -> Tổng {r['tong']:>10,.0f} đ | "
            f"CPS = {r['cps']:>6,.0f} đ ({r['so_voi_baseline']:.2f}x) | Hòa vốn xem lại <= {r['xem_lai_hoa_von_phut']:.1f} phút"
        )

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
