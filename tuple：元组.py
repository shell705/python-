# 元组一旦定义完成，不可修改
# 元组的定义
t1=(1,"hello",True)
t0=tuple()
t00=()
print(f"t1的内容是{t1},类型是{type(t1)}")
# 定义单元素元组
t2=("good",)
print(f"t2类型是{type(t2)}")
t3=((1,2,3),t1)
print(f"t1的内容是{t3},类型是{type(t3)}")
element=t3[1][2]
print(element)
# 操作
t4=("shell","ETO","PDC","PIA",1,2,3,1,1,114514)
index=t4.index("ETO")
print(f"ETO的下标是{index}")
print(t4.count(1))
print(len(t4))
# 元组的遍历
def tuple_while_func():
    t5=(1,2,3,4,5)
    ind=0
    while ind<len(t5):
        ele=t5[ind]
        print(ele)
        ind+=1
tuple_while_func()
def tuple_for_func():
    t6=(1,2,3,4,5)
    for m in t6:
        print(m)
tuple_for_func()
# 特例:元组嵌套列表
t7=(1,2,["ETO","PDC"])
print(f"t7内容是{t7}")
t7[2][1]="PIA"
print(f"修改后t7内容是{t7}")