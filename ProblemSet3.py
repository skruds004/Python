# %% [markdown]
# # Problem 1
# The variable *rainfall_mi* contains a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every value is separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable *num_rainy_months*. In other words, count the number of items with values > 3.0. Print the variable *num_rainy_months*. Hard-coded answers will receive no credit.

# %%
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

rainfall = rainfall_mi.split(", ")
num_rainy_months = 0
for inches in rainfall:
    if float(inches) > 3.0:
        num_rainy_months += 1
        
print(num_rainy_months)

# %% [markdown]
# # Problem 2
# The variable *sentence* stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the *variable same_letter_count*. Print the variable *variable same_letter_count*. Hard-coded answers will receive no credit.

# %%
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
words = sentence.split()
same_letter_count = 0
for word in words:
    if word[0] == word[-1]:
        same_letter_count += 1
        
print(same_letter_count)

# %% [markdown]
# # Problem 3
# Write code to count the number of strings in the list *items* that have the character "w" in it. Assign that number to the variable *acc_num*. Print the variable *acc_num*.
# Hints:
# 1. Use an accumulation pattern.
# 2. the _in_ operator checks whether a substring is present in a string.
# Hard-coded answers will receive no credit.

# %%
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for item in items:
    if 'w' in item:
        acc_num += 1
        
print(acc_num)

# %% [markdown]
# # Problem 4
# Write code that counts the number of words in variable *sentence* that contain either an “a” or an “e”. Store the result in the variable *num_a_or_e*.  Print the variable *num_a_or_e*.
# Hints:
# 1. Make sure to not double-count words that contain both an a and an e.
# 2. Use the _in_ operator.
# 3. Use either _if_ or _if_-_elif_.
# Hard-coded answers will receive no credit.

# %%
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
words = sentence.split()
num_a_or_e = 0
for word in words:
    if 'a' in word:
        num_a_or_e += 1
    elif 'e' in word:
        num_a_or_e += 1
        
print(num_a_or_e)

# %% [markdown]
# # Problem 5
# The text file PS3_wnvhumancases.txt contains data on West Nile virus infections in the United States from 2006 through 2018. Each record (line) in the file has four columns(values) separated by a comma. Each column is described below.
# 
#     Column 1:  Year (reported)
#     Column 2:  Week (week reported)
#     Column 3:  County
#     Column 4:  Cases (number of cases reported)
# 
# Process the file and use an accumulation pattern to provide a count of the number of records in the file in the variable __nrecs__ and the total number of incidents, i.e., a total of Positive Cases, in the variable __nincidents__.  Your output should appear similar to the following:
# 
#     Total Records processed:  1789
#     Total Incidents:  4993
# 
# Hint:  Since this is a text file each line is a string. You will need to split the line into a list of values. 

# %%
my_file = open("PS3_wnvhumancases.txt","r")
nrecs = 0
nincidents = 0
for line in my_file:
    split_line = line.split(",")
    nrecs += 1
    nincidents += int(split_line[3])
    
print("Total Records processed: " ,nrecs)
print("Total Incidents: ", nincidents)
my_file.close()

# %%



