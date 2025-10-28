import nhanvienFN as nhanvienFN
import os


FILE_DATA = "nhanvien_data.csv"

class QuanLiNV:
    def __init__(self):
        self.dsnv= []
        self.doc_dsnv()

    def _nhap_float(self, thong_bao, gia_tri_mac_dinh=None):
        while True:
            try:
                gia_tri = input(thong_bao).strip()
                if not gia_tri:
                    return gia_tri_mac_dinh if gia_tri_mac_dinh is not None else 0.0
                return float(gia_tri)
            except ValueError:
                print("Lỗi: Vui lòng nhập một số hợp lệ.")

    def nhap_dsnv(self):
        print("\n--- 1. Nhập danh sách nhân viên ---")
        while True:
            ma = input("Nhập Mã nhân viên (hoặc Enter để kết thúc): ").strip()
            if not ma:
                break
            if any(n.ma.lower() == ma.lower() for n in self.dsnv):
                print(f"Lỗi: Mã nhân viên '{ma}' đã tồn tại.")
                continue

            ho_ten = input("Nhập Họ tên nhân viên: ").strip()
            bo_phan = input("Nhập Bộ phận (Hành chính/Tiếp thị/Trưởng phòng): ").strip()
            luong = self._nhap_float("Nhập Lương tháng: ")
            bo_phan_lower = bo_phan.lower()
            
            if "hành chính" in bo_phan_lower:
                nv_moi = nhanvienFN.NhanVien(ma, ho_ten, "Hành chính", luong)
            elif "tiếp thị" in bo_phan_lower:
                doanh_so = self._nhap_float("Nhập Doanh số bán hàng: ")
                ti_le_hoa_hong = self._nhap_float("Nhập Tỉ lệ hoa hồng: ")
                nv_moi = nhanvienFN.TiepThi(ma, ho_ten, "Tiếp thị", luong, doanh_so, ti_le_hoa_hong)
            elif "trưởng phòng" in bo_phan_lower:
                luong_trach_nhiem = self._nhap_float("Nhập Lương trách nhiệm: ")
                nv_moi = nhanvienFN.TruongPhong(ma, ho_ten, "Trưởng phòng", luong, luong_trach_nhiem)
            else:
                print("Bộ phận không hợp lệ. Nhân viên không được thêm.")
                continue
            
            self.dsnv.append(nv_moi)
            self.luu_dsnv()
        
    def luu_dsnv(self):
        try:
            with open(FILE_DATA, 'w', encoding='utf-8') as f:
                for nv_obj in self.dsnv:
                    parts = [str(nv_obj.ma), nv_obj.ho_ten, nv_obj.bo_phan, str(nv_obj.luong)]    
                    if isinstance(nv_obj, nhanvienFN.TruongPhong):
                        parts.insert(0, 'TP')
                        parts.append(str(nv_obj.luong_trach_nhiem))
                    elif isinstance(nv_obj, nhanvienFN.TiepThi):
                        parts.insert(0, 'TT')
                        parts.append(str(nv_obj.doanh_so))
                        parts.append(str(nv_obj.ti_le_hoa_hong))
                    else:
                        parts.insert(0, 'HC')
                    f.write("|".join(parts) + "\n")
                    print("Lưu danh sách nhân viên vào file thành công")
        except Exception as e:
            print(f"Lỗi khi ghi file: {e}")

    def doc_dsnv(self):
        print("\n--- 2. Đọc thông tin nhân viên ---")
        self.dsnv = []
        if not os.path.exists(FILE_DATA):
            print(f"Không tìm thấy file dữ liệu '{FILE_DATA}'. Bắt đầu với danh sách trống.")
            return
        try:
            with open(FILE_DATA, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if not parts or len(parts) < 5: continue
                    parts = [p.strip() for p in parts]
                    loai_nv = parts[0]
                    ma, ho_ten, bo_phan, luong = parts[1:5]
                    nv_obj = None

                    if loai_nv == 'TP' and len(parts) >= 6:
                        luong_trach_nhiem = parts[5]
                        nv_obj = nhanvienFN.TruongPhong(ma, ho_ten, bo_phan, luong, luong_trach_nhiem)
                    elif loai_nv == 'TT' and len(parts) >= 7:
                        doanh_so, ti_le_hoa_hong = parts[5], parts[6]
                        nv_obj = nhanvienFN.TiepThi(ma, ho_ten, bo_phan, luong, doanh_so, ti_le_hoa_hong)
                    elif loai_nv == 'HC':
                        nv_obj = nhanvienFN.NhanVien(ma, ho_ten, bo_phan, luong)
                    
                    if nv_obj:
                        self.dsnv.append(nv_obj)
            
            print(f"Đã tải thành công nhân viên từ file.")

        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")
            
    def xuat_dsnv(self):
        if not self.dsnv:
            print("Danh sách nhân viên hiện đang trống.")
            return
        print("\n=======================================================")
        print(f"DANH SÁCH NHÂN VIÊN ({len(self.dsnv)} người)")
        print("=======================================================")
        for nv_obj in self.dsnv:
            nv_obj.xuat()
            print("-------------------------------------------------------")
            
    def tim_nhan_vien_theo_ma(self):
        print("\n--- 3. Tìm nhân viên theo mã ---")
        ma_tim = int(input("Nhập mã nhân viên cần tìm: "))
        nv_tim_thay = None
        for nv_obj in self.dsnv:
            if int(nv_obj.ma) == ma_tim:
                nv_tim_thay = nv_obj
                break
        if nv_tim_thay:
            print(f"Đã tìm thấy nhân viên có mã '{ma_tim}' - Họ tên: {nv_tim_thay.ho_ten}")
        else:
            print(f"Không tìm thấy nhân viên nào có mã '{ma_tim}'")

    def xoa_nhan_vien(self):
        print("\n--- 4. Xóa thông tin nhân viên ---")
        ma_xoa = int(input("Nhập mã nhân viên cần XÓA: "))
        index_to_delete = -1
        for i, nv_obj in enumerate(self.dsnv):
            if int(nv_obj.ma) == ma_xoa:
                index_to_delete = i
                break
        if index_to_delete != -1:
            ten_nv = self.dsnv[index_to_delete].ho_ten
            del self.dsnv[index_to_delete]
            self.luu_dsnv()
            print(f"Đã xóa nhân viên '{ten_nv}' (Mã: {ma_xoa}) và cập nhật file.")
        else:
            print(f"Không tìm thấy nhân viên có mã '{ma_xoa}' để xóa.")

    def cap_nhat_thong_tin_nhan_vien(self):
        print("\n--- 5. Cập nhật thông tin nhân viên ---")
        ma_cap_nhat = int(input("Nhập mã nhân viên cần CẬP NHẬT: "))
        nv_cap_nhat = None
        for nv_obj in self.dsnv:
            if int(nv_obj.ma) == ma_cap_nhat:
                nv_cap_nhat = nv_obj
                break
        if not nv_cap_nhat:
            print(f"Không tìm thấy nhân viên có mã '{ma_cap_nhat}'.")
            return
        print(f"\nĐang cập nhật nhân viên: {nv_cap_nhat.ho_ten} (Mã: {nv_cap_nhat.ma})")
        ho_ten_moi = input(f"Nhập Họ tên mới (Cũ: {nv_cap_nhat.ho_ten}): ").strip()
        if ho_ten_moi:
            nv_cap_nhat.ho_ten = ho_ten_moi
        luong_hien_tai = f"{nv_cap_nhat.luong:,.0f} VND"
        luong_thang_moi = self._nhap_float(f"Nhập Lương tháng mới (Cũ: {luong_hien_tai}): ", -1)
        if luong_thang_moi != -1 and luong_thang_moi >= 0:
            nv_cap_nhat.luong = luong_thang_moi

        if isinstance(nv_cap_nhat, nhanvienFN.TruongPhong):
            print("--- Cập nhật Trưởng phòng ---")
            luong_tn_hien_tai = f"{nv_cap_nhat.luong_trach_nhiem:,.0f}"
            luong_tn_moi = self._nhap_float(f"Nhập Lương trách nhiệm mới (Cũ: {luong_tn_hien_tai}): ", -1)
            if luong_tn_moi != -1 and luong_tn_moi >= 0:
                nv_cap_nhat.luong_trach_nhiem = luong_tn_moi
                
        elif isinstance(nv_cap_nhat, nhanvienFN.TiepThi):
            print("--- Cập nhật Nhân viên Tiếp thị ---")
            ds_hien_tai = f"{nv_cap_nhat.doanh_so:,.0f}"
            ds_moi = self._nhap_float(f"Nhập Doanh số mới (Cũ: {ds_hien_tai}): ", -1)
            if ds_moi != -1 and ds_moi >= 0:
                nv_cap_nhat.doanh_so = ds_moi
                
            ti_le_hien_tai = nv_cap_nhat.ti_le_hoa_hong * 100 
            tl_moi = self._nhap_float(f"Nhập Tỉ lệ hoa hồng mới (Cũ: {ti_le_hien_tai:.1f}%): ", -1)
            if tl_moi != -1 and tl_moi >= 0:
                nv_cap_nhat.ti_le_hoa_hong = tl_moi / 100
        self.luu_dsnv()
        print(f"Đã cập nhật thành công nhân viên mã '{ma_cap_nhat}' và ghi vào file.")

    def tim_nhan_vien_theo_khoang_luong(self):
        print("\n--- 6. Tìm nhân viên theo khoảng lương ---")
        ds_ket_qua = []
        luong_min = float(input("Nhập mức lương tối thiểu: "))
        luong_max = float(input("Nhập mức lương tối đa: "))
    
        if luong_min > luong_max:
                print("Lỗi: Mức lương tối thiểu không thể lớn hơn tối đa")
                return
        ds_ket_qua = [
            nv for nv in self.dsnv 
                if luong_min <= nv.get_thu_nhap() <= luong_max
                ]
        if ds_ket_qua:
            print(f"Đã tìm thấy nhân viên có thu nhập từ {luong_min:,.0f} VND đến {luong_max:,.0f} VND:")
            for nv in ds_ket_qua:
                print(f"{nv.ma:<10}{nv.ho_ten:<25}{nv.get_thu_nhap():>10}")
        else:
            print(f"Không tìm thấy nhân viên nào trong khoảng lương này")

    def sap_xep_theo_ho_ten(self):
        print("\n--- 7. Sắp xếp thông tin nhân viên từ A-Z ---")
        def lay_ten(ho_ten):
            ten_day_du = ho_ten.strip().split()
            return ten_day_du[-1] if ten_day_du else ""
        ds_sap_xep = sorted(
            self.dsnv, 
            key=lambda nv: (lay_ten(nv.ho_ten), nv.ho_ten))
        print("Danh sách nhân viên sau khi sắp xếp theo Tên (A-Z):")
        for nv in ds_sap_xep:
                print(f"{nv.ma:<10}{nv.ho_ten:<25}{nv.get_thu_nhap():>10}")
        
    def sap_xep_theo_thu_nhap(self):
        print("\n--- 8. Sắp xếp nhân viên theo thu nhập ---")
        ds_sap_xep = sorted(
            self.dsnv, 
            key=lambda nv: nv.get_thu_nhap(), 
            reverse=True)
        print("Danh sách nhân viên sau khi sắp xếp theo Thu nhập (Giảm dần):")
        for nv in ds_sap_xep:
                print(f"{nv.ma:<10}{nv.ho_ten:<25}{nv.get_thu_nhap():>10}")

    def xuat_5_nhan_vien_thu_nhap_cao_nhat(self):
        print("\n--- 9. Xuất 5 nhân viên có lương cao nhất ---")
        ds_sap_xep = sorted(
            self.dsnv, 
            key=lambda nv: nv.get_thu_nhap(), 
            reverse=True)
        ds_top_5 = ds_sap_xep[:5]
        if ds_top_5:
            print(f"TOP NHÂN VIÊN CÓ THU NHẬP CAO NHẤT:")
            for nv in ds_top_5:
                print(f"{nv.ma:<10}{nv.ho_ten:<25}{nv.get_thu_nhap():>10}")
        else:
            print("Danh sách nhân viên trống, không thể xuất Top 5")