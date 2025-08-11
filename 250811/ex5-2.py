color = ['빨강','주황','노랑','초록','파랑','남색','보라']

# print(color[0]) #빨강
# print(color[5]) #남색
# print(color[2:6]) #노 초 파 남
# print(color[-3]) #파란색
# print(color[-4:-1]) #초록 파랑 남색  

# for co in color:
#     print("나는 %s을 좋아한다."%co)

n = len(color)
# print(n) #7

for i in range(0,n): #0~6
    # print(i)
    print("나는 %s을 좋아한다."%color[i])
    