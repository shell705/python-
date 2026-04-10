def list_while_func():
    list1=[1,2,3,4,5]
    index=0
    while index<len(list1):
        element=list1[index]
        print(element)
        index+=1
list_while_func()
def list_for_func():
    list2=[1,2,3,4,5]
    for m in list2:
        print(m)
list_for_func()
list0=[1,2,3,4,5,6,7,8,9,10]
list3=[]
for num in list0:
    if num%2==0:
       list3.append(num)
print(list3)