import nhanvien as nhanvien

class QuanLiNV:
    def __init__(self):
        self.dsnv= []

    def nhap_dsnv(self):
        while True:
            ma = int(input("Nhập mã nhân viên: "))
            ho_ten = input("Nhập họ tên nhân viên: ")
            luong = float(input("Nhập lương nhân viên: "))
            bo_phan = input("Nhập bộ phận nhân viên: ")
            if bo_phan.lower() == "hành chính":
                nv = nhanvien.NhanVien(ma, ho_ten, bo_phan, luong)
                self.dsnv.append(nv)
            elif bo_phan.lower() == "tiếp thị":
                doanh_so = int(input("Nhập doanh số bán hàng: "))
                ti_le_hoa_hong = float(input("Nhập tỉ lệ hoa hồng: "))
                nv = nhanvien.TiepThi(ma, ho_ten, bo_phan, luong, doanh_so, ti_le_hoa_hong)
                self.dsnv.append(nv)
            elif bo_phan.lower() == "trưởng phòng":
                luong_trach_nhiem = float(input("Nhập lương trách nhiệm: "))
                nv = nhanvien.TruongPhong(ma, ho_ten, bo_phan, luong, luong_trach_nhiem)
                self.dsnv.append(nv)
            elif bo_phan.lower() == "exit":
                print("Kết thúc nhập thông tin sinh viên")
                break
            else:
                print("Nhập sai yêu cầu")
            return self.dsnv
        
    def tim_nhan_vien_theo_ma(self):
        ma_tim = int(input("Nhập mã nhân viên cần tìm: "))
        nv_tim_thay = None
        for nv in self.dsnv:
            if nv.ma == ma_tim:
                nv_tim_thay = nv
                break
        if nv_tim_thay:
            print(f"Đã tìm thấy nhân viên có mã '{ma_tim}' - Họ tên: {nv_tim_thay.ho_ten}")
        else:
            print(f"Không tìm thấy nhân viên nào có mã '{ma_tim}'")

    def tim_nhan_vien_theo_khoang_luong(self):
        ds_ket_qua = []
        luong_min = float(input("Nhập mức lương tối thiểu (VND): "))
        luong_max = float(input("Nhập mức lương tối đa (VND): "))
    
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
        ds_sap_xep = sorted(
            self.dsnv, 
            key=lambda nv: nv.get_thu_nhap(), 
            reverse=True)
        print("Danh sách nhân viên sau khi sắp xếp theo Thu nhập (Giảm dần):")
        for nv in ds_sap_xep:
                print(f"{nv.ma:<10}{nv.ho_ten:<25}{nv.get_thu_nhap():>10}")

    def xuat_5_nhan_vien_thu_nhap_cao_nhat(self):
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