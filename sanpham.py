class SanPham:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__giam_gia = giam_gia

    def get_ten_sp(self):
        return self.__ten_san_pham
    def set_ten_sp(self, ten_sp):
        self.__ten_san_pham = ten_sp
    def get_gia_sp(self):
        return self.__gia
    def set_gia_sp(self, gia_sp):
        self.__gia = gia_sp
    def get_giam_gia_sp(self):
        return self.__giam_gia
    def set_giam_gia_sp(self, giam_gia_sp):
        self.__giam_gia = giam_gia_sp

    def thue_nhap_khau(self):
        return self.__gia * 0.1
    def nhap_thong_tin_sp(self):
        self.__ten_san_pham = input("Tên sản phẩm: ")
        self.__gia = float(input("Giá sản phẩm: "))
        self.__giam_gia = float(input("Giảm giá sản phẩm: "))
    def __str__(self):
        thongtin = f"""Sản phẩm {self.__ten_san_pham} có giá {self.__gia} được giảm giá {self.__giam_gia} và thuế nhập khẩu {self.thue_nhap_khau()}"""
        return thongtin
    