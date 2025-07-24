l=[1,2,3,2,0,0,3,4,1,0,0,5]
temp=[]
for i in range(0,len(l)):
    if l[i]!=0:
        temp.append(l[i])
print(temp)
for i in range(0,len(temp)):
    l[i]=temp[i]
for i in range(len(temp),len(l)):
    l[i]=0
print(l)

               