num=int(input("请输入数字"))
if int(input("猜测上面输入的数字"))!=num:
    if int(input("错了，再猜"))==num:
        print("终于猜对了")
    else:
        print("还是错的，有点用咯")
else:
    print("恭喜猜对")

if int(input("输入身高"))>120:
    print("身高超限")
    if int(input("输入vip等级"))>=3:
        print("尊贵的vip3用户可以免费游玩")
    else:
        print("请支付门票")
else:
    print("可以免费游玩")

age=int(input("输入年龄"))
if age>=18:
    print("你成年了")
    if age<30:
        print("年龄符合标准")
        if int(input("请输入入职时长"))>=2:
            print("恭喜你符合要求")
        elif int(input("输入你的级别"))>=3:
            print("你也符合要求")
        else:
            print("你的工龄和级别不够")
    else:
        print("你年纪太大了")
else:
    print("你年龄太小了")