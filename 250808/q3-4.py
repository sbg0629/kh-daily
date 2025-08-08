g = int(input("주민번호 뒷 자리 첫 번째 숫자 입력하세요"))

if g == 1 or g == 3:
    print("남성입니다")
elif g == 2 or g == 4:
    print ("여성입니다")

else:
    print("다시 입력하세요.")
