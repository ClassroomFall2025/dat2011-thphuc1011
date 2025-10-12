import SinhVienPoly as svpl

class QuanLiSV:
    def __init__(self):
        self.dssv = []

    def nhap_dssv(self):
        while True:
            ho_ten = input("Nhập họ tên sinh viên: ")
            nganh_hoc = input("Nhập ngành học sinh viên: ")
            if nganh_hoc.lower() == "it":
                java = float(input("Điểm Java: "))
                html = float(input("Điểm Htmk: "))
                css = float(input("Điểm Css: "))
                sv = svpl.SinhVienIT(ho_ten, nganh_hoc, java, html, css)
                self.dssv.append(sv)
            elif nganh_hoc.lower() == "biz":
                marketing = float(input("Điểm Marketing: "))
                sales = float(input("Điểm Sales: "))
                sv = svpl.SinhVienBiz(ho_ten, nganh_hoc, marketing, sales)
                self.dssv.append(sv)
            elif nganh_hoc.lower() == "exit":
                print("Kết thúc nhập thông tin sinh viên")
                break
            else:
                print("Nhập sai yêu cầu")
            return self.dssv
    def xuat_dssv(self):
        if not self.dssv:
            print("Danh sách sinh viên rỗng")
        else:
            print(f'{"Tên Sinh Viên":<20} {"Ngành Học":<10} {"Điểm":<10} {"Học Lực":<10}')
            for sv in self.dssv:
                sv.xuat()
    def xuat_dssv_gioi(self):
        if not self.dssv:
            print("Danh sách sinh viên rỗng")
        else:
            print("Danh sách sinh viên học lực giỏi")
            dssv_gioi  = [sv for sv in self.dssv if sv.get_hoc_luc() == "Giỏi"]
            print(f'{"Tên Sinh Viên":<20} {"Ngành Học":<10} {"Điểm":<10} {"Học Lực":<10}')
            for sv in dssv_gioi:
                sv.xuat()
    def sap_xep_dssv(self):
        if not self.dssv:
            print("Danh sách sinh viên rỗng")
        else:
            print("Danh sách sinh viên điểm số tăng dần")
            dssv_sapxep = sorted(self.dssv, key = lambda z :z.get_diem())
            print(f'{"Tên Sinh Viên":<20} {"Ngành Học":<10} {"Điểm":<10} {"Học Lực":<10}')
            for sv in dssv_sapxep:
                sv.xuat()