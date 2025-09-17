def cal(a, b ,c):
    match c:
        case '+':
            return print('%d + %d = %d' % (a, b, (a+b)))
        case '-':
            return print('%d + %d = %d' % (a, b, (a-b)))
        case '*':
            return print('%d + %d = %d' % (a, b, (a*b)))
        case '/':
            return print('%d + %d = %d' % (a, b, (a/b)))
        case '//':
            return print('%d + %d = %d' % (a, b, (a//b)))
        case '%':
            return print('%d + %d = %d' % (a, b, (a%b)))
        case '**':
            return print('%d + %d = %d' % (a, b, (a**b)))
        case _:
            return print('Error!')
while True:
    try:
        user_input = ' '
        if user_input.lower() == 'q': 
            break
        n1 =int(input('n1: '))
        n2 = int(input('n2: '))
        op = input('operator: ')
        cal(n1, n2, op)
        user_input = input("'q' to exit or press any key to continue: ")
    except Exception as e:
            print(e)