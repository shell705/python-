# 字符串是字符的容器，可以存放任意数量的字符(不可修改)
my_str="Shell wants to join ETO"
print(my_str[1])
print(my_str[-2])
target=my_str.index("ETO")
print(target)
# 字符串替换
my_str2=my_str.replace("ETO","PDC")
print(my_str)
print(my_str2)
# 字符串分割
_list=my_str.split(" ")
print(_list)
# 字符串规整操作(不传入参数既去除收尾空格)
new_str="12Shell wants to join ETO21"
new_str2=new_str.strip("12")
print(new_str2)
# count和len同list和tuple