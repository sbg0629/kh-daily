import csv

file_name = "weather.csv"
f = open(file_name,"r",encoding='utf-8')

lines = csv.reader(f) #csv파일 전체를 읽어 옴

for line in lines:
    print(line,)

f.close()
