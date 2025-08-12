# utf-8 서계표준 문자셋 (ex>ms949,euc-kr,iso9000번대)
# f = open("new_file.txt","w",encoding="utf-8") # w는 파일을 씀

# for name in names:
#     f.write(name+"\n") #줄 바꿈 추가 

# names =["홍지수","안지용","김연수","이예림","이지은"]


# f = open("new_file2.txt","w",encoding="utf-8")
# f.write("테스트~~")



f = open("new_file3.txt","a",encoding="utf-8") #a 는 추가 

names =["홍해해","안지응","김홍구","이은지","이지예"]
for name in names:
    f.write(name+"\n") #줄 바꿈 추가 


#공통 
print("파일 쓰기 완료!")

f.close()
