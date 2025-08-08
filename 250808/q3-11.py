a = int(input("필기시험 점수를 입력하세요"))
b = int(input("실기시험 점수를 입력하세요"))

c = a+b

print("%d + %d = %d"%(a,b,c))
if c % 3 == 0:
    print("%d는 3의 배수 입니다"%c)
else:
    print("%d는 3의 배수가 아니다"%c)


    # 나눴을 때 나머지가 0이면 그 수에 배수이다