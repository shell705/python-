# 法1
f=open("D:/tools/python learning/test7/文件的读取测试.txt","r",encoding="UTF-8")
including=f.read()
num=including.count("and")
print(f"and在文件中出现了{num}次")
f.close()
# 法2
f=open("D:/tools/python learning/test7/文件的读取测试.txt","r",encoding="UTF-8")
count_and=0
for line in f:
    line=line.strip()
    words=line.split(" ")
    for word in words:
        if word=='and':
            count_and+=1
print(f"and在文件中出现了{count_and}次")
