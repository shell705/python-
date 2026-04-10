name="shell"
for x in name:
    print(x)
#案例
name="itheima is a brand of itcast"
num=0
for x in name:
    if x=="a":
        num+=1
print(f"这句话里有{num}个a")
#range语句
#语法1
for x in range(10):
    print(x)
#语法2
for x in range(3,10):
    print(x)
#语法3
for x in range(3,10,2):
    print(x)
#实用:快速确定执行次数
for x in range(10):
    print("送玫瑰花")
#案例:数偶数
num=0
for x in range(0,100):
    if x%2==0:
        num+=1
print(num)
