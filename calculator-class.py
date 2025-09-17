class Operator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plus(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def intdiv(self):
        return self.a // self.b
    def mod(self):
        return self.a % self.b
    def pow(self):
        return self.a ** self.b

n1 = int(input('Enter number1: '))
n2 = int(input('Enter number2: '))
op = input('Enter operator: ')

A = Operator(n1, n2)

op_packages = {
    '+': A.plus(),
    '-': A.minus(),
    '*': A.mul(),
    '/': A.div(),
    '//': A.intdiv(),
    '%': A.mod(),
    '**': A.pow()
}

if op in op_packages:
    print(f'{n1} {op} {n2} = ',op_packages[op])