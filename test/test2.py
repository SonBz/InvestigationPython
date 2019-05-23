class sinhvien:
        def __init__ (self,ten,tuoi):
                self.ten = ten
                self.tuoi = tuoi
        @classmethod
        def form_String(cls,str):
                lst = str.split('-')
                new_list=[st.strip() for st in lst]
                ten,tuoi  = new_list
                print(new_list)
                return cls(ten,tuoi)
 
str = "Nguyễn Tạ Sơn-12"
sinhvienA = sinhvien.form_String(str)
print(sinhvienA.__dict__)
