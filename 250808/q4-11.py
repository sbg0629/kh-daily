num = input("숫자를 입력하세요")
print(num)
count = 0
for number in num:
    if int(number) % 2 != 0:
        count += 1
print("홀수의 개수" ,count)
    