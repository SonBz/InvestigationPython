
from SinhVien import People

class Manage(People):
    def __init__(self,name,age,university,Class):
        super().__init__(name,age)
        self.university=university
        self.Class=Class


list_Sv=[]
Select =0 
while Select < 5:  
    print("")
    print("=========Menu==========") 
    print("1: Add student")
    print("2: Delete student")
    print("3: See The List Of Student")
    print("4: Student to Search")
    print("5: Exit The Program")
    Select = int(input("You Choose :"))  

    def addStudent():
        print("--You choose more students--")
        wantToAdd =int(input("Number of Student who want to add :"))
        fileStudent =open("file.txt","a")
        for i in range(wantToAdd):
            print(" Student",i+1)
            name = input("Enter name :")
            age = int(input("Enter age :"))
            university =input("University :")
            Class = input("Which Class :")
            Student = Manage(name,age,university,Class)
            out_string=str(Student.name)+"-"+str(Student.age)+"-"
                       +str(Student.university)+"-"+str(Student.Class)+"\n"
            fileStudent.write(out_string)
            #list_Sv.append(Student) 
        print(" Success (^-^)")
        fileStudent.close()
    
    def showList():
        print("Students List")
        fileStudent =open("file.txt","r")
        list_Sv = fileStudent.read().split("\n")
        for i in range(len(list_Sv)-1):
            list_sv_new=list_Sv[i].split("-")
            print("--> Student ",i+1)
            print("Student name :",list_sv_new[0],"- Age:",list_sv_new[1],
                  "University :",list_sv_new[2],"- Class:",list_sv_new[3])
        fileStudent.close()
    
    def seach():
        searchType =0
        fileStudent =open("file.txt","r")
        list_sv = fileStudent.read().split("\n")
        while searchType < 3:
            print("--Seach Type--")
            print("1:Search by name")
            print("2:Search by age")
            print("3:exit")
            searchType =int(input("You Choose :"))        
    
            def SearchName():
                flag =0
                fullName =input("name to search:")
                if fullName != " " :
                    for i in range(len(list_Sv)):
                        list_sv_new=list_sv[i].split("-")
                        if list_Sv[0] == fullName:
                            print("--> Student ",i+1)
                            print("Student name :",list_sv_new[0],"- Age:",list_sv_new[1],
                                  "University :",list_sv_new[2],"- Class:",list_sv_new[3])
                            flag = 1
                    if flag == 0:
                        print("No Student found")
                else:
                    print("request to enter information")
    
            def SearchAge():
                flag =0
                Age =int(input("age to search :"))
                if Age != " ":
                    for i in range(len(list_sv)):
                        list_sv_new=list_sv[i].split("-")
                        if list_Sv[1] == Age:
                            print("--> Student ",i+1)
                            print("Student name :",list_sv_new[0],"- Age:",list_sv_new[1],
                                  "University :",list_sv_new[2],"- Class:",list_sv_new[3])
                            flag = 1
                    if flag == 0:
                        print("No Student found")
                else:
                    print("request to enter information")
            LuaChoTimKiem ={
                1: SearchName,
                2: SearchAge
            }
            LuaChoTimKiem.get(searchType, lambda : " Error")()
        fileStudent.close()
    
    def delete() :
        flag =0
        showList()
        fullNameDel = input(" Full Name :")
        fileStudent =open("file.txt","r")
        list_Sv = fileStudent.read().split("\n")
        if fullNameDel !="":
            for i in range(len(list_Sv)-1):
                list_Sv_new=list_Sv[i].split("-")
                if list_Sv[0] == fullNameDel:
                    del list_Sv[i]
                    print("x--> Delete success")
                    flag=1
            if flag == 0 :
                print (" No Students found")
        else:
            print("request to enter information")   
        fileStudent.close()                     
    suluachon ={
          1: addStudent,
          2: delete,
          4: seach,
          3: showList
        }
    suluachon.get(Select ,lambda :" Error")()
        
       

