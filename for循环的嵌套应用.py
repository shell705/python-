day=0
for day in range(1,101):
    print(f"表白第{day}天")
    for flower in range(1,11):
        print(f"送第{flower}束花")
#练习
for n in range(1,10):
    for m in range(1,n+1):
        print(f"{m}*{n}={m*n}\t",end='')
    print()