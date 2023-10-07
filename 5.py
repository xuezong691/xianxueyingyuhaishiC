dict={"114514":"田所浩二","1023014181":"薛总"}
remove_the_keys=[]
for x in dict.keys():
    if x[-1] in {"1","3","5","7","9"}:
        remove_the_keys.append(x)
for y in remove_the_keys:
    del dict[y]     
print(dict)