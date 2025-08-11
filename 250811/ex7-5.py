# def func(n): 
def func(): 
    # x = n+5
    # print(x)
    # return x
    global x
    x = 100 #지역 변수 : 함수내에서만 사용 가능
    print(x)

# func(10)
# a = func(10) #return값이 없을때 none이다
# print(a)

x=200
print(x)
func()
print(x)
# 200
# 100
# 200

# global
# 200
# 100
# 100
