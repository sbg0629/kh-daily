phone_list1 = ["010-1111-2222","010-2222-3333","010-3333-4444"]
print(phone_list1)

phone_list2 =[]

for numer in phone_list1:
    # print(numer)
    x = numer.replace("-","")
    phone_list2.append(x)
    
    
print(phone_list2)