for num in range(2, 1001):
    is_prime = True
    # 只检查到平方根，减少循环次数
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)