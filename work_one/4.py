list=[1,6,9,4,"hello","嗨嗨害"]
list_1=[]
for i in list:
    if isinstance(i,int) is False:
        pass
    else:
        list_1.append(i)
for t in range(len(list_1)):
    for n in range(t+1,len(list_1)):
        if list_1[t]>list_1[n]:
            list_1[t],list_1[n]=list_1[n],list_1[t]
print(list_1)            