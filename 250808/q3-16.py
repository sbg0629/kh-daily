a = int(input("첫번째 수 입력하세요"))
b = int(input("두번째 수 입력하세요"))

print("원하는 연산자?")
x= input("+ * - / 하나 선택")

if x =="+":
  print("%d + %d = %d" %(a,b,a+b))
elif x == "-":
  print("%d - %d = %d" %(a,b,a-b))
elif x == "*":
  print("%d * %d = %d" %(a,b,a*b))
elif x == "/":
  print("%d / %d = %d" %(a,b,a/b))
else: 
  print("선택오류")




