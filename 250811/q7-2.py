# def num():
#     if args == 1:
#         result = a+b
#         return print("%d + %d = %d" %(a,b,result))
#     elif args == 2:
#         result = a-b
#         return print("%d - %d = %d" %(a,b,result))
#     elif args == 3:
#         result = a*b
#         return print("%d * %d = %d" %(a,b,result))
#     else:
#         result = a/b
#         return print("%d / %d = %d" %(a,b,result))


# args = int(input("원하는 연산을 입력하세요"))
# # r = args()
# a = int(input("첫번쨰 수를 입력하세요"))
# b = int(input("두번째 수를 입력하세요"))
# result = num()
# # print()

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

print("-1선택 옵션")
print("1.더하기")
print("2.빼기")
print("3.곱하기")
print("4.나누기")

choice = input("원하는 연산을 입력하세요 ")
num1 = int(input("첫 번째 수를 입력하세요"))
num2 = int(input("두 번째 수를 입력하세요"))
print()

if choice == "1":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == "2":
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice == "3":
    print(num1,"*",num2,"=",mult(num1,num2))
elif choice == "4":
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("입력오류")