print("기능선택")
print("1 더하기")
print("2 빼기")
print("3 곱하기")
print("4 나누기")

a = input("계산 기능을 선택하세요 1/2/3/4")
b = int(input("첫번째 수 입력하세요"))
c = int(input("두번째 수 입력하세요"))


if a =="1":
  print("%d + %d = %d" %(b,c,b+c))
elif a == "2":
  print("%d - %d = %d" %(b,c,b-c))
elif a == "3":
  print("%d * %d = %d" %(b,c,b*c))
elif a == "4":
  print("%d / %d = %d" %(b,c,b/c))
else: 
  print("선택오류")




