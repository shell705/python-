def test_func(compute):
    result=compute(5,3)
    print(result)
    print(type(compute))
def compute1(x,y):
    return x+y
def compute2(x,y):
    return x-y
test_func(compute1)
test_func(compute2)
