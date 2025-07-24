arr=[1,2,3,4,5,6,7]
d=8
size=len(arr)
d=d%size
temp=[]
for i in range(0,d):
    temp.append(arr[i])
for i in range(d,len(arr)):
    arr[i-d]=arr[i]
temp_index=0
for i in range(size-d,len(arr)):
    arr[i]=temp[temp_index]
    temp_index=temp_index+1
print(arr)