#局部变量
#num1=0
def test_a():
    global num1
    num1=100
    print(num1)
test_a()
#全局变量
num2=200
def test_b():
    print(num2)
print(num2)
test_b()
print(num1)