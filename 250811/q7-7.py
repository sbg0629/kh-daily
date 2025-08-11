# def num(x):
#     for i in range(x+1):
#         result = i*i
#         i+=1
#         print(result ,end=" ")
#     return result


# n = int(input("n값을 입력하세요"))
# a = num(n)
# print(a)



def num(x):
    list_new = []


    for i in range(1,x+1):
        list_new.append(i**2)
    return list_new

n = int(input("n값을 입력하세요"))
a = num(n)
print(a)