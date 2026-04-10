n=1
while n<=100:
    print(f"表白第{n}天")
    n+=1
    i=1
    while i<=5:
        print(f"送{i}朵花")
        i+=1
print("第100天彻底成为小丑")
#案例:打印99乘法表
n=1
N=int(input())
while n<=N:
    m = 1
    while m<=n:
        print(f"{m}*{n}={m*n} \t",end='')
        m+=1
    n+=1
    print()