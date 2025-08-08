a = input("숫자 입력하세요")

# 파이썬 에서 len은 객체의 길이를 구하는 함수

if len(a)==1:
    print("한자리")
elif len(a) == 2:
    print("두자리수")
elif len(a) == 3:
    print("세자리수")
else:
    print("범위 벗어남0 ~ 999")

# num >=0 and num <= 9 0~과9사이
# num >=10 and num <= 99 10~과99사이
# num >=100 and num <= 999 100~과999사이
