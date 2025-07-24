arr=[1,1,1,3,3,4,4,5,5]
i=0
j=1
while j<len(arr):
    if arr[i]==arr[j]:
        j=j+1
    else:
        arr[i+1] = arr[j]
        i=i+1
        j=j+1
print(arr)
 