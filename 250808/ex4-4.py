for i in range(1,11):
    #print(i,end= " ") #출력 끝에 공백 문자 하나를 추가합니다
                        #엔터 대신에 스페이스 

    print(i, end = "777")
# print('') #''작은 따옴표는 enter역할
# print("") #"" 큰 따옴표도 enter역할
print() #공백도 엔터 역할
for i in range(10): #초기 값 0에 10-1(9)까지
    print(i,end = " ")

print()

for i in range(1,10,2): #2씩 증가 하면서 10-1까지 나옴
    print(i,end = " ")


print()
for i in range(20,0,-2): #2씩 감소 하면서 시작값20에서 2까지
    print(i,end = " ")

print()
for i in range(20,-1,-2): #2씩 감소 하면서 시작값20에서 0까지
    print(i,end = " ")