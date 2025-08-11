animals = ("토기","거북이","사자","여우")
print(animals)

#튜플에서는 값을 변경 추가 할 수 없다
# animals[2] ="호랑이" #에러
# print(animals)

# numbers = tuple(range(10)) #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(numbers)

numbers = tuple(range(10,21)) #(10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(numbers)

print("numbers[0] = ", numbers[0]) #10
print("numbers[2:5] = ", numbers[2:5]) #(12, 13, 14)
print("numbers[2:] = ", numbers[2:]) #(12, 13, 14, 15, 16, 17, 18, 19, 20)
print("numbers[:5] = ", numbers[:5]) #(10, 11, 12, 13, 14)
print("numbers[-2] = ", numbers[-2]) #19
print("numbers[::-1] = ", numbers[::-1]) # (20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10)
# ㄴ::1 -> 맨뒤에서 맨 앞으로 출력 
