print("-" * 30)
print("섭씨      화씨")
print("-" * 30)

for c in range(-20,31,5): #c는 섭씨
    f = c * 9.0/5.0+32.0 #f 화씨 구하는 공식
    # print("%d %f" %(c,f))
    print("%5d %6.1f" %(c,f)) 
    #ㄴd5자리 쓰고 소수 1까지 나오고 6자리 쓴다
print("-" * 30)