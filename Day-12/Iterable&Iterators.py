# iterables is the one which can be looped over. shld have __iter__ method.
# An object needs to return an iterator object from its __iter__ mthod. an iter object that is returned from the __iter__ method shld define __next__ method.
# which accesses elements in the container one at a time. So if something is iterable that doesn't mean its an iterator.
# nums = [1,2,3,4]
# for num in nums:
#     print(num)
# print(dir(nums)) # nums is iterable but not iterator

# it_nums = iter(nums) # nums.__iter() both results the same result . it returns an iterator object
# Iterator is an object with the state that remembers where it is during iterations. it shoul define __next__ method which fetches it's next value.
# Iterator returns one value at a time which will help for memory efficiency
# print(it_nums)
# print(dir(it_nums))
# print(next(it_nums))
# print(next(it_nums))
# print(next(it_nums))
# print(next(it_nums))
# print(next(it_nums)) # threw StopIteration exception when it runs out of value basically it works as below but in for loop we don't get StopIteration exception
# while True:
#     try:
#         item = next(it_nums)
#         print(item)
#     except StopIteration:
#         break

#-----------------Built In Range Functions --------------------------------
class myRange:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self # as we are defining __next__ fun within the same class we can just return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        currentvalue = self.start
        self.start+=1
        return currentvalue

nums = myRange(1,10)
print(next(nums))
print(next(nums))
# for num in nums:
#     print(num)

# ---------------------Generators --------------------------
# Generators are also an iterators so __iter__ & __next__ methods are created automatically so we don't need to create them manually

def my_range(start,end): # Genertaors fun works like a class does that we created so good to use generators
    current = start
    while current < end :
        yield current
        current+=1

numbers = my_range(1,10)
for num in numbers:
    print(num)

# It's not mandatory to have end value as the iterator can go on forever but it fetches one value at a time
# this will be useful when it comes to memory efficient program bcoz sometimes there are so many values that u just couldn't hold them all in memory
# if you were to put them in a list or tuple but if u simply use it as a iterator then u can loop over one value at a time until it got exhauste

# eg: when wrting a password cracker and wanted to brute-force it by checking all of the possible password using a certain group of characters 
# there would be so many different possible passwords that you couldn't hold them possibly on a single list as ur computer would run out of memory
# but you could use an iterator to loop through all those possiblities one at a time. It might take some time but wouldn't take up all of your computers memory