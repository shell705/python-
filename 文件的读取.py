f=open("D:/tools/python learning/test7/文件的读取测试.txt","r",encoding="UTF-8")
print(type(f))
# print(f"读取19字符：{f.read(19)}")
# print(f"读取剩余全部字节：{f.read()}")
# lines=f.readlines()    # 读取全部行,封装到列表中
# print(lines)
# print(type(lines))
line1=f.readline()
line2=f.readline()
line3=f.readline()
print(f"第一行：{line1}")
print(f"第二行：{line2}")
print(f"第三行：{line3}")
for line in f:
    print(f"下一行是:{line}")
import time
time.sleep(30)       # 暂停执行
f.close()      # 关闭文件