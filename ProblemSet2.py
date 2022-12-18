# %% [markdown]
# # Problem 1
# Write one _for_ loop to print out each character of the string *my_str* on a separate line. 

# %%
my_str = "MICHIGAN"

# Write your code below.
for char in my_str:
    print(char)

# %% [markdown]
# # Problem 2
# In the cell below where indicated, do the following:
# 1. Write one _for_ loop to print out each element of the list *several_things*. 
# 2. Write another _for_ loop to print out the _type_ of each element of the list *several_things*. 

# %%
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

# Write your code below.
for element in several_things:
    print(element)
    
for elem_type in several_things:
    print(type(elem_type))

# %% [markdown]
# # Problem 3
# Write code that uses iteration to print on a separate line the length of each element of the list *str_list*. 

# %%
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code below.
for length in str_list:
    print(len(length))

# %% [markdown]
# # Problem 4
# Write code to count the number of characters in the string *original_str* using the accumulation pattern. Assign the answer to a variable num_chars. Print the variable num_chars.
# 
# Do NOT use the len function to solve the problem.  You may use the len function on the string to confirm the your answer is correct. 

# %%
original_str = "The quick brown rhino jumped over the extremely lazy fox."

# Write your code below.
num_chars = 0
for index in original_str:
    num_chars += 1
    
print(num_chars)

# %% [markdown]
# # Problem 5
# Write code to create a list of word lengths for the words in *original_str* using the accumulation pattern and assign the answer to a variable num_words_list. You need to use the len function to determine the lenght of each word. Print the list created. 

# %%
original_str = "The quick brown rhino jumped over the extremely lazy fox."

# Write your code below.
str_list = original_str.split()
num_words_list = []
for string in str_list:
    num_words_list.append(len(string))
    
print(num_words_list)

# %% [markdown]
# # Problem 6
# The string *addition_str* contains list of numbers separated by the plus sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer).  Print the variable sum_val. 
# 
# You should use the split function to split by "+" and int() to cast to an integer.

# %%
addition_str = "2+5+10+20"

# Write your code below.
sum_val = 0
int_list = addition_str.split("+")
for num in int_list:
    sum_val += int(num)
    
print (sum_val)

# %% [markdown]
# # Problem 7
# The string *week_temps_f* contains a list of fahrenheit temperatures separated by the comma.  Write code that uses the accumulation pattern to compute the average temperature and assign it to the variable *avg_temp*. Do not hard code your answer.  This means that your code must compute both the total of all temperatures and the number of temperatures in week_temps_f.  Print the variable avg_temp.
# 
# You need to use the *split* function to split by "," and float() to cast to a float. 

# %%
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

# Write your code below.
num_temps = 0
sum_temps = 0
week_temps = week_temps_f.split(",")
for temp in week_temps:
    num_temps += 1
    sum_temps += float(temp)
    
avg_temp = sum_temps/num_temps
print(avg_temp)


# %% [markdown]
# # Problem 8
# Write a program that uses the turtle module and a _for_ loop to draw something.  It doesn’t have to be complicated, but draw something different than we did in the textbook or in class.  Hint: if you are drawing something complicated, try setting .speed(10) for the turtle to draw fast or .speed(0) to draw super fast.
# 
# This version of Turtle is missing a couple of properties and methods as described in the online textbook.  

# %%
from mobilechelonian import Turtle

# Write your code below.
turt = Turtle()
for idx in range(0, 25):
    turt.left(45)
    turt.forward(idx)


# %%


# %%


# %%



