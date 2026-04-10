age=input("输入年龄")
print(f"我今年{age}岁")
age=int(age)
if age>=18:
    print("我已成年")
    print("已经高中毕业")
if age<18:
    print("还未成年")
    if age>=15:
        print("在读高中")
    if 12<=age<15:
        print("在读初中")
    if age<12:
        print("在读小学")