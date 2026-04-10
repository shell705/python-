name_list = [
    "张伟",
    "李娜",
    "王磊",
    "陈俊宇",
    "杨雨欣"
]
for name in name_list:
    print("I want to invite {} to come to my party".format(name))
cannot_come=name_list.pop(0)
print("{} can't come to my party".format(cannot_come))
name_list.insert(0,"熊娜")
for name in name_list:
    print("I want to invite {} to come to my party".format(name))
print("I find a bigger tabie")
name_list.insert(0,"钱哥")
name_list.insert(4,"丽萨")
name_list.append("老龙")
for name in name_list:
    print("I want to invite {} to come to my party".format(name))
print("I can only invite two people to my party")

while len(name_list)>2:
    removed_people=name_list.pop()
    print("Sorry,I cannot invite {} to my party".format(removed_people))
del name_list[0]
del name_list[0]
print(name_list)