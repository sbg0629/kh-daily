# ┌─*args를 사용하여 여러 개의 입력을 받을 수 있음
def average(*args):
    # print(args)#튜플 형식으로 출력됌
    num_args= len(args)
    sum = 0 
    for i in range(num_args):
        sum+=args[i]
    print(sum)
    avg = sum/num_args
    # print(avg)
    print("%d 과목 평균: %.1f"%(num_args,avg))

average(85,96,87)
average(85,96,87,97,72)

#위에 함수 기능만 하나 만들어두면 편하게 할 수 있음.