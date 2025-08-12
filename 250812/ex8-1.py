class Person: #사람이나 사물이 될 수 있는 틀/판
    name = " 김정연" #name : 속성
    # Person1객체를 self가 받음
    def hello(self): #hello 메소드 호출 될 떄 객체를 self 받음
        # print("안녕하세요")
        print(Person.name + " 님 안녕하세요")

# ┌─참조 변수
person1 = Person() #객체 생성
person1.hello() #메소드 호출

Person.name =" 황서영"
person1.hello() #메소드 호출