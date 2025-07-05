fnum=int(input('enter the first num'))
snum=int(input('enter the second number'))

op = input('enter the operation to perform')

if op =='+':
    print(fnum+snum)
    
elif op =='-':
    print(fnum-snum)
    
elif op == '*':
    print(fnum * snum)

else:
    print(fnum/snum)