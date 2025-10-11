class ChuNhat:


    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def get_chu_vi(self):
        return (self.dai + self.rong) * 2
    def get_dien_tich(self):
        return self.dai * self.rong
    def xuat(self):
        print(f"Hình chữ nhật có chiều dài là {self.dai}, rộng là {self.rong}, chu vi là {self.get_chu_vi()} và diện tích là {self.get_dien_tich()}")
    
    
class Vuong(ChuNhat):
    def __init__(self, canh):
        self.canh = canh
        super().__init__(self.canh, self.canh)
    def xuat(self):
        print(f"Hình vuông có cạnh: {self.dai}")
