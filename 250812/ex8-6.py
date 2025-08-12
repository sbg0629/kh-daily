class Person:
    def __init__(self,name):
        # ┌─pass는 동작없이 다음 실행
        # pass 
        self.name = name 
        
    def show_name(self):
        print(self.name)

class Student(Person): #Person 클래스(부모)를 상속받은 student 클래스 (자식)
    pass

x = Student("홍")
x.show_name()