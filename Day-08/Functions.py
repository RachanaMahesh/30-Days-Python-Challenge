# Method:1
# def fun():
#     print("Inside fun()")
# fun()

# Method:2
# def add(var1:int, var2:int) -> int:
#     return var1 + var2
# sum = add(3,5)
# print("Sum is %d"%sum)

# -----------------TYPES OF ARGUMENTS----------------
# Type1:Default
# def fun(x,y=10):
#     print("X :", x)
#     print("Y: ", y)
# fun(5)

# Type2:Keyword
# def student(name, age):
#     print("My name is ",name)
#     print("My age is ", age)
# student(name= "Rachana", age=22)
# student(age=22,name= "Poo")

# Type3:Positional
# def student(name, age):
#     print("My name is ",name)
#     print("My age is ", age)
# student("Rachana",22)
# student(22,"Poo")

# Type4 :Arbitary
def fun(*args, **kwargs):
    for arg in args:
        print(arg)
    for key,value in kwargs.items():
        print(f"{key}-{value}")

fun("Geeks","For","Geeks",first="Geeks", second="For",third = "Geeks")