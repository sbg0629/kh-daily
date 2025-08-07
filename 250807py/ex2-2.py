"""
큰 따옴표 3개 주석.
# input("당신의 이름은?")
"""
name = input("당신의 이름은?")
# birth = input("당신의 태어난 해?") 숫자를 입력해도 문자로 받음

birth = int(input("당신의 태어난 해?") )
age = 2025 - birth
''' 작은 따옴표 3개로 범위 주석.
# age = 2025 - birth #오류 : 'int' and 'str' -> int로 변환해서 오류 해결.
# # print("%d님" %name) #%d로 인해 not str
# # print("%s님" %name) #%s는 문자열을 받음.
# # print("%s님이 태어난 해는 %d" %(name,birth)) #오류 남 birth가 문자열로 받아드려서
# # print("%s님이 태어난 해는 %s" %(name,birth)) 
# # print("%s님이 태어난 해는 %s" %(name,age)) xx
'''
print("%s님이 태어난 해는 %d" %(name, age))






