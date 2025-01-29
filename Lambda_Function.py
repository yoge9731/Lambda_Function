# Lambda Function
def total_sum(*numbers):
    result=0
    for num in numbers:
        result=result+num
    return result
print(total_sum(1,2,3,4))

def add(*a):
    print(a)
add(1,2,3,4,5,6,7,8,9,10)

def add(*a):
    print(type(a))
add(1,2,3,4,5,6,7,8,9,10)  

def add(*a):
    print(a)
add( )

def add(*a):
    print(a)
add(1)

# sum numbers
def add(*numbers):
    return sum(numbers)
print(add(12,102,135))

def student_info(**details):
    print(details)
    print(type(details))
    for key, value in details.items():
        print(f"{key}:{value}")

student_info(name="yogee", age=30, course="python")

add = lambda a, b : a+b
print(add(1,2))

double = lambda x : 2*x
print(double(200))

student = [
    {'name':'yogee', "age":30, "marks":99},
    {'name':'krishna', "age":25, "marks":95},
    {"name":'hanuma', "age":26, "marks":96}
]
student.sort(key= lambda x : x["marks"])
print(student)

student = [
    {'name':'yogee', "age":30, "marks":99},
    {'name':'krishna', "age":25, "marks":95},
    {"name":'hanuma', "age":26, "marks":96}
]
student.sort(key= lambda x : x["marks"], reverse=True)
print(student)

def factoreal(n):
    if n==1:
        return 1
    return n*factoreal(n-1)
print(factoreal(3))

# nested function
def outer_function(name):
    def inner_function():
        print(f"hello {name}")
    inner_function()
outer_function("yogee")

def calculate(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    def div():
        print(a/b)

    add()
    sub()
    mul()
    div()

calculate(2, 4)

    