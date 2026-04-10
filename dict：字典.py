my_dict1={"跳蚤":665,"主任":663,"东东":619}
my_dict2={}
my_dict3=dict()
print(f"字典1内容是{my_dict1},类型是{type(my_dict1)}")
print(f"字典2内容是{my_dict2},类型是{type(my_dict2)}")
print(f"字典3内容是{my_dict3},类型是{type(my_dict3)}")
# key不能重复，保留新的
score=my_dict1["跳蚤"]
print(score)
# key可以是除字典外任意数据类型，value无限制
# 定义嵌套字典
stu_score_dict={
    "跳蚤":{"语文":125,"数学":135,"英语":148},
    "洲洲":{"语文":105,"数学":129,"英语":137}
}
score1=stu_score_dict["洲洲"]["英语"]
print(f"洲洲的英语分数是{score1}")
# 常用操作
my_dict1["思慎"]=619
my_dict1["跳蚤"]='北大'
print(my_dict1)
# 删除元素
score=my_dict1.pop("思慎")
print(f"删除{score}后结果为{my_dict1}")
# 获取全部key完成遍历
keys=my_dict1.keys()
print(keys)
for key in keys:
    print(f"字典的key是{key}")
    print(f"字典的value是{my_dict1[key]}")
# 法2
for key in my_dict1:
    print(f"字典的key是{key}")
    print(f"字典的value是{my_dict1[key]}")
# 统计元素数量
print(len(my_dict1))
# 练习
dictionary={
    "A":{"部门":"科技部","工资":3000,"级别":1},
    "B": {"部门": "市场部", "工资": 5000, "级别": 2},
    "C": {"部门": "市场部", "工资": 7000, "级别": 3},
    "D": {"部门": "科技部", "工资": 4000, "级别": 1},
    "E": {"部门": "市场部", "工资": 6000, "级别": 2}
}
print(dictionary)
for m in dictionary:
    level=dictionary[m]["级别"]
    if level==1:
        dictionary[m]["级别"]=2
        dictionary[m]["工资"]=dictionary[m]["工资"]+1000
print(dictionary)