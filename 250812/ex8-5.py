class Members:
    total = 0 #클래스 속성

    def __init__(self,name,phone): 
        self.name = name    #객체 속성
        self.phone = phone    
        # Members.total += 1       
        self.total += 1       
    
    def show_info(self): #self는 기본
        print("이름: %s , 전화번호는: %s"%(self.name, self.phone))
        
Member1= Members("황선영","010-1111-2222") 
Member2= Members("강동욱","010-1111-3333") 
Member3= Members("신진서","010-1111-4444") 

Member1.show_info()
Member2.show_info()
Member3.show_info()

# print("총 회원 수 : ",Member1.total)
# print("총 회원 수 : ",Member2.total)
# print("총 회원 수 : ",Member3.total)
print("총 회원 수 : ",Members.total)
