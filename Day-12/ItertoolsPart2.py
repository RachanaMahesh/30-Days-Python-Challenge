import itertools
# 10. chain() : allows us to chain together the iterables so that we will go through all the items in the 1st iterable & then followed by 2nd iterable and so on
print("----------------------  10. chain()    ------------------------")
letters = ['a','b','c','d']
numbers = [0,1,2,3]
names = ["Rachana","Mahesh"]
# we can create a new list that combines all 3 lists and loop over all the items as below
new_list =letters+numbers+names
print(new_list)
#the problem with above approach is it creates a new list with all of those values. so above all 3 lists are short so it doesn't matter
# but what if these lists contains millions of items? therefore it is majorly inefficient to create a copies of the lists and put them in another variable
# or what if those are generators & something else apart from list then we can use chain
combined = itertools.chain(letters,numbers,names)
for item in combined:
    print(item,end=" ")
print()
print("----------------------  11. islice()  ------------------------")
#----------------------------------------------------------------------------------------------------------------------------

# 11.islice(): this func allows us to perform slicing on an iterator. we can pass 3 arguements 1.starting point 2.stopping point 
# to start from 0 to 9 (stop point) & 5 to stop at 5th index
# res= itertools.islice(range(10),5)
# res= itertools.islice([0,5,10,17,18,20,25,30,6],5)
res= itertools.islice(range(10),1,5,2) # 1 start index & 5 end index & 2 - step value
print(list(res))
# it's useful bcoz we may have an iterator that is too large to put into memory so we don't want to cast it to list just to get certain slice of the iterator 
# for example letsgrab only first 3lines from the log files which has 1000 lines in it
with open('test.log','r') as f: # files are actually iterators, when you u call __next__() on them it will get the next line in the file & we can use it as a other iterators
    header = itertools.islice(f, 3) # it goes upto 3 lines 
    for line in header:
        print(line,end="") # as it as \n after each line if we add just print then we add 2 lines

print("---------------------------  13. compress()  ------------------------------------------------")
#13. compress(): 
setters =[True,True,False,True]
result = itertools.compress(letters,setters)
print(list(result))

#filter():
print("--------------------------- filter()  example------------------------------------------------")
def lt2(num):
    if num < 2:
        return True
    return False
num = [0,1,2,3,2,1,0]
result1 = filter(lt2,num)
for item in result1:
    print(item, end =" ")
print()

print("---------------------------  14. filterfalse()  ------------------------------------------------")
# filterfalse():
result2 = itertools.filterfalse(lt2,num)
for item in result2:
    print(item, end =" ")
print()

print("---------------------------  15. dropwhile()  ------------------------------------------------")
# dropwhile():
result2 = itertools.dropwhile(lt2,num)
for item in result2:
    print(item, end =" ")
print()

print("---------------------------  16. takewhile()  ------------------------------------------------")
# takewhile():
result3 = itertools.takewhile(lt2,num)
for item in result3:
    print(item, end =" ")
print()

print("---------------------------  17. accumulate()  ------------------------------------------------")
#accumulate(): 
result4 = itertools.accumulate(num)
for item in result4:
    print(item, end =" ")
print()

print("---------------------------  18. groupby()  ------------------------------------------------")
# groupby(): 
def get_state(person):
    return person['state']

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]
person_group = itertools.groupby(people, get_state)
for key,group in person_group:
    print('state: ', key)
    # for person in group:
    #     print("Person:",person)
    print('Count:',len(list(group)))
    print()

print("---------------------------  19. tee()  ------------------------------------------------")
#tee(): 
# people.sort(key=get_state)

# Step 2: Convert groupby iterator to a list of tuples (state, list of people)
person_group_list = [(state, list(group)) for state, group in itertools.groupby(people, get_state)]

# Step 3: Create two copies using tee
copy1, copy2 = itertools.tee(iter(person_group_list))

# Step 4: Iterate over first copy
print("\nFirst Copy:")
for state, group in copy1:
    print('State:', state)
    for person in group:
        print("  ", person)



