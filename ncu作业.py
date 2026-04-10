def str_replace(string,positions):
    list_string=list(string)
    for pos in positions:
        list_string[pos]="*"
    string1=''.join(list_string)
    return string1
dict1={"H01":["张三","13812345678","zhang12@163.com","360101199001098254"],
       "H02":["李四","13966677788","lisi88@sina.com","110101197507225238"],
       "H03":["赵小五","13543216654","zhao@qq.com","210101200704187168"]}
print("**************************\n用户信息:")
num=input(str("编号:"))
name=dict1[num][0]
phone=dict1[num][1]
mail=dict1[num][2]
identity=dict1[num][3]
phone=str_replace(phone,[3,4,5,6])
identity=str_replace(identity,[6,7,8,9])
if mail==dict1["H01"][2]:
    mail="zh*****@***.com"
elif mail==dict1["H02"][2]:
    mail="li****@****.com"
elif mail==dict1["H03"][2]:
    mail="zh**@**.com"
print(f"姓名:{name}")
print(f"电话:{phone}")
print(f"邮箱:{mail}")
print(f"身份证号码:{identity}")
print("**************************")