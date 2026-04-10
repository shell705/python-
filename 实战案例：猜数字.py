import random
num=random.randint(1,10)
first_guess=int(input("第一次猜测"))
if first_guess!=num:
    print("第一次猜错")
    if first_guess>num:
        print("太大了")
    else:
        print("太小了")
    second_guess=int(input("第二次猜测"))
    if second_guess!=num:
        print("第二次猜错")
        if second_guess>num:
            print("太大了")
        else:
            print("太小了")
        third_guess=int(input("第三次猜测"))
        if third_guess != num:
            print("第二次猜错")
            if third_guess > num:
                print("太大了")
            else:
                print("太小了")
            print(f"答案是{num}")
        else:
            print("第三次猜对")
    else:
        print("第二次猜对")
else:
    print("第一次猜对")