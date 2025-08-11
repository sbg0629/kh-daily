def even_odd(n):
    if n%2==0:
        print("%d은 짝수이다"%n)
    else:
        print("%d는 홀수이다"%n)

# even_odd(7)
# x= nput("양의 정수를 입력하세요: ") 타입 오류
x= int(input("양의 정수를 입력하세요: "))
even_odd(x)

