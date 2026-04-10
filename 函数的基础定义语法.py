#函数的定义
def random_number(a,b):
    import random
    num = random.randint(a,b )
    print(f"随机数{num}")
random_number(1,10)
def add(x,y):
    result=x+y
    print(f"{x}和{y}的和是{result}")
add(3,5)
#练习
def temp(t):
    if t<=37.3:
        print("体温正常，可以进入")
    else:
        print("体温过高，立即处决")
t=float(input("测量体温"))
temp(t)