my_list=[3,1,2,5,4]
my_tuple=(3,1,2,5,4)
my_str="badcfeg"
my_set={3,1,2,5,4}
my_dict={"key2":2,"key4":4,"key3":3,"key5":5,"key1":1}
# len元素个数
# 最大最小值
print(f"{type(my_list)}中最大元素是{max(my_list)},最小元素是{min(my_list)}")
print(f"{type(my_tuple)}中最大元素是{max(my_tuple)},最小元素是{min(my_tuple)}")
print(f"{type(my_set)}中最大元素是{max(my_set)},最小元素是{min(my_set)}")
print(f"{type(my_dict)}中最大元素是{max(my_dict)},最小元素是{min(my_dict)}")
print(f"{type(my_str)}中最大元素是{max(my_str)},最小元素是{min(my_str)}")
# 类型转换：容器转列表
print(list(my_list))
print(list(my_tuple))
print(list(my_str))
print(list(my_set))
print(list(my_dict))   # 保留key
# 容器转元组
print(tuple(my_list))
print(tuple(my_tuple))
print(tuple(my_str))
print(tuple(my_set))
print(tuple(my_dict))
# 容器转字符串
print(str(my_list))
print(str(my_tuple))
print(str(my_str))
print(str(my_set))
print(str(my_dict))
# 转集合
print(set(my_list))
print(set(my_tuple))
print(set(my_str))
print(set(my_set))
print(set(my_dict))
# 容器的通用排序功能
print(f"{type(my_list)}的排序结果是{sorted(my_list)}")
print(f"{type(my_tuple)}的排序结果是{sorted(my_tuple)}")
print(f"{type(my_str)}的排序结果是{sorted(my_str)}")
print(f"{type(my_set)}的排序结果是{sorted(my_set)}")
print(f"{type(my_dict)}的排序结果是{sorted(my_dict)}")

print(f"{type(my_list)}的反向排序结果是{sorted(my_list,reverse=True)}")
print(f"{type(my_tuple)}的反向排序结果是{sorted(my_tuple,reverse=True)}")
print(f"{type(my_str)}的反向排序结果是{sorted(my_str,reverse=True)}")
print(f"{type(my_set)}的反向排序结果是{sorted(my_set,reverse=True)}")
print(f"{type(my_dict)}的反向排序结果是{sorted(my_dict,reverse=True)}")
# 字符大小：基于ASCII码表，按位比较
print(f"abd大于abc,结果:{'abd'>'abc'}")