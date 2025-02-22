# PASS BY VALUE FOR Non - Mutable Objects
# def fun(string):
#     string = "Updated the string inside fun()"
#     print(id(string))
#     print("Inside fun() :",string)
#     return

# string = "Defined string outside fun()"
# print(id(string))
# print("Outside fun() Before fun call :",string)
# fun(string)
# print("Outside fun() After fun call :",string)

# PASS BY REFERENCE FOR Mutable Objects
def fun(list):
    string = "Updated the List inside fun()"
    list[0] = 100
    print(id(list))
    print("Inside fun() :",list)
    return

list = [2,4,6,8,10]
print(id(list))
print("Outside fun() Before fun call :",list)
fun(list)
print("Outside fun() After fun call :",list)