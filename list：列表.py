# 列表的定义
def_list=['元素1','元素2','元素3',1,2,3,True]
print(def_list)
print(type(def_list))
#定义空列表
list_name=[]
list_name2=list()
# 嵌套列表
list2=['666',def_list]
print(list2)
#列表的下标索引
print(def_list[2])
print(def_list[-1])
print(list2[1][1])
# 列表的常用操作
#查找
index=def_list.index('元素1')
print(f"元素1在列表中的下标索引值为{index}")
# index=def_list.index('元素n')
# print(index)
#修改元素
def_list[1]='新元素'
print(f"修改后的列表为{def_list}")
#插入元素
def_list.insert(1,'新元素2')
print(def_list)
#追加元素
def_list.append(False)
print(def_list)
def_list.extend([4,5,6])
print(def_list)
#删除元素
del def_list[3]
print(def_list)
element=def_list.pop(2)
print(f"取出元素{element}后，列表为{def_list}")
def_list.remove('新元素2')
print(def_list)
#清空列表
def_list.clear()
print(def_list)
new_list=(1,1,2,3,3,4,3)
num=new_list.count(3)
print(f"新列表中有{num}个元素3")
count=len(new_list)
print(f"新列表中有{count}个元素")