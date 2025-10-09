class SanPham:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.ten_san_pham = ten_san_pham
        self.gia = gia
        self.__giam_gia = giam_gia


    def thue_nhap_khau(self):
        return self.gia * 0.1
    def nhap_thong_tin_sp(self):
        self.ten_san_pham = input("Tên sản phẩm: ")
        self.gia = float(input("Giá sản phẩm: "))
        self.__giam_gia = float(input("Giảm giá sản phẩm: "))
    def xuat_thong_tin_sp(self):
        print(f"Sản phẩm {self.ten_san_pham} có giá {self.gia} được giảm giá {self.__giam_gia} và thuế nhập khẩu {self.thue_nhap_khau()}")
    def __str__(self):
        return f"Sản phẩm {self.ten_san_pham} có giá {self.gia} được giảm giá {self.__giam_gia} và thuế nhập khẩu {self.thue_nhap_khau()}"