# SYNTAX : eval(expression, global variables(dictionary),local variables(dictionary))
result = eval("5+2*3")
print(result)

a = 10
b = 20
print(eval("a+b"))

def square(n):
    return n*n
print(eval("square(5)"))

x = 10
context ={"x":20, "y":60}
print(eval("x+y",context))

#SECURITY RISK untrusted userinput input can be dangerous as it can execute arbitary code
# user_input = "import os; os.system('rm-rf /')" COuld delete files
# eval(user_input) Dangerous

#SAFE ALTERNATIVE to use ast.literal_eval()
import ast
safe_input = "{'name':'Aice','age':25}"
result = ast.literal_eval(safe_input) # safely converts to dictionary {'name': 'Aice', 'age': 25} without executing arbitary code
print(result)
