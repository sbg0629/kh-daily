class Members:
    def set_into(self,name): #self는 기본 name 추가
        self.name = name #(self.name)객체의 속성에다가 파라미터를 받음
        print(name)
    
    def show_info(self): #self는 기본 
        print("이름: ",self.name)

Member1 = Members() #객체 생성
Member1.set_into("홍지수") #2번에 name으로 들어가서 3번에 속성에 저장되고 4번으로 출력
Member1.show_info()

Member2 = Members() #객체를 여러개 생성 가능 
Member2.set_into("안지영")
Member2.show_info()
