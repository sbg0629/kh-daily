# def a(string):
#     result = string.replace(" ","-")
#     return result

# text = input("문장을 입력하세요")
# str = a(text)
# print(str)

def space_hyphen(string):
    result = ""
    i = 0
    while i<len (string):
        if string[i] == " ":
            result+="-"
        else:
            result+= string[i]
        i+=1
    return result

string = input("문자열을 입력하세요")
print(space_hyphen(string))


