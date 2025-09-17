class M:
    def Hello(self):
        print('Hello Python')
    def Cal(self, a,b):
        print(f'{a} + {b} = {a+b}')
        print(f'{a} - {b} = {a-b}')
        print(f'{a} * {b} = {a*b}')
        print(f'{a} / {b} = {a/b}')
        print(f'{a} // {b} = {a//b}')
        print(f'{a} % {b} = {a%b}')
        print(f'{a} ** {b} = {a**b}')


A = M()
B = M()
A.Hello()
B.Cal(1,1)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'My name is {self.name} , and I am {self.age} year old.')


s1 = Student('nina', 11)
s2 = Student('dae', 11)

s1.introduce()
s2.introduce()