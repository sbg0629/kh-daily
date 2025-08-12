class Arge:
    def __init__(self,width,width1,height):
        self.width = width
        self.width1 = width1
        self.height = height
    def area(self):
            return (self.width + self.width1)/2*self.height
        
w = int(input("사다리꼴의 윗변을 입력하세요: "))
w1 = int(input("사다리꼴의 밑변을 입력하세요: "))
h = int(input("사다리꼴의 높이을 입력하세요: "))

t1 = Arge(w,w1,h)
print("사다리꼴의 면적는? %.2f" % t1.area())