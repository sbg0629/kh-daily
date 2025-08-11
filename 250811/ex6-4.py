car = {"brand":"현대","model":"아반떼","start":1990,"year":2021}
print(car)
# ┌─

# ┌─pop: 키에 해당돠는 값을 잘라냄
x = car.pop("start")
print(x)
print(car)


car.clear()
print(car)