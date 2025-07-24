arr1=[1,2,3,1,4,5] #union of two sorted array
arr2=[2,2,3,4,5,6]

s=set()
for i in range(0,len(arr1)):
    s.add(arr1[i])
for i in range(0,len(arr2)):
    s.add(arr2[i])
print(s)