class sinhvien:
    # Các thuộc tính

    # Các phương thức
    def __init__(self, ten_sv, namsinh_sv, diem_sv):
        self.ten_sinh_vien = ten_sv
        self.nam_sinh = namsinh_sv
        self.diem = diem_sv
    def xuat_thong_tin_sv(self):
        print("Tên sinh viên:", self.ten_sinh_vien)
        print("Năm sinh:", self.nam_sinh)
        print("Điểm:", self.diem)

sv1 = sinhvien("Tình Chos", 2006, 0.5)
sv1.xuat_thong_tin_sv()