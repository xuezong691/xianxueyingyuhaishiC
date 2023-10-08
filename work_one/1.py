#第一种
a=int(input("第一个整数："))
b=int(input("第二个整数："))
c=int(input("第三个整数："))
num_max=max(a,b,c)
if num_max==a:
    num_1=a
    num_max=max(b,c)
    if num_max==b:
        num_2=b
        num_3=c
    if num_max==c:
        num_2=c
        num_3=b    
if num_max==b:
    num_1=b
    num_max=max(a,c)
    if num_max==a:
        num_2=a
        num_3=c
    if num_max==c:
        num_2=c
        num_3=a
 
if num_max==c:
    num_1=c
    num_max=max(b,a)
    if num_max==b:
        num_2=b
        num_3=a
    if num_max==a:
        num_2=a
        num_3=b 
print(num_1,num_2,num_3)



#第二种
a=int(input("随便一个整数"))
b=int(input("随便一个整数"))
c=int(input("随你便一个整数"))
def bidaxiao(x,y):
    if x>y:
        return True
    else:
        return False
if bidaxiao(a,b) is True:
    num_1=a
    num_2=b
    if bidaxiao(a,c) is False:
        num_0=c
        print(num_0,num_1,num_2)
    elif bidaxiao(b,c) is True:
        num_3=c
        print(num_1,num_2,num_3)
    else:
        num_15=c
        print(num_1,num_15,num_2)    

else:
    num_1=b
    num_2=a   
    if bidaxiao(b,c) is False:
        num_0=b
        print(num_0,num_1,num_2)
    elif bidaxiao(a,c) is True:
        num_3=c
        print(num_1,num_2,num_3)
    else:
        num_15=c 
        print(num_1,num_15,num_2)   



#第三种
a=int(input("第一个整数："))
b=int(input("第二个整数："))
c=int(input("第三个整数："))
list_1=[a,b,c]
for t in range(len(list_1)):
    for n in range(t+1,len(list_1)):
        if list_1[t]<list_1[n]:
            list_1[t],list_1[n]=list_1[n],list_1[t]
print(list_1)                 
