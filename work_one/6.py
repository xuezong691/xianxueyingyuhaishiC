the_list=[6,6,6,5,8,18,444,6,8,8,1,3,5,1,1,4,5,1,4]
def count(list):
  dict={}
  for i in the_list:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
  return dict      
print(count(the_list))         