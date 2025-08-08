a = int(input("필기시험 점수를 입력하세요"))
b = int(input("실기시험 점수를 입력하세요"))

# print("필기시험 점수%d"%a)
# print("실기시험 점수%d"%b)

# if a >= 80 and b >=80:
#     print("합격")
# else:
#     print("불합격")

# 두가지 방법

if a >= 80 and b >=80:
    result = "합격"
else:
    result = "불합격"

print("필기시험 점수%d" %a)
print("실기시험 점수%d" %b)
print("판정: %s" %result)
