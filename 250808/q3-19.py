a = input("아이디는?")

if a == "admin":
    print("콘텐츠 이용 가능")
else: #어드민 아닐 떄 
    b = int(input("회원님의 레벨은1~9?")) 
    # ㄴ 다시 회원레벨을 받아옴
    if a<4 :
        print("콘텐츠를 이용가능")
    else:
        print("콘텐츠 이용 불가능")