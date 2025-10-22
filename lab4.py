# Code lab 4 bài 1 ở đây
def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if so_nuoc <= 10 and so_nuoc >= 0:
        tien_nuoc_thang = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc_thang = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_nuoc_thang = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc_thang = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc_thang
    

    # Code lab 4  bài 2 ở đây
def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_db):
    banh_dau_xanh = {"đường": 0.04, "đậu": 0.07}
    banh_thap_cam = {"đường": 0.06, "đậu": 0}
    banh_deo = {"đường": 0.05 , "đậu": 0.02}
    nguyen_lieu = {}
    duong_hop_banh = sl_bdx * banh_dau_xanh["đường"] + sl_btc * banh_thap_cam["đường"] + sl_db * banh_deo["đường"]
    dau_hop_banh = sl_bdx * banh_dau_xanh["đậu"] + sl_btc * banh_thap_cam["đậu"] + sl_db * banh_deo["đậu"]
    nguyen_lieu["đường"] = duong_hop_banh
    nguyen_lieu["đậu"] = dau_hop_banh
    return nguyen_lieu