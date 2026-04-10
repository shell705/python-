# 对list切片，从1开始，4结束，步长1
my_list=[0,1,2,3,4,5,6]
result1=my_list[1:4]
print(result1)
# 对tuple进行切片,从头到尾，步长为1
my_tuple=(0,1,2,3,4,5,6)
result2=my_tuple[:]
print(result2)
# 对str切片，从头到尾，步长2
my_str="01234567"
result3=my_str[::2]
print(result3)
# 对str切片，从头到尾，步长-1
my_str="01234567"
result4=my_str[::-1]
print(result4)
# 对list切片，从3开始，1结束，步长-1
my_list=[0,1,2,3,4,5,6]
result5=my_list[3:1:-1]
print(result5)
# 对tuple进行切片,从头到尾，步长为-2
my_tuple=(0,1,2,3,4,5,6)
result6=my_tuple[::-2]
print(result6)
# 练习
str0="万过薪月，员序程马黑来，nohtyP学"
str1=str0[9:4:-1]
print(str1)
str2=str0.split("，")[1][::-1]
str3=str2.replace("来","")
print(str3)
