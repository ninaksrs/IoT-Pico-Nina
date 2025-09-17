num1= int(input('Enter number:'))
num2= int(input('Enter number:'))
operator=input('Enter operator (+,-,*,/,//,%,**)')
if operator=='+':
    print(f'{num1}+{num2}={num1+num2}')
elif operator=='-':
    print(f'{num1}-{num2}={num1-num2}')
elif operator=='*':
    print(f'{num1}*{num2}={num1*num2}')
elif operator=='/':
    print(f'{num1}/{num2}={num1/num2}')
elif operator=='//':
    print(f'{num1}//{num2}={num1//num2}')
elif operator=='%':
    print(f'{num1}%{num2}={num1%num2}')
elif operator=='**':
    print(f'{num1}**{num2}={num1**num2}')
else:
    print('Error')

    