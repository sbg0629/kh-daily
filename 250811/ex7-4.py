def func(food):
    for x in food:
        print(x)
    food.append("딸기") #딸기 추가 .
    food.append("수박")

# func(["사과","오렌지","바나나"])
fruits = (["사과","오렌지","바나나"])
func(fruits)

print(fruits)
func(fruits)