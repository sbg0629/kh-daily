
count = 0
for i in range(200,800):
    if i % 5 != 0:
        print(i , end = " ")
        count +=1
        if count % 10 ==0:
            print()


