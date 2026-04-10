# 不支持元素重复且无序
my_set={"shell","ETO","PDC","PIA","面壁者","执剑人","ETO"}
print(my_set)
empty_set=set()
print(empty_set)
# 修改
# 添加
my_set.add("罗辑")
my_set.add("PDC")   # 重复元素无效添加
print(f"添加元素后，结果是{my_set}")
# 删除
my_set.remove("罗辑")
print(f"移除元素后，结果是{my_set}")
element=my_set.pop()
print(f"取出随机元素{element}后结果是{my_set}")
# 清空
my_set.clear()
print(f"清空后结果是{my_set}")
# 求差集
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
print(set3)
# set1.difference_update(set2)
# print(set1)
# print(set2)
set4=set1.union(set2)
print(f"set4={set4}")
# 遍历（只能用for）
for element in set4:
    print(f"集合的元素有：{element}")
# 练习
my_set=set()
my_list=["shell","ETO","PDC","PIA","面壁者","执剑人","ETO"]
for element in my_list:
    my_set.add(element)
print(my_set)
