# def tup1(*args):
#     num_sum=len(args)
#     sum = 0
#     for i in range(num_sum):
#         sum+=args[i]
#     print("튜플의 합은:",sum)

# tup1(10,20,30,40,50)

def sum_tup(numbers):
    total=0

    for number in numbers:
        total+=number

    return total

tup1=(10,20,30,40,50)
total = sum_tup(tup1)

print("튜플의 합계 : ",total)

