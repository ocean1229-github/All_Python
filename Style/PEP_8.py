# 이름규칙
# bad
someVariableName = 1
SomeVariableName = 1

def someFunctionName():
    print("Hello")

# good
some_variable_name = 1

def some_function_name():
    print("Hello")


# bad
someConstant = 3.14
SomeConstant = 3.14
some_constant = 3.14

# good
SOME_CONSTANT = 3.14


# bad (의미 없는 이름)
a = 2
b = 3.14
print(b * a * a)

# good (의미 있는 이름)
radius = 2
PI = 3.14
print(PI * radius * radius)


# bad (의미 없는 이름)
def do_something():
    print("Hello, world!")

# good (의미 있는 이름)
def say_hello():
    print("Hello, world!")


#들여쓰기
# bad (스페이스 2개)
def do_something():
  print("Hello, world!")

# bad (스페이스 8개)
i = 0
while i < 10:
        print(i)

# good (스페이스 4개)
def say_hello():
    print("Hello, world!")

# 함수 정의
# bad
def a():
    print('a')
def b():
    print('b')

def c():
    print('c')

# good
def a():
    print('a')


def b():
    print('b')


def c():
    print('c')

# 괄호 안
# bad
spam( ham[ 1 ], { eggs: 2 } )

# good
spam(ham[1], {eggs: 2})


# 함수괄호
# bad
def spam (x):
    print (x + 2)


spam (1)


# 쉼표
# bad
print(x , y)

# good
print(x, y)


# 지정연산자
# bad
x=1
x    = 1

# good
x = 1


# 연산자
# bad
i=i+1
submitted +=1

# good
i = i + 1
submitted += 1

# 우선순위의 경우
# bad
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# good
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)


# 코멘트
# bad
x = x + 1# 코멘트

# good
x = x + 1  # 코멘트