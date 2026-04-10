i=0
while i<100:
    print("重复100次")
    i+=1

s=0
i=1
while i<=100:
    s+=i
    i+=1
print(s)

import random
num=random.randint(1,10)
flag=True
while flag:
    guess_num=int(input("猜测数字"))
    if guess_num!=num:
        print("猜错了")
        if guess_num<num:
            print("太小了")
        else:
            print("太大了")
    else:
        print("猜对了")
        flag=False