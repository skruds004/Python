# %% [markdown]
# # Problem 1
# Inspect the code below. The function *subtract_five* should take one integer as input and return that integer minus 5. Running the function will cause Python to throw an error. Change the function so the program correctly prints the value in y.

# %%
def subtract_five(inp):
    return inp-5

y = subtract_five(9) - 6
print(y)

# %% [markdown]
# # Problem 2
# Below is another bit of code that generates an error. The function works correctly but an error thrown when the program is run. Run the program and view the error. Inspect the code. Why does it cause an error? Write a comment explaining why an error occurs. Change the program so that the statement print(yp) will print the integer 7.You will receive negative credit if your solution is print(7).

# %%
def change_amounts(yp):
    n = yp - 4
    return n * 7

yp = change_amounts(5)
print(yp)
#the error occurs because yp is a local variable in the change_amounts function, and it cannot be accessed outside the function

# %% [markdown]
# # Problem 3
# Define a function called change_amounts that has the integer argument *num_here*. If the *num_here* is larger than 10, it should return the *num_here* + 5; otherwise it should return the *num_here* + 2. 

# %%
def change_amounts(num_here):
    if num_here > 10:
        return num_here + 5
    else:
        return num_here + 2

print(change_amounts(15)) 
print(change_amounts(5))  

# %% [markdown]
# # Problem 4
# Define a function called *mult_both* that has two integer parameters: *int1* and *int2*. The default values for *int1* and *int2* are 3 and 4 respectively. The function’s return value should be the two input integers multiplied together. Note, the default value for a parameter is the value assumed by the parameter when no actual parameter is passed.

# %%
def mult_both(int1 = 3, int2 = 4):
    if int1 is None:
        int1 = 3
    if int2 is None:
        int2 = 4
    return int1 * int2


  
# write your function above
print(mult_both())
print(mult_both(5,5))

# %% [markdown]
# # Problem 5
# Define a function called *max_in_list* that returns the maximum value from a list of integers. If the list is empty, your function should return False.

# %%
def max_in_list(temp_list):
    if len(temp_list) == 0:
        return False
    else:
        max_element = temp_list[0]
        for element in temp_list:
            if max_element < element:
                max_element = element
                
        return max_element
# write your function above
my_list = [1,15,73,3,6,10,24]
print(max_in_list(my_list))
print(max_in_list([]))

# %% [markdown]
# # Problem 6
# Write a function named *words_starting_with* that accepts a string as an argument.  The function returns a dictionary whose keys are the unique first letter of each word in the string and whose associated values is a list of words starting with that letter. For example, calling the function as below:
# 
#    words_starting_with("this is the correct Terminal")
#     
#    returns: 
#    
#       { "t": ["this", "the", "terminal"], "i": ["is"], "c": ["correct"]}
# Approach (in the function):
# 
#     Split the sentence into words. Note, the string has embedded new-line (\n) characters.  You need to replace the new-line character with a space. (search for the replace() function in strings)
#     
#     Iterate through the words.
#     
#       convert the first letter to lower case (search for the lower() function in strings)
#     
#       If the first character of the current word is not in the dictionary,
#           initialize the dictionary entry for the current character with an empty list as the value
#       Append the current word to the value for the current character key  

# %%
def words_starting_with(sentence):
    sentence.replace("\n", " ")
    sentence_list = sentence.split()
    word_sort = {}
    for word in sentence_list:
        word = word.replace(word[0], word[0].lower())
        if word[0] in word_sort:
            word_sort[word[0]].append(word)
        else:
            word_sort[word[0]] = [word]
    return word_sort # delete this line and put in your code for the body of the function

sentence = """A satire, however hard it tries
Will always be delightful
Are you upset by how delicious it is
Does it tear you apart to see the satire so pleasing"""
print(words_starting_with(sentence))

# %% [markdown]
# # Problem 7
# In the problem you will calculate the largest Scrabble score for a word in a list of words.  This problem has the following parts:
# 
# 1) Complete the function computeScrabbleScore that accepts a word that returns the Scrabble score for that word. The Scrabble Score for a word is the sum of the value associated with each letter in the word.  The dictionary *letter_values* below has the letter values.
# 
# 2) Complete the function wordScore that accepts a list of words as a parameter and builds the dictionary *word_dict* that has the word as the key and the associated Scrabble score of the word as the value.  This function calls computeScrabbleScore to get the score for each word.
# 
# 3) Print the dictionary returned by wordScore.
# 
# 3) Uses the max accumulation pattern to iterate through the dictionary returned by wordScore to find and print the word with the highest score.
# 
# Note, that *letter_values* has only lower case letters.  You need to allow for uppercase letters.  This means you need to convert upper case letters to lower case before accumulating the Scrabble score for the word. Hint: search for the lower() function for strings.

# %%
def computeScrabbleScore(word):
    letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1,'j':8, 'k':5,
                     'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1,'v':8, 'w':4,
                     'x':8, 'y':4, 'z':10}
# Use the variable score to accumulate the value of the word
    score = 0
    for char in word:
        score += letter_values[char]
    return score

def wordScore(word_list):
    word_dict = {}
    for element in word_list:
        element = element.lower()
        current_score = computeScrabbleScore(element)
        if current_score in word_dict:
            word_dict[current_score].append(element)
        else:
            word_dict[current_score] = [element]
            
    return word_dict
# Use the variable word_dict for the (word,word score) dictionary.


word_list = ['Half','a','league','half','a','league','Half','a','league','onward',
         'All','in','the','valley','of','Death','Rode','the','six','hundred',
         'Forward','the','Light','Brigade','Charge','for','the','guns','he','said',
         'Into','the','valley','of','Death','Rode','the','six','hundred']
word_dict = wordScore(word_list)

# Write code here to find the word in word_dict with the largest word score and print that word.
highest_score = 0
for key in word_dict:
    if key > highest_score:
        highest_score = key

highest_words = word_dict[highest_score]
print("The word(s) with the highest score is/are: ")
for word in highest_words:
    print(word)
    

# %%



