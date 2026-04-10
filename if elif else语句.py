height=int(input("输入身高(cm):"))
vip_level=int(input("输入vip级别"))
date=int(input("今天的日期是："))
if height<120:
    print("您身高小于120cm，可以免费游玩")
elif vip_level>3:
    print("您的vip等级大于三，可以免费游玩")
elif date==1:
    print("今天是一号免费日，可以免费游玩")
else:
    print("请支付门票")
print("祝您游玩愉快")
#简化：
if int(input("输入身高："))<120:
    print("您的身高小于120cm，可以免费游玩")
elif int(input("输入vip级别"))>3:
    print("您的vip级别大于3，可以免费游玩")
elif int(input("今天的日期是："))==1:
    print("今天是一号免费日，可以免费游玩")
else:
    print("请支付门票")
print("祝您游玩愉快")