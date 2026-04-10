#布尔类型
result=10>5
print(f"10>5的判断结果是 {result}",type(result))
result="shell"=="Shell"
print(f"Shell与shell是否等效 {result}",type(result))
result="shell"!="Shell"
print(f"Shell与shell是否不等效 {result}",type(result))
m=2016-2007
n=9
result=m>=n
print(f"2016-2007是否大于等于9 {result}")
num1=10
num2=10
num3=5
print(f"10==5*2的结果是{num1==num3*2}")
print(f"10!=10+5的结果是{num1!=num2+num3}")
#定义储存布尔类型的数据
bool_1=True
bool_2=False
print(f"bool_1变量的内容是：{bool_1}",f"类型是{type(bool_1)}")