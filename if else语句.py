age=input("输入年龄")
print(f"我今年{age}岁")
age=int(age)
if age>=18:
    print("我已成年")
    print("已经高中毕业")
else:
    print("我还未成年")
#作业
height=input("请输入身高(cm):")
height=int(height)
if height>120:
    print("您的身高超出120cm，需要购票")
else:
    print("您的身高未超过120cm，可以免费游玩")
print("祝您游玩愉快")