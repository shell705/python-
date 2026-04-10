"""
函数说明
:param x:形参x的说明
:param y:形参y的说明
:return:返回值的说明
"""
def add(x,y):
    """
    接收两个参数，进行两个数相加
    :param x:第一个加数
    :param y: 第二个加数
    :return: 和
    """
    result=x+y
    print(f"{x}和{y}的和是{result}")
    return result
add(5,6)