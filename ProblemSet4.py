# %% [markdown]
# # Run this cell first

# %%
umSchools = {
  "A. Alfred Taubman College of Architecture & Urban Planning": 1906,
  "College of Engineering": 1854,
  "College of Literature, Science, and the Arts": 1841,
  "Gerald R. Ford School of Public Policy": 1914,
  "Horace H. Rackham School of Graduate Studies": 1912,
  "Penny W. Stamps School of Art & Design": 1974,
  "School of Dentistry": 1875,
  "School of Education": 1921,
  "School of Information": 1996,
  "School of Kinesiology": 1984,
  "School of Law": 1859,
  "School of Medicine": 1850,
  "School of Music, Theatre & Dance": 1880,
  "School of Natural Resources & Environment": 1927,
  "School of Nursing": 1893,
  "School of Pharmacy": 1876,
  "School of Public Health": 1941,
  "School of Social Work": 1951,
  "Stephen M. Ross School of Business": 1924
}

january_temp_data = """2016,   6, 51
        2015,  -3, 41
        2014, -14, 43
        2013,  -3, 60
        2012,   2, 55
        2011,   1, 52
        2010,   3, 47
        2009, -10, 39
        2008,   3, 62
        2007,   5, 50
        2006,  18, 53
        2005,  -3, 56
        2004,  -6, 55
        2003,  -5, 47
        2002,  11, 55
        2001,   1, 43
        2000,  -2, 56"""

# %% [markdown]
#  # Problem 1
# The dictionary *courses* is a hypothetical schedule for a semester.  The key is the course name and the value is the number of credits. Use an accumulation pattern to find the total number of credits taken this semester and assign it to the variable *credits*. Print the variable *credits*.

# %%
courses = {'CPS 141':4, 'ENG 101':3, 'CIS 100':3, 'CNT 206':4, 'MTH 160':4}
credits = 0
for key in courses.keys():
    credits += courses[key]
    
print(credits)

# %% [markdown]
# # Problem 2
# The dictionary *umSchools* maps the names of schools at Michigan to the year they were founded. Write code that assigns the year that the School of Information was founded to the variable *si_founded* (so si_founded should end up with the value 1996). Print the variable *si_founded*. 

# %%
si_founded = umSchools["School of Information"]
print(si_founded)


# %% [markdown]
# # Problem 3
# Using the *umSchools* dictionary, write code to add the name of every school that was founded in the 20th century (after 1900) into a list *newer_schools*. Print the list *newer_schools*.

# %%
newer_schools = []
for key in umSchools.keys():
    if umSchools[key] >= 1900:
        newer_schools.append(key)
        
print(newer_schools)


# %% [markdown]
# # Problem 4
# Given the string *s* below, write code to determine the most common letter in the string and assign that to the variable *common_letter*.  This is a two part problem:
# 1. Create a dictionary of letters and their associated count.
# 2. Use a max accumulation pattern on that dictionary to find the letter with the largest count.
# 
# Print most common letter and the associated number of occurances.

# %%
s = """
peter piper picked a peck of pickled peppers;
a peck of pickled peppers peter picked;
if peter piper picked a peck of pickled peppers,
where's the peck of pickled peppers peter picked?
"""

char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
        
highest_count = 0
for char in char_count.keys():
    if char_count[char] > highest_count:
        highest_count = char_count[char]
        common_letter = char
        
print(common_letter, ": ", highest_count)

# %% [markdown]
# # Problem 5
# Given the string *s* below, write code to determine the most common word in the string and assign it to the variable *common_word*.  This is similar to the above problem in that there are two parts:
# 1. Create a dictionary words and their associated count.
# 2. Use a max accumulation pattern on that dictionary to find the word with the largest count.
# 
# Print most common word and the associated number of occurances.

# %%
s = "Number of slams in an old screen door depends upon how loud you shut it, the count of slices in a bread depends how thin you cut it, and amount 'o good inside a day depends on how well you live 'em. All depends, all depends, all depends on what's around ya."
s_list = s.split()
words = {}
for word in s_list:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

highest_count = 0
for word in words.keys():
    if words[word] > highest_count:
        highest_count = words[word]
        common_word = word
        
print(common_word, ": ", highest_count)

# %% [markdown]
# # Problem 6
# Write code that will count the number of vowels in the string *s* and assign the result to the variable *num_vowels*. For this problem, vowels are only a, e, i, o, and u. You may find the _in_ operator useful to derive the solution. Print the variable *num_vowels*.

# %%
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = 0
for char in s:
    if char in vowels:
        num_vowels += 1
        
print(num_vowels)

# %% [markdown]
# # Problem 7
# Write code that creates the dictionary *vowel_frequencies* where the keys are the five vowels and the values are number of occurances of that vowel in the string *s*. Using vowel_frequencies dictionary and a max accumulation pattern determine the most common vowel and assign the result to the variable *common_vowel*.  Print the variable *common_vowel*.

# %%
s = "singing in the rain and playing in the rain are two entirely different situations but both can be good fun"
vowels = ['a','e','i','o','u']
vowel_frequencies = {}
for char in s:
    if char in vowels:
        if char in vowel_frequencies:
            vowel_frequencies[char] += 1
        else:
            vowel_frequencies[char] = 1

highest_count = 0
for vowel in vowel_frequencies.keys():
    if vowel_frequencies[vowel] > highest_count:
        common_vowel = vowel
        highest_count = vowel_frequencies[vowel]

print(common_vowel, ": ", highest_count)

# %% [markdown]
# # Problem 8
# The string *january_temp_data* contains January temperature information for Ann Arbor for the years 2016 to 2000. The string *january_temp_data* is formatted so that it consists of multiple lines.  Each line is composed of three “columns” separated by commas. 
# 1. Year.
# 2. Lowest temperature.
# 3. Highest temperature.
# Write code that will create two dictionaries: *january_lows* and *january_highs*.  The dictionary *january_lows* maps a year to the lowest temperature.  The dictionary *january_highs* maps a year to the higest temperature. In both dictionaries, the keys should be integers (for each year) and the values should be integers for the temperatures.
# 
# Each set of values in the string is separated by a new-line character.  You must use .split('\n') to split the lines of january_temp_data into a list. This results in a list of strings where each string holds the three columns.  YOu must then use .split(',') to split a given line into a list containing the three column values. Use int() to cast strings to integers.
# 
# Print the variables *january_lows* and *january_highs*.

# %%
january_lows = {}
january_highs = {}

january_temp_list = january_temp_data.split('\n')
for year in january_temp_list:
    current_year = year.split(',')
    january_lows[int(current_year[0])] = int(current_year[1])
    january_highs[int(current_year[0])] = int(current_year[2])
    
print(january_lows)
print(january_highs)

# %% [markdown]
# # Problem 9
# Again using he string *january_temp_data*, write code that will determine which year had the largest difference between the lowest and highest temperature. Store the year as an integer in the variable  *biggest_temp_diff_year* and temperature difference is the variable *biggest_temp_diff*.  Print both *biggest_temp_diff_year* and *biggest_temp_diff*.
# 
# You need use much of the code from the above problem to parse the into the three values: year, lowest temperature, and the highest temperature.  Write additional code to calculate the temperature difference and use a max accumulation pattern tp determine the year with the largest temperature difference.

# %%
biggest_temp_diff = 0

for year in january_highs.keys():
    year_temp_diff = january_highs[year]-january_lows[year]
    if year_temp_diff > biggest_temp_diff:
        biggest_temp_diff = year_temp_diff
        biggest_temp_diff_year = year
        
print(biggest_temp_diff_year, ": ", biggest_temp_diff)

# %%



