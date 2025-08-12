import json

member = {"id":"swhong","name":"홍성우","age":"23","history":[{"date":"2025-08-12","route":"mobile"},
                                                           {"date":"2025-07-12","route":"pc"}]}
    
    # dump(): 딕셔너리를 json 파일로 생성
with open("member.json","w",encoding="utf-8") as f:
    json.dump(member,f,ensure_ascii=False,indent=4)
