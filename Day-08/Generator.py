# def fib(limit):
#     a,b =0,1
#     while a< limit:
#         yield a
#         a,b  = b,a+b

# # result = fib(5)
# # print(next(result))
# # print(next(result))
# # print(next(result))
# # print(next(result))
# # print(next(result))

# for i in fib(5):
#     print(i)

# Generator expression
res = (i*5 for i in range(5) if i%2 == 0)
for x in res:
    print(x)
