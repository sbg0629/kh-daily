file_numes = ["file1.py","file2.txt","file3.pptx","file4.doc"]

for i in file_numes:
   arr = i.split(".")
   print("%s => 파일명은 %s , 확장자: %s"%(i,arr[0],arr[1]))

