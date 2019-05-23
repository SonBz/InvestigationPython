class ConNguoi :
    def __init__(self,ten,tuoi):
        self.ten = ten
        self.tuoi =tuoi

class SinhVien(ConNguoi):
    def __init__(self,ten,tuoi,truong,lop):
        super().__init__(ten,tuoi)
        self.truong=truong
        self.lop=lop

sv = SinhVien("Nguyễn Tạ Sơn",12,"HVKTMM","AT13E")
print(sv.__dict__)