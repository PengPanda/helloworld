# import time as TI
from time import localtime

x = 2
y = 3
z = 4
'''
ggggggg
'''
print x + y
print(z**3)  # 平方
print('we\'re going to do \n something')
print("we're going to do sth")
print("I" + "'m" + ' panda ' + str(9))

example_list = [1, 2, 3, 4]
for i in example_list:
    print(i)
print 'test'

for i in range(1, 10, 2):
    print(i)

if x < y < z:
    print("I'm cute!")
if x == y:
    print("I'm smart!")
elif x < y:
    print("hehe")
else:
    print("SB")


def myadd(a, b):
    c = a**b
    print z
    return c


z = myadd(x, y)
print z

text = 'This is my first line.\nThis is my second line. \
\nThis is my third line.'

# print(text)
my_file = open('pp\'s_file.txt', 'w')
my_file.write(text)
my_file.close()

append_text = '\nThis is the appended text.'  # append text
my_file = open('pp\'s_file.txt', 'a')
my_file.write(append_text)
my_file.close()

file = open('pp\'s_file.txt', 'r')  # read file
# content = file.read()
# print(content)
first_line = file.readline()
print 'the first line: ', first_line
second_line = file.readline()
print 'the second line: ', second_line
file.close()


class Calculator:  # class name start with caps letter
    name = 'pp'
    price = 90
    hight = 100
    width = 15
    weight = 20

    def __init__(self, name, price, hight, width, weight):
        self.n = name
        self.p = price
        self.h = hight
        self.w = width
        self.wt = weight

    def add(self, a, b):  # 'self' is needed
        result = a + b
        print 'a + b = ', result

    def minus(self, a, b):
        result = a - b
        print 'a - b = ', result

    def times(self, a, b):
        result = a * b
        print 'a * b =', result

    def divide(self, a, b):
        result = a / b
        print 'a/b = ', result


# print Calculator.name
# print Calculator.price

calcu = Calculator('panda', 90, 15, 10, 200)
print calcu.n
print calcu.h
calcu.add(10, 29)
calcu.divide(29, 10)

# a_input = input('please give a in put:')

# print TI.localtime()
print localtime()