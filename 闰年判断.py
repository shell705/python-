year=int(input(f"输入年份值："))
if year%100!=0&year%4==0:
    print("是闰年")
elif year%400==0:
    print("是闰年")
else:
    print("不是闰年")