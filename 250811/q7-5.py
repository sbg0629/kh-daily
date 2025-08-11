# def revers(x):
#     return x[::-1] #문자열 거꾸로 뒤집기



# text = input("문자열을 입력하세요")
# a = revers(text)
# print(a)

def str_revers(string):
    result = ""
    index = len(string)

    while index > 0:
        result += string[index - 1]
        index -=1
    return result

string = input("문자열을 입력하세여")
print(str_revers(string))