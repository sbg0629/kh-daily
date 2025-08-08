score = int(input("정수를 입력하세요 :"))

if score >=90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
    
    # print("등급: ",grade) 
    # 들여쓰기 떄문에 else에 포함 되어 있다.
print("등급: ",grade)
    
