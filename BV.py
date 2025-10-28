class HoaDon:
    def __init__(self, ma, ten_kh, dich_vu):
        self.__ma = ma
        self.__ten_kh = ten_kh
        self.__dich_vu = dich_vu
    def tinh_tien_hoa_don(self):
        pass
    def danh_gia_muc_su_dung(self):
        pass
    def xuat(self):
        print(f"Mã Khách Hàng {self.__ma} có tên {self.__ten_kh} sử dụng loại dịch vụ {self.__dich_vu} và tiền hóa đơn là {self.tinh_tien_hoa_don()} có đánh giá mức sử dụng {self.danh_gia_muc_su_dung()}")

class HoaDonDien(HoaDon):
    def __init__(self, ma, ten_kh, dich_vu, chi_so_thang_truoc, chi_so_thang_nay):
        super().__init__(ma, ten_kh, dich_vu)
        self.__chi_so_thang_truoc = chi_so_thang_truoc
        self.__chi_so_thang_nay = chi_so_thang_nay
    def tinh_tien_hoa_don(self):
        So_Kwh = self.__chi_so_thang_nay - self.__chi_so_thang_truoc
        Tong = So_Kwh*2500
        return (Tong)
    def danh_gia_muc_su_dung(self):
            So_Kwh = self.__chi_so_thang_nay - self.__chi_so_thang_truoc
            if So_Kwh <= 100 and So_Kwh >= 0:
                Muc_SD = "Thấp"
            elif So_Kwh <= 300:
                Muc_SD = "Trung Bình"
            else:
                Muc_SD = "Cao"
            return Muc_SD
    
class HoaDonNuoc(HoaDon):
    def __init__(self, ma, ten_kh, dich_vu, M3):
         super().__init__(ma, ten_kh, dich_vu)
         self.__M3 = M3
    def tinh_tien_hoa_don(self):
        return( self.__M3 * 1000)
    def danh_gia_muc_su_dung(self):
        if self.__M3 <=10 and self.__M3 >= 0:
            Muc_SD = "Thấp"
        elif self.__M3 <= 30:
            Muc_SD = "Trung Bình"
        else:
            Muc_SD = "Cao"
        return Muc_SD






    