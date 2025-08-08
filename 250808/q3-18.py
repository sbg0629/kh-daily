a = int(input("시작 수는?"))
b = int(input("끝 수는?"))
c = int(input("정수는?"))


#c >a and a<b
if a<=c<=b: 
    #c가 a보다 크거나 같거나 b보다 작거나 같으면 사이에 있다
     
    print("%d는 %d~ %d 사이에 있다"%(c,a,b))
else:
    print("%d는 %d~ %d 사이에 없다"%(c,a,b))
    




