# Define the class & genertoe fun for below logic
# my_sentence = Sentence("This is a test")
# for word in my_sentence:
#     print(word)

# --- Outupt: --- 
# This
# is 
# a
# test

class Sentence:
    def __init__(self,secntence):
        self.secntence = secntence
        self.index = 0
        self.word = secntence.split()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.word):
            index = self.index
            self.index+=1
            return self.word[index]
        else:
            raise StopIteration

my_sentence = Sentence("This is a test")
print(next(my_sentence))
print(next(my_sentence))
for word in my_sentence:
    print(word)


def sentence(string):
    st = string.split(" ")
    for word in st:
        yield word
    # i=0
    # while i < len(st):
    #     yield st[i]
    #     i+=1

my_sentence = sentence("This is a test")
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
# print(next(my_sentence))
# for word in my_sentence:
#     print(word)