# num=int(input("请输入四位明文："))
# a=int(num/1000+5)%10
# b=int(num/100+5)%10
# c=int(num/10+5)%10
# d=int(num+5)%10
# print(f"密码：{c}{d}{a}{b}")
num=input("请输入四位明文：")
print(f"{(int(num[2])+5)%10}{(int(num[3])+5)%10}{(int(num[0])+5)%10}{(int(num[1])+5)%10}")