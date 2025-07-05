l=[1,1,2,2,3,3,4,4,5,5]
s=set()
for i in range(0,len(l)):
    s.add(l[i])
count=0
for i in s:
    l[count]=i
    count =count+1
print(l)
    