# iterables is the one which can be looped over. shld have __iter__ method.
# An object needs to return an iterator object from its __iter__ mthod. an iter object that is returned from the __iter__ method shld define __next__ method.
# which accesses elements in the container one at a time. So if something is iterable that doesn't mean its an iterator.
nums = [1,2,3,4]
# for num in nums:
#     print(num)
print(dir(nums)) # nums is iterable but not iterator
it_nums = iter(nums) # nums.__iter() both results the same result . it returns an iterator object
# Iterator is an object with the state that remembers where it is during iterations. it shoul define __next__ method which returns next value.
# Iterator returns one value at a time whixh will help for memory efficiency
print(dir(it_nums))