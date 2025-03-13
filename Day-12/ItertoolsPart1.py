# itertools ia collection of tools that allows us to work with iterators in a fast & memory efficient way
import itertools
# --------------------------------------------------------------------------------------------------

# 1. count() - func will work with any size of data 
# for item in counter:
#     print(item)
# print(next(counter))
# print(next(counter))
# print(next(counter))

# --------- Count is used for mapping ----------
data = [100,200,300,400]
daily_data = list(zip(itertools.count(),data))
print(daily_data)

# --- count() with arguments -----------
# counter = itertools.count(start = 5, step = -2.5)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. zip_longest(): it doesn't end until tehe longest iterable is exhausted. This pairs iterables together. It will pair with default placeholder "none" value when shortest iterable is exhausted.
# ---- zip() fun will ends at the shortest iterable can refer above example ----------
l = [100,200,300,400]
result = list(itertools.zip_longest(range(0,10), l))
print(result)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. cycle() : returns an iterator that goes goes on forever. it takes an iterator as an arguement and will cycle through those values over & over
# counter = itertools.cycle([1,2,3]) 
counter = itertools.cycle(("On","OFF")) 
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#------------------------------------------------------------------------------------------------------------------

# 4. repeat() : it takes some input and repats it infinitely . we can set the limit on this too.

counter1 = itertools.repeat(2, times=3) 
print(next(counter1))
print(next(counter1))
print(next(counter1))
# print(next(counter1)) # it repeats for 3 times and then threw STOP ITERATION EXCEPTION
# print(next(counter1)) # if we would have run it via for loop then it would've looped through three times & we wouldn't have seen EXCEPTION as for loop handles STOP ITERATION EXCEPTION 
# it is used for passing a stream of constant values to map & zip that also operate on intervals 
squares = list(map(pow , range(10), itertools.repeat(2)))
# map takes the function then it takes iterables and & uses those values from those to pass as arguments to that func & it loops through until the shortest list of arguements has run through
print(squares)
#------------------------------------------------------------------------------------------------------------------

# 5. starmap() is similar to map but instead of taking arguments from iterables it instead take arguements that are already paired up as a tuple
squarelist = itertools.starmap(pow , [(0,2),(1,2),(2,2)])
print(list(squarelist))
#------------------------------------------------------------------------------------------------------------------

# 6. combinations(): allows us to take an iterable & return all of the combinations or permutaions.
# combinations : are all diff ways that you can group a certain number of items or the order doesn't matter
# 7. permutations : are all diff ways that you can group a certain number of items and the order does  matter
letters = ['a','b','c','d']
result1 = itertools.combinations(letters,2)

for item in result1:
    print(item,end=" ")
print()
result2 = itertools.permutations(letters,2)

for item in result2:
    print(item,end=" ")  
print()
#------------------------------------------------------------------------------------------------------------------

# 8. product(): In the above example values are not repeating i.e., ('a','a'), ('b','b') etc for this we can't use permutations & combinations
#  so inorder to repeat the values we need to use product() func which will give you the cartian product of iterables that u pass in. if we pass 1 value then we need to tell how many times it should repeat
numbers = [0,1,2,3]
result3 = itertools.product(numbers,repeat=3)
for item in result3:
    print(item,end=" ") 
print("--------------------")
# this is also a way for building password crackers i.e., to arrange all alpha numeric characters in a patter of 6/8
#------------------------------------------------------------------------------------------------------------------

# 9. combinations_with_replacements(): ther's a way to get cobinations with repeated values as well 
result4 = itertools.combinations_with_replacement(numbers,3)
for item in result4:
    print(item,end=" ") 
print("-----------------------------------")
#------------------------------------------------------------------------------------------------------------------

