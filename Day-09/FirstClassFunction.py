# A programming language is said to have FirstClassFunction if it treats functions as first-class-citizen
# first-class-citizen is an entity which supports all the operations generally available to other entities. 
# These operations include being passed as an argument, returned from a function & assigned to a variable.

#--------- Function Assigned to a variable ------------
def square(n):
    return n*n
# f = square(5)
# print(square)
# print(f)

f = square
# print(square)
# print(f)
# print(f(5))

# If function accepts other func as argument or returns the fun as a result that's wt we call Higher Order function
#--------- Function Passed As An Argument ------------
def map(func,arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = map(square,[1,2,3,4,5])
# s

#--------- Return the Function as a result ------------
def logger(msg):
    def log_message():
        print(msg)
    return log_message

log_hi = logger("Hi")
log_hi()

#Eg:2 
def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag,msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1("Headline")

print_p = html_tag('p')
print_p("hello, Good Morning!")