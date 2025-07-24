a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))
root1=0
root2=0
d=(b**2)-4*a*c
root1=(-b+(d)**(1/2))/2*a
root2=(-b-(d)**(1/2))/2*a
print(root1,root2)