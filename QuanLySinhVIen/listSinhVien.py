class sinhVien:
    def __init__(self,name,age):
        self.name=name
        self.age=age
lis=[]
s=sinhVien("son",18)
s2=sinhVien("cuong",20)
lis.append(s)
lis.append(s2)
with open("file.txt","r") as new :
    lis=new.read().split("\n")
    for i in range(len(lis)-1):
        new_list=lis[i].split("-")
        #print(i,"-",lis[i])
        print(i,"-",new_list[0],"-",new_list[1],"-",new_list[2]) 
    



   


