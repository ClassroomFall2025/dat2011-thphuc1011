import BV 

class QuanLiBV:
    def __init__(self):
        self.dshd = []
    
    def nhap_DSHD(self):
        while True:
            ma = int(input("Nhập Mã Khách Hàng: "))
            ten_kh = input("Nhập tên khách hàng: ")
            dich_vu = input("Nhập loại dịch vụ(Điện/Nước): ")
            if dich_vu.lower() == "điện":
                chi_so_thang_truoc = float(input("Nhập chỉ số điện tháng trước: "))
                chi_so_thang_nay = float(input("Nhập chỉ số điện tháng này: "))
                hd = BV.HoaDonDien(ma, ten_kh, dich_vu, chi_so_thang_truoc, chi_so_thang_nay)
                self.dshd.append(hd)
            elif dich_vu.lower() == "nước":
                M3 = float(input("Nhập số mét khối nước sử dụng: "))
                hd = BV.HoaDonNuoc(ma, ten_kh, dich_vu, M3)
                self.dshd.append(hd)
            else:
                print("Nhập sai yêu cầu")
            return self.dshd
    def xuat_DSHD(self):
        if not self.dshd:
            print("Danh sách hóa đơn rỗng")
        else:
            for sv in self.dshd:
                sv.xuat()

    def xuat_DSHD_DGC(self):
        if not self.dshd:
            print("Danh sách hóa đơn rỗng")
        else:
            dshd_cao  = [hd for hd in self.dshd if hd.danh_gia_muc_su_dung() == "Cao"]
            for sv in dshd_cao:
                sv.xuat()

    def sap_xep_DSHD(self):
        if not self.dshd:
            print("Danh sách hóa đơn rỗng")
        else:
            dshd_sapxep = sorted(self.dshd, key = lambda z :z.tinh_tien_hoa_don())
            for sv in dshd_sapxep:
                sv.xuat()
