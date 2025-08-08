phone = input("하이픈(-)을 포함한 휴대폰을 입력" )

for x in phone:
    if x != "-": #하이픈이 아닐 때 출력
        # print(x) #숫자 하나하나 엔터 
        print(x,end ="") #숫자 다 붙임