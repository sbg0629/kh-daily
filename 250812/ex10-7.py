import json

member = {"id":"swhong","name":"홍성우","age":"23","history":[{"date":"2025-08-12","route":"mobile"},
                                                           {"date":"2025-07-12","route":"pc"}]}

# ㄴdumps : member 딕셔너리의 json으로 인코딩
# ensure_ascill=false -> 아스키 형태로 저장하지 말라
# indent=4 = 4칸 들여쓰기
json_string = json.dumps(member,ensure_ascii=False,indent=4)
print(json_string)