# temp = {"월":15.5,"화":17.0,"수":16.2,"목":12.9,"금":11.0,"토":10.5,"일":13.3}

# print("------------------------")
# for key in temp.keys():
#     print(key,end="   ")

# print("------------------------")
# for values in temp.values():
#     print(values,end=" ")
# print()
# print("------------------------")


# print("numbers[::-1] = ", numbers[::-1]) # (20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10)



temp = {"월":15.5,"화":17.0,"수":16.2,"목":12.9,"금":11.0,"토":10.5,"일":13.3}

print("-"*70)
print("월   화   수   목   금   토   일")
print("-"*70)

for key in temp:
    print(temp[key],end= " ")

print()
print("-"*70)

