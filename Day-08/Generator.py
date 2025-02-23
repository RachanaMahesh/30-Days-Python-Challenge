# Real Time UseCase
import mem_profile
import time
import random

names = ["Akash","Anjali", "Ammu", "Anu","Arati"]
subjects = ["MECH","CS", "ECE","EEE"]

print('Memory (Before) {}Mb'.format(mem_profile.memory_usage_psutil()))
def people_list(num_people):
    result = []
    for i in range(num_people):
        people = {
            id : i,
            'name' : random.choice(names),
            'subject': random.choice(subjects)
        }
        result.append(people)
    return result

def people_generator(num_people):
    for i in range(num_people):
        people = {
            id : i,
            'name' : random.choice(names),
            'subject': random.choice(subjects)
        }
        yield people
    
t1 = time.perf_counter()
people = people_list(1000000)
t2 = time.perf_counter()

t3 = time.perf_counter()
people = people_generator(1000000)
t4 = time.perf_counter()

print('Memory (After) {}Mb'.format(mem_profile.memory_usage_psutil()))
print("took {} seconds".format(t2-t1))
print("took {} seconds".format(t4-t3))

# Eg:1
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

# Eg:2
# def square(list):
#     for l in list:
#         yield l*l
# results = square([2,4,6,8])
# for res in results:
#     print(res)
# Generator expression
#Eg:1
#  res = (i*5 for i in range(5) if i%2 == 0)
# for x in res:
#     print(x)

# Eg:2
# list=[2,4,6,8]
# res = (i*i for i in list)
# for x in res:
#     print(x)

