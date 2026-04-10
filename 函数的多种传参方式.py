# 位置参数
def user_info(name,age,gender):
    print(f"姓名:{name}，年龄:{age}，性别:{gender}")
user_info('shell',18,'男')
# 关键字传参（可以与位置参数混用）
user_info(name='贝壳',gender='男',age=18)
user_info('洲洲',gender='男',age=18)
# 缺省参数（默认参数必须在最后）
def user_info(name,age,gender='男'):
    print(f"姓名:{name}，年龄:{age}，性别:{gender}")
user_info(name='钍',gender='女',age=18)
user_info(name='洲洲',age=18)
# 不定长参数（默认为元组形式）
def user_info1(*args):
    print(args)
    print(type(args))
user_info1('shell')
user_info1('shell',18)
user_info1('shell',18,'男')
# （默认为字典）
def user_info2(**kwargs):
    print(kwargs)
    print(type(kwargs))
user_info2(name='贝壳',gender='男',age=18)
