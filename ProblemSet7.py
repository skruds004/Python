# %% [markdown]
# # Problem 1
# You need to produce a list of Scrabble word values for a list of words.  Write a function *scrabbleValue* that is passed a the string parameter *word* and returns the scrabble value for that word.  The scrabble value of each letter is in the dictionary *letter_values*.  Use the *map* function and the *scrabbleValue* function to create and print a list of scrabble word values for the words in the list *words*.

# %%
def scrabbleValue(word):
    value = 0
    for letter in word:
        value += letter_values[letter]
        
    return value

letter_values =  {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g': 2, 'h':4,
    'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,
    's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}

words = ['python', 'program', 'list', 'string', 'unix', 'hours', 'syntax', 'error']
value_list = list(map(lambda x: scrabbleValue(x), words))
print(value_list)

# %% [markdown]
# Output should be:  
# &nbsp;&nbsp;&nbsp;&nbsp;[14, 12, 4, 7, 11, 8, 16, 5]

# %% [markdown]
# # Problem 2
# You need to produce a list of word whose word lenght is an even number.  Write a function *selectWord* that is passed the string parameter *word*.  The function returns *True* if the lenght of the string is an even number; otherwise *False* is returned. Use the *filter* function and *selectWord* function to create and print a list of even length words from the list *words*.

# %%
def selectWord(word):
    if len(word)%2 == 0:
        return True
    else:
        return False

words = ['python', 'program', 'list', 'string', 'unix', 'hours', 'syntax', 'error']
even_words = list(filter(selectWord,words))
print(even_words)

# %% [markdown]
# Output should be:  
# &nbsp;&nbsp;&nbsp;&nbsp;['python', 'list', 'string', 'unix', 'syntax']

# %% [markdown]
# # Problem 3
# This is the same problem as Problem 2 but you must use *list comprehension* and the *filter* function within the *list comprehension*. 

# %%
def selectWord(word):
    if len(word)%2 == 0:
        return True
    else:
        return False

words = ['python', 'program', 'list', 'string', 'unix', 'hours', 'syntax', 'error']
even_words = [x for x in filter(lambda x: selectWord(x), words)]
print(even_words)

# %% [markdown]
# Output should be:  
# &nbsp;&nbsp;&nbsp;&nbsp;['python', 'list', 'string', 'unix', 'syntax']

# %% [markdown]
# # Problem 4
# This is the identical problem as Problem 3. However, instead of using the *selectWord* function in the *filter* function, you need to use a *lamba expression*. Hint: returning true or false based upon whether the length of the string is even or odd, may be done with a simple python expression.  If you used an *if* statement in *selectWord*, ponder the expression that you used. 

# %%
words = ['python', 'program', 'list', 'string', 'unix', 'hours', 'syntax', 'error']
even_words = [x for x in filter(lambda x: len(x)%2 == 0, words)]
print(even_words)

# %% [markdown]
# Output should be:  
# &nbsp;&nbsp;&nbsp;&nbsp;['python', 'list', 'string', 'unix', 'syntax']

# %% [markdown]
# # Problem 5
# The list *names* where each element is a string in "First Name Last Name" sequence. Derive a new list from *names* where the string is in "Last Name, First Name" sequence.  Use list comprehension to convert the list. Hint, you will need to split each name into the First and Last.  Remember 'a' + 'b' ==> 'ab'. 

# %%
names = ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Marie Curie","Charles Darwin", "Galileo Galilei", "Margaret Mead"]
new_names = [x[1] + ', ' + x[0] for x in list([x.split() for x in names])]
print(new_names)

# %% [markdown]
# Output should be:  
# &nbsp;&nbsp;&nbsp;&nbsp;['Newton, Isaac', 'Einstein, Albert', 'Bohr, Niels', 'Curie, Marie', 'Darwin, Charles', 'Galilei, Galileo', 'Mead, Margaret']

# %% [markdown]
# # Problem 6
# Given a string as below, write code the uses list comprehension to reverse the words in the string.  You need to use the reversed() and join() functions. Albeit, this solution is just one line of code, this is a challenging problem.  You need to break this down into multiple steps:  
# &nbsp;&nbsp;&nbsp;&nbsp;1) You know how to split a string into a list of words.  
# &nbsp;&nbsp;&nbsp;&nbsp;2) Reverse the list of words using reversed().  The end result should the a list of the words in reverse order.  
# &nbsp;&nbsp;&nbsp;&nbsp;3) Use list comprehension to iterate through the list of reversed words.  
# &nbsp;&nbsp;&nbsp;&nbsp;4) Use join() to join the words in the reversed list into a string.  

# %%
sentence  = 'we are never ever getting back together'
s = ' '.join([x for x in reversed(sentence.split())])
print(s)

# %% [markdown]
# Output show be:  
# &nbsp;&nbsp;&nbsp;&nbsp;together back getting ever never are we

# %%



