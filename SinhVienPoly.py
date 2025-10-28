class SinhVienPoly:
    def __init__(self, ho_ten, nganh_hoc):
        self.__ho_ten = ho_ten
        self.__nganh_hoc = nganh_hoc
    def get_diem(self):
        pass
    def get_hoc_luc(self):
        if self.get_diem() >= 9 and self.get_diem() <=  10:
            hoc_luc = "Xuất sắc" 
        elif self.get_diem() >= 8:
            hoc_luc = "Giỏi" 
        elif self.get_diem() >= 7:
            hoc_luc = "Khá" 
        elif self.get_diem() >= 5:
            hoc_luc = "Trung bình" 
        elif self.get_diem() >= 0:
            hoc_luc = "Chưa đạt"
        else:
           print("Điểm không hợp lệ")
        return hoc_luc
    def xuat(self):
        print(f"{self.__ho_ten:<20} {self.__nganh_hoc:<10} {self.get_diem():<10} {self.get_hoc_luc():<10}")

class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, nganh_hoc, diem_java, diem_html, diem_css):
        super().__init__(ho_ten, nganh_hoc)
        self.__diem_java = diem_java
        self.__diem_html = diem_html
        self.__diem_css =  diem_css
    def get_diem(self):
        return(2* self.__diem_java + self.__diem_html + self.__diem_css) /  4
    
class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, nganh_hoc, diem_marketing, diem_sales):
        super().__init__(ho_ten, nganh_hoc)
        self.__diem_marketing =  diem_marketing
        self.__diem_sales = diem_sales
    def get_diem(self):
        return (2* self.__diem_marketing + self.__diem_sales) / 3
    