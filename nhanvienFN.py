class NhanVien:
    def __init__(self, ma, ho_ten, bo_phan, luong):
        self.ma = ma
        self.ho_ten = ho_ten
        self.bo_phan = bo_phan
        self.luong = float(luong)

    def get_thu_nhap(self):
        return self.luong
    
    def get_thue_thu_nhap(self):
        thu_nhap = float(self.get_thu_nhap())
        if thu_nhap <= 9000000:
            return 0
        elif thu_nhap <= 15000000:
            return (thu_nhap - 9000000) * 0.10
        else:
            thue_bac_1 = (15000000 - 9000000) * 0.10
            thue_bac_2 = (thu_nhap - 15000000) * 0.12
            return thue_bac_1 + thue_bac_2

    def xuat(self):
        print(f"{self.ma:<20} {self.ho_ten:<10} {self.bo_phan:<10} {self.luong:<10} {self.get_thu_nhap():<10} {self.get_thue_thu_nhap():<10}")

class TiepThi(NhanVien):
    def __init__(self, ma, ho_ten, bo_phan, luong, doanh_so, ti_le_hoa_hong):
        super().__init__(ma, ho_ten, bo_phan, luong)
        self.doanh_so = float(doanh_so)
        self.ti_le_hoa_hong = float(ti_le_hoa_hong)
    def get_thu_nhap(self):
        hoa_hong = self.doanh_so * self.ti_le_hoa_hong
        return self.luong + hoa_hong

class TruongPhong(NhanVien):
    def __init__(self, ma, ho_ten, bo_phan, luong, luong_trach_nhiem):
        super().__init__(ma, ho_ten, bo_phan, luong)
        self.luong_trach_nhiem = float(luong_trach_nhiem)
    def get_thu_nhap(self):
        return self.luong + self.luong_trach_nhiem