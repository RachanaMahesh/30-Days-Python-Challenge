#Example 1:
# def decorator_func(originalfun):
#     def wrapper(*args,**kwargs): # inorder to execute display(), use def wrapper()
#         print("wrapper func is executed before {}".format(originalfun.__name__))
#         return originalfun(*args,**kwargs)
#     return wrapper

# # @decorator_func
# # def display():
# #     print("Hi Good Morning !")

# # display = decorator_func(display) # Alternate method instead of @decorator_func
# # display()

# @decorator_func
# def display(name,age):
#     print("I am {} and I am {}".format(name,age))

# display("Rachana",25)

#Example 2
# class Decorator_class(object):
#     def __init__(self,originalfun):
#         self.originalfun = originalfun
    
#     def __call__(self, *args, **kwargs):
#         print("wrapper class is executed before {}".format(self.originalfun.__name__))
#         return self.originalfun(*args,**kwargs)
    
# @Decorator_class
# def display(name,age):
#     print("I am {} and I am {}".format(name,age))

# display("Rachana",25)

#Example 3
import logging
import time
from functools import wraps

def logger(fun):
    logging.basicConfig(filename="{}.log".format(fun.__name__),level=logging.INFO)
    @wraps(fun)
    def wrapper_fun(*args,**kwargs):
        logging.info("Run fun - '{}' with args: {} and kwargs :{}".format(fun.__name__,args,kwargs))
        fun(*args,**kwargs)
    return wrapper_fun

def timer(fun):
    @wraps(fun)
    def wrapper(*args,**kwargs):
        t1= time.time()
        result = fun(*args,**kwargs)
        t2 = time.time() - t1
        print("fun - '{}' took {}seconds to complete".format(fun.__name__,t2))
        return result
    return wrapper

# display = logger(timer(display))
@logger
@timer
def display(name,age):
    time.sleep(1)
    print("Display info: ran with argument ({},{})".format(name,age))

display("Hank",39)
