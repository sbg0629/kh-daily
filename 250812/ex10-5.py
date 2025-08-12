import os 

if os.path.exists("scores2.txt"): #scores2파일이 존재하는가
    os.remove("scores2.txt") #존재하면 삭제
    print("삭제 완료")
else:
    print("파일이 존재 하지 않음!") #존재하지 않으면 출력
