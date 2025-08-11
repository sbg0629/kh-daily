def cir_area():
    result = r*r*3.14
    return result

def cir_length():
    result = 2*r*3.14
    return result

# r = 10
r = int(input("반지름을 입력하세요"))
area=cir_area()
# print(area)
length = cir_length()
print("원의 면적:%.1f , 원주의 길이: %.1f" %(area,length))
