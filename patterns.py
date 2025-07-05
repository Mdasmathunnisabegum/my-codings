rows=int(input("enter the number of the rows:"))

ascii_value= ord('a')

for i in range(1, rows + 1):
    
     for j in range(i):
         
         print(chr(ascii_value),end=" ")
         
         ascii_value += 1
     print()