# nunber = [7,9,15,18,30,-3,7,12,-16,-12]
# list = nunber[1::2]
# sum =0
# i = 0
# while i < len(list):
#     sum += list[i]
#     i+=1
# print(sum)

nunber = [7,9,15,18,30,-3,7,12,-16,-12]

sum =0
i = 0

print("짝수 번쨰 요소 : ", end = "")
while i < len(nunber):
    if(i+1)%2 == 0:
        sum+=nunber[i]
        print(nunber[i],end=" ")
    i+=1

print()
print("합계",sum)
