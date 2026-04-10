# 定义一个变量，用来记录余额
money=50
#通过print语句，输入变量记录的内容
print("余额还有：", money)
#物品定价
icecream=5
drink=3
#购买数量
m=2
n=4
#计算余额
change=money-icecream*m-drink*n
print("买了",m,"个冰淇淋，",n,"瓶饮料剩余：",change,"元")
change_type=type(change)
print(change_type)