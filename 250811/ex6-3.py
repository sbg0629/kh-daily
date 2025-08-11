# ┌─ 딕셔너리 키:값 , 키:값
member = {"name":"황예린","age":22,"emile":"yerin@hanmail.net"}
print(member)

# ┌─dict 사용해서 리스트, 튜플을 사용해서 딕셔너리 생성
score = dict ([("국어",80),("영어",90),("수학",100)])
print(score)

# ┌─키를 사용해서 값을 출력했다.
print(score["국어"]) 
print(score["영어"])
print(score["수학"])

# ┌─추가 됌
score["음악"]=70
print(score)

# ┌─값이 77로 변경.
score["수학"]=77
print(score)