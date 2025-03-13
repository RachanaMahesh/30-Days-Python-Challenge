import itertools
import operator
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

print("---------------------------  12. compress()  ------------------------------------------------")
#13. compress(): func used is datascience problems where u can pass iterables & some selector & it will retuen a new iterable that only containes items in our iterable that has a corresponding True value.
setters =[True,True,False,True]
result = itertools.compress(letters,setters)
print(list(result))

#filter(): it ia aimilR TO COMPRESS but the difference is that filter() uses a function to determine whether something is true or false but in compress those values were passed in as iterable
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

print("---------------------------  13. filterfalse()  ------------------------------------------------")
# filterfalse(): it is similar to filter() func except instead it gives you the values that retun false instead of true 
result2 = itertools.filterfalse(lt2,num)
for item in result2:
    print(item, end =" ")
print()

print("---------------------------  14. dropwhile()  ------------------------------------------------")
# dropwhile(): drops the first few ones that met the criteria 
result2 = itertools.dropwhile(lt2,num)
for item in result2:
    print(item, end =" ")
print()

print("---------------------------  15. takewhile()  ------------------------------------------------")
# takewhile(): instead will grab all the values that retuned true  & as soon as it hits a value that doesn't return true then it will just stop at that point
result3 = itertools.takewhile(lt2,num)
for item in result3:
    print(item, end =" ")
print()

print("---------------------------  16. accumulate()  ------------------------------------------------")
#accumulate(): takes an iterable & returns accumulated sum of each item & it uses addition by default 
result4 = itertools.accumulate(num)
for item in result4:
    print(item, end =" ")
print()
# we can use other operatior as well i.e., multiply
n =[1,3,5,6,7]
multiples_result = itertools.accumulate(n, operator.mul)
for item in multiples_result:
    print(item, end =" ")
print()

print("---------------------------  17. groupby()  ------------------------------------------------")
# groupby(): go through an iterable & group value based on a certain key & then it will return a stream of tuples 1. key 2. an iterator that were grouped by that key

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
# we can use these to fetch how many student in a class got A, B & C...
#Group by () expects the initial iterable to be sortd so that it can group properly which is different from SL-group by 

print("---------------------------  18. tee()  ------------------------------------------------")
#tee(): when we want to replicate an iterator 
people.sort(key=get_state)

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

# if we want more copie then we could just pass in an arguement to this tee func & return however many that we'd like to have
# #NOTE: we shld no longer use the original iterator after u copy it.i.e., we shldn't use person_group_list but can use copy1 & copy2

x=[1,2,3,4]
x1,x2,x3 = itertools.tee(x,3)  
for i in x1:
    print(i,end=  " ")
print()
for i in x2:
    print(i,end=  " ")
print()
for i in x3:
    print(i,end=  " ")
print()