class Cat:
    #┌─속성이 3개
    kor_name = "로키"
    eng_name = "rocky"
    age = 2

    #┌─메소드 2개
    def sound(self):
        print("야옹~!~")
    def speed(self):
        print("엄청 빠르다!")

mycat = Cat() #mycat 객체 생성
print("한글이름 : ",mycat.kor_name) #객체의 속성을 출력
print("영어이름 : ", mycat.eng_name) #객체의 속성을 출력
print("나이 : ",mycat.age) #객체의 속성을 출력

mycat.sound() #객체의 메소드로 출력
mycat.speed() #객체의 메소드로 출력