x=str(input("随便写一串英文："))
list1=[]
if x.find("ol")==-1:
    print("海海害，没有ol哦")
else:    
  for string in x:
    if string=="o":
       list1.append("f")
       list1.append("z")
       list1.append("u")
    elif string!="l":
       list1.append(string)
  reverse=list(reversed(list1))
  result="".join(reverse)  
  print(result)


#pro

x=str(input("随便写一串英文："))
list1=[]
if x.find("ol")==-1:
    print("海海害，没有ol哦")
else:    
    for string in x.replace("ol","fzu",99):
        list1.append(string)
reverse=list(reversed(list1))
result="".join(reverse)  
print(result)
       