# NameError: name 'x' is not defined
# print(x)

try:
    print(x)
except NameError: #파이썬 시스템 오류 대신에 메시지로 처리
    print("변수가 정의되지 않아 오류가 발생함요")
