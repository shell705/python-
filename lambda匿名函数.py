# 无名称的函数，只可使用一次
def test_func(compute,a,b):
    result=compute(a,b)
    print(result)
    print(type(compute))
test_func(lambda x,y:x+y,5,3)   # 定义匿名函数，默认有返回值
test_func(lambda x,y:x-y,8,3)