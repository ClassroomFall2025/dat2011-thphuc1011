class SinhVienPoly:
    def __init__(self, ho_ten, nganh_hoc):
        self.ho_ten = ho_ten
        self.nganh_hoc = nganh_hoc
    def get_diem(self):
        pass
    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem >= 9 and diem <10:
            hoc_luc = "Xuất sắc" 
        elif 8 <= diem < 9:
            hoc_luc = "Giỏi" 
        elif 7 <= diem < 8:
            hoc_luc = "Khá" 
        elif 5 <= diem < 7:
            hoc_luc = "Trung bình" 
        else: 
            hoc_luc = "Yếu"
        return hoc_luc
        
    def xuat(self):
        print(f"{self.ho_ten: <16} {self.nganh_hoc: <8} {self.get_diem(): <8} {self.get_hoc_luc(): <8}")

class SinhVienIT(SinhVienPoly):
    def __init__(self, ten_sv, nganh, java, html, css):
        super().__init__(ten_sv, nganh)
        self.java = java
        self.html = html
        self.css = css
    def get_diem(self):
        return(2* self.java + self.html + self.css) /  4
    
class SinhVienBiz(SinhVienPoly):
    def __init__(self, sinh_vien, nganh, marketing, sales):
        super().__init__(sinh_vien, nganh)
        self.marketing =  marketing
        self.sales = sales
    def get_diem(self):
        return (2* self.marketing + self.sales) / 3
    