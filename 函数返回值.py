def add(a,b):
    result=a+b
    return result
r=add(1,3)
print(r)
#None类型
def say_hi():
    print("hello")
result1=say_hi()
print(f"返回内容{result1}")
print(f"返回值类型为{type(result1)}")
def say_hi():
    print("hello")
    return None
result2=say_hi()
print(f"返回内容{result2}")
print(f"返回值类型为{type(result2)}")
#if判断中None等于False
def check_age(age):
    if age>18:
        return"Success"
    else:
        return None
result=check_age(19)
if not result:
    print("未成年禁止进入")
else:
    print("欢迎光临")