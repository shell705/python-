import time
def square_root_1(c):
    i=g=0
    for j in range(0,c+1):
        if j*j>c and g==0:
            g=j-1
        while abs(g*g-c)>0.000001:
            g+=0.0000003
            i+=1
            print("%d:g=%.10f"%(i,g))
c=int(input("数字"))
t1=time.time()
square_root_1(c)
t2=time.time()
print(f"耗时{t2-t1}秒")