email = input('enter the email id:')
password=input('enter the password to go to next page:')

if email == 'asma2004@gmail.com' and password =='AS_ma@2004':
    print('Welcome')
elif email == 'asma2004@gmail.com' and password !='AS_ma@2004':
    print('INVALID')
password=input('enter the password once again to log in')
if password =='AS_ma@2004':
    print('WELCOME')
else:
    print('incorrect')