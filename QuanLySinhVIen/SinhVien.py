class People :
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    #@property   #bien method thành thuộc tính
    def Output(self):
      return '{}'.format(self.age)


