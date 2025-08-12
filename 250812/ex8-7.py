class Person:
    def __init__(self,name):
        self.name = name 
        
    def show_name(self):
        print(self.name)

class Student(Person): 
    def show_name(self): #오버라이딩 
        print("환영합니다.")
        print(self.name + "님 반갑습니다")

x = Student("홍")
x.show_name()