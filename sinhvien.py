class sinhvien:
    # Các phương thức
    def __init__(self, ten_sv, namsinh_sv, diem_sv,):
        self.ten_sinh_vien = ten_sv
        self.nam_sinh = namsinh_sv
        self.diem = diem_sv
    def __str__(self):
        return f"Sinh viên {self.ten_sinh_vien} sinh năm {self.nam_sinh} có điểm {self.diem}"

class sinhvienXLDL(sinhvien):
     def __init__(self, ten_sv, namsinh_sv, diem_sv,lap_trinh):
        super().__init__(ten_sv, namsinh_sv, diem_sv)
        self.lap_trinh = lap_trinh
     def __str__(self):
        return f"{super().__str__()} và học lập trình {self.lap_trinh}"
    
sv1 = sinhvienXLDL("Phúc", 2006, 8.5, "Python")
print(sv1)