class Members:
    def __init__(self,name,age): 
        self.name = name
        self.age = age    #파라미터 두개를 받아와서 각각의 속성에 넣음
       
    
    def show_info(self): #self는 기본
        print("이름: ",self.name)
        print("나이 : ",self.age)

# ┌─TypeError: Members.__init__() missing 2 required positional arguments: 'name' and 'age 
# 값이 없어서 오류
# Member1 = Members()

Member1= Members("황선영",18) 
Member1.show_info()

Member2= Members("최종화",32) 
Member2.show_info()
