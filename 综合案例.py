f=open("D:/tools/python learning/test7/综合案例测试.txt","r",encoding="UTF-8")
g=open("D:/tools/python learning/test7/bill备份.txt.bak","a",encoding="UTF-8")
for line in f:
    line = line.strip()
    word = line.split(",")[4]
    if word =="正式":
        g.write(f"\n{line}")
f.close()
g.close()
# 重复运行前先删掉测试文件