arr=[12, 35, 1, 10, 34, 1]
first_largest=arr[0]
Second_largest=arr[0]
for i in range(0,len(arr)):
    if arr[i]>first_largest:
        Second_largest=first_largest
        first_largest=arr[i]
    else:
        if arr[i]>Second_largest:
            Second_largest=arr[i]
            
print(Second_largest)