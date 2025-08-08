# a = input("문장을 입력해주세요")
# x = 0

# b = a.replace(" ","-")
# print(b)
    

# while b >= 0:
#     print(a[x])
#     i -= 1
# # for b in reversed(a):
# #     print(b)
    



# # you mean everything to me.


sentence = input("문장을 입력 ")
i = len(sentence) - 1 
while i >=0:
    if sentence[i] == " ":
        print("-",end="")
    else:

        print(sentence[i],end='')
    i -=1
    
        