# EXAMPLE : 1
# def outerfun():
#     message = "Hi"
#     def innerfun():
#         print(message) 
#     return innerfun()

# outerfun()
# EXAMPLE : 2
# def outerfun():
#     message = "Hi"
#     def innerfun():
#         print(message) 
#     return innerfun

# my_fun = outerfun()
# print(my_fun.__name__)
# my_fun()

# EXAMPLE : 3
# def outerfun(msg):
#     message = msg
#     def innerfun():
#         print(message) 
#     return innerfun

# hi_fun = outerfun("Hi")
# hello_fun = outerfun("Hello")
# print(hi_fun.__name__)
# hi_fun()
# hello_fun()

#  EXAMPLE : 4
# def htmltag(tag):
#     def wrap_text(msg):
#         print("<{0}>{1}</{0}>".format(tag,msg))
#     return wrap_text

# fun = htmltag("h1")
# print(fun.__name__)
# fun("Hi I'm Rachana")

#  EXAMPLE : 5
import logging
logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(fun):
    def log_fun(*args):
        logging.info('Running "{}" with arguments {}'.format(fun.__name__,args))
        print(fun(*args))
    return log_fun

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

add_logger = logger(add)
sub_logger = logger(sub)
add_logger(3,6)
add_logger(3,9)
sub_logger(7,4)
sub_logger(3,6)
