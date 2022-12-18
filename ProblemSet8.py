# %% [markdown]
# # A Note About Testing
# As you write code in any cell, add print statements, so you can see whether your code is working correctly. Never make assumuptions to what a variable contains.  Use print statements liberally to see the values and the type of a variable.  We are deliberately starting to remove some of the "scaffolding" that we have been providing, putting more responsibility on you to figure out whether your code is right.

# %% [markdown]
# # Run this cell first 
# This will import the csv and json modules and build a list of dictionaries call *umich_buildings*. These data structures are used in later problems.

# %%
# do all our imports at the top of the file, because that's the standard style
import csv
import json
from ps8_vincenty import latLngDistanceMeters

fh = open('ps8_umich_buildings.json','r')
umich_buildins_str = fh.read()
umich_buildings = json.loads(umich_buildins_str) 


baby_file = open('ps8_us-common-baby-names.csv','r')
baby_reader = csv.DictReader(baby_file)
baby_names = list(baby_reader) # turn the reader object into a real list

# %% [markdown]
# The variable *umich_buildings* is list where each element is a dictionary.  The keys in the dictionary contained in each list element are: 
# 
# <table>
#   <tr>
#     <th style="text-align: center">Key</th>
#     <th style="text-align: center">Description</th> 
#   </tr>
#   <tr>
#     <td style="text-align: center">address</td>
#     <td  style="text-align: left">The address of the building</td> 
#   </tr>
#   <tr>
#     <td style="text-align: center">id</td>
#     <td  style="text-align: left">The building id, e.g.,asb is Administrative Services Building </td> 
#   </tr>
#   <tr>
#     <td style="text-align: center">lat</td>
#     <td  style="text-align: left">The geographic latitude,i.e., north-south position of a point on the Earth's surface</td> 
#   </tr>
#   <tr>
#     <td style="text-align: center">lng</td>
#     <td  style="text-align: left">The geographic longitude,i.e.,the angular distance of a place east or west of the meridian at Greenwich, England</td> 
#   </tr>
#   <tr>
#     <td style="text-align: center">name</td>
#     <td  style="text-align: left">The building name</td> 
#   </tr>
# </table>
# 
# Below is typical element in the list:  
# {  
# &nbsp;&nbsp;&nbsp;&nbsp;"address": "1201 South Main Street Ann Arbor, MI 48104-3722",  
# &nbsp;&nbsp;&nbsp;&nbsp;"id": "stadm",  
# &nbsp;&nbsp;&nbsp;&nbsp;"lat": 42.265071,  
# &nbsp;&nbsp;&nbsp;&nbsp;"lng": -83.748662,  
# &nbsp;&nbsp;&nbsp;&nbsp;"name": "Michigan Stadium"  
# }  

# %% [markdown]
# # Problem 1
# Write a function named *buildingLatLong_* that returns a (latitude, longitude) tuple for any building id in *umich_buildings*. You will need to iterate through each list element, then for each list element compare the value associated with the id key to the value passed to the function. If that building id could not be found, return *None*.

# %%
def buildingLatLong(building_id):
    for dictionary in umich_buildings:
        if dictionary['id'] == building_id:
            return (dictionary['lat'],dictionary['lng'])
    return None
    
print(buildingLatLong('ccrb'))

# %% [markdown]
# For building id ccrb the output should be:  (42.278866, -83.732666)

# %% [markdown]
# # Problem 2
# Write a function named _*buildingName_* that accepts a building id as a parameter and returns the associated building name. If that building ID could not be found, return *None*.

# %%
def buildingName(building_id):
    for dictionary in umich_buildings:
        if dictionary['id'] == building_id:
            return dictionary['name']
    return None
print(buildingName('ccrb'))

# %% [markdown]
# For building id ccrb the output should be:  Central Campus Recreation Building

# %% [markdown]
# # Problem 3
# "Vincenty's formulae are two related iterative methods used to calculate the distance between two points on the surface of a spheroid, developed by Thaddeus Vincenty (1975a)"
# 
# The file *vincenty.py*, which was imported in the first cell, contains code that calculates the "vincenty distance" between two points' using the latitude and longitude of both points. The function *latLngDistanceMeter*, present in vincenty.py, accepts two tuples as paramters where each tuple contains the coordinates (latitude,longitude) of a point on the Earth and performs the vincenty calculation.  Below is an example of how this function is called:
# 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latLngDistanceMeters((42.3584, -71.0912), (42.278, -83.7382))
# 
# Write a function named _*buildingDistance*_ that is passed two building IDs and determines the vincenty distance between two building IDs.

# %%
def buildingDistance(building1_id, building2_id):
    for dictionary in umich_buildings:
        if dictionary['id'] == building1_id:
            loc1 = (dictionary['lat'], dictionary['lng'])
    for dictionary in umich_buildings:
        if dictionary['id'] == building2_id:
            loc2 = (dictionary['lat'], dictionary['lng'])
            
    return latLngDistanceMeters(loc1,loc2)

vdistance = buildingDistance('nq','stadm')
print("The vincenty distance between building nq and stadm:",vdistance)

# %% [markdown]
# # Problem 4: 
# Write code that iterates over *umich_buildings* and outputs a *.csv* file called *north_quad_distance.csv*. The csv file has two columns: The first column is the *building name* and the second column is the vincenty distance of that building from North Quad(nq). Since this is a csv file the first row identifies the columns.  So, column 1 of the first row has the value "Name" and column 2 has the value "Distance from NQ". There should be one subsequent row for each building (including North Quad, which should have a zero distance).  You should use the string .format() function to format each row in the csv file.
# 
# Check your work by opening the .csv file in a text editor and importing it into a spreadsheet program like Excel or Google Sheets.
# 
# You file should appear similar to that below:  
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name,Distance from NQ  
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1000 Victors Way,4674.366005  
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1032 Greene Building,1498.650608  
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;523 South Division Building,639.5818755  
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Administrative Services Building,1410.470849  

# %%
csvfile = open('north_quad_distance.csv',"w",newline='')
loc_format = '{},{}'
writer = csv.writer(csvfile)
writer.writerow(['Name','Distance from NQ'])
for location in umich_buildings:
    distance = buildingDistance('nq',location['id'])
    writer.writerow([loc_format.format(location['name'],distance)])
csvfile.close()

# %% [markdown]
# This next problem uses the list *baby_names* loaded from us-common-baby-names.csv (see first cell). Each element in the list is an OrderedDict object which is just like a dictionary except the elements are ordered in creation sequence.  This means that you may treat *baby_names* as a list where each element in the list is a dictionary.  A sample row appears as below.
# 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OrderedDict([('year', '1880'),('name', 'John'),('percent', '0.081541'),('sex', 'boy')])
#              
# The *percent* key holds a percentage value which represents the number of babies born that year who were given the name found in the value of the name key.  

# %% [markdown]
# # Problem 5
# Write the function *popularInYear* that accepts the integer parameter *year* and returns the most popular name for that year. The most popular name is the one with the largest percentage.  This problem is essentially finding the maximum percentage in a subset of the baby_names list that match the year parameter.  

# %%
def findMostPopularName(year):
    max_perc = 0.0
    for baby in baby_names:
        if (baby['year'] == year) and (float(baby['percent']) > float(max_perc)):
            max_perc = baby['percent']
            pop_baby = baby
    return pop_baby

year = '1967'
mostPopular = findMostPopularName(year)
percent = round(float(mostPopular['percent'])*100,2)
print('Most popular name in',year,'is',mostPopular['name'],'with',percent,'percent')

# %% [markdown]
# ## Nested Data and Nested Iteration
# Many web services return information either in a json or xml format.  Below is sample json return by the Facebook API and is representative in structure of the json returned by most web services.  You will be working complex nested data in future modules.  This problem will serve as a warmup for those future problem sets.
# 
# First, just get familiar with the structure of the data. You may want to copy and paste it to a site like https://jsoneditoronline.org/ so you may inspect the data.
# 
# Run the cell below before proceeding to the problems.

# %%
fb_data = {
 "data": [
  {
    "id": "2253324325325123432madeup", 
    "from": {
      "id": "23243152523425madeup", 
      "name": "Jane Smith"
    }, 
    "to": {
      "data": [
        {
          "name": "Your Facebook Group", 
          "id": "432542543635453245madeup"
        }
      ]
    }, 
    "message": "This problem might use the accumulation pattern, like many problems do", 
    "type": "status", 
    "created_time": "2014-10-03T02:07:19+0000", 
    "updated_time": "2014-10-03T02:07:19+0000"
  }, 
 
  {
    "id": "2359739457974250975madeup", 
    "from": {
      "id": "4363684063madeup", 
      "name": "John Smythe"
    }, 
    "to": {
      "data": [
        {
          "name": "Your Facebook Group", 
          "id": "432542543635453245madeup"
        }
      ]
    }, 
    "message": "Here is a fun link about programming", 
    "type": "status", 
    "created_time": "2014-10-02T20:12:28+0000", 
    "updated_time": "2014-10-02T20:12:28+0000"
  }]
}

# %% [markdown]
# ## Problem 6
# Extract the contents of the first message into a variable called *first_message*.  Print *first_message*.

# %%
first_message = fb_data['data'][0]['message']
print(first_message)

# %% [markdown]
# Output should be: This problem might use the accumulation pattern, like many problems do

# %% [markdown]
# # Problem 7
# Extract the name of the author of the second post, into a variable called *second_name*.  Print *second_name*.

# %%
second_name = fb_data['data'][1]['from']['name']
print(second_name)

# %% [markdown]
# Output should be: John Smythe

# %% [markdown]
# # Problem 8
# Write code that generates a list of the names of all the senders of the messages in fb_data. Store it in a variable called *senders*.  Print the variable *senders*.

# %%
senders = []
for data in fb_data['data']:
    senders.append(data['from']['name'])
print(senders)

# %% [markdown]
# Should be: `['Jane Smith', 'John Smythe']`

# %% [markdown]
# # Tests
# 

# %%
# PROBLEM 1 TESTS

passed_test_1 = False
if umich_buildings and len(umich_buildings) == 161:
    first_building = {'lat': 42.238815, 'lng': -83.73215, 'id': '1000v', 'name': '1000 Victors Way', 'address': '1000 Victors Way'}
    building_zero = umich_buildings[0]
    if building_zero['name'] == first_building['name'] and building_zero['id'] == first_building['id']:
        print('[P1] GOOD! umich_buildings seems to be properly loaded')
        passed_test_1 = True
    else:
        print('[P1] umich_buildings does not seem to have the expected buildings')
else:
    print('[P1] umich_buildings does not seem to contain the expected list of 161 buildings')

# PROBLEM 2 TESTS

if passed_test_1:
    LL = buildingLatLong('nq')
    if LL:
        lat,lng = LL
        if abs(lat-42.280477)+abs(lng - (-83.740131)) < 0.01:
            if buildingLatLong('xxxx') == None:
                print('[P2] GOOD! The latitude and longitude fetching function seems to work')
            else:
                print('[P2] When a building ID does not appear, be sure buildingLatLong returns None')
        else:
            print('[P2] The buildingLatLong function does not appear to return the correct value')
    else:
        print('[P2] buildingLatLong when called on nq does not appear to return the correct value')


# PROBLEM 3 TESTS
if passed_test_1:
    if buildingName('nq') == 'North Quadrangle':
        if buildingName('xxxx') == None:
            print('[P3] GOOD! The name fetching function seems to work')
        else:
            print('[P3] When a building ID does not appear, be sure buildingName returns None')
    else:
        print('[P3] The buildingName function does not appear to return the correct value')

# PROBLEM 4 TESTS
if passed_test_1:
    # checking that the distance from North Quad to Michigan Stadium is about 1.1 miles
    D = buildingDistance('nq', 'stadm')
    if type(D) == type(0.0):
        if abs(D - 1850.34173428) < 0.01:
            if buildingDistance('nq', 'nq') < 0.01:
                print('[P4] GOOD! The distance computation seems to work')
            else:
                print('[P4] Unexpected value for building distance in our test case')
        else:
            print('[P4] Unexpected value for building distance in our test case')
    else:
        print('[P4] be sure that buildingDistance returns a float')

# PROBLEM 5 TESTS
if passed_test_1:
    north_quad_closest = ['Modern Languages Building', 'Rackham School of Graduate Studies, Horace H.', 'Hamilton Square']
    stadium_closest = ['Crisler Center', 'William Davidson Player Development Center', 'Facilities Services Building B', 'Transportation Services Building']
    if closestBuildingNames('stadm', 4) == stadium_closest and closestBuildingNames('nq') == north_quad_closest:
        print('[P5] GOOD! The closest buildings list seems to work')
    else:
        print('[P5] Unexpected value for building distance in our test case')

# PROBLEM 6 TESTS
f = open('north_quad_distance.csv', 'r')
reader = csv.DictReader(f)
row = list(reader)[0]
if 'name' not in row:
    print("[P6] 'name' field not present in .csv file")
elif 'distance_from_nq' not in row:
    print("[P6] 'distance_from_nq' field not present in .csv file")
elif row['name'] != '1000 Victors Way':
    print("[P6] first building is not 1000 Victors Way")
else:
    print("[P6] GOOD! You seem to have written out the .csv file correctly")
f.close()
        
print('== RUNNING PART 2 TESTS ==')
propery_loaded_baby_names = False

if len(baby_names) == 25800 and len(baby_names[0])==4:
    propery_loaded_baby_names = True
else:
    print('Be sure that you are properly loading us-common-baby-names.csv')

# PROBLEM 7 TESTS
if propery_loaded_baby_names:
    popular_in_1980 = ['Michael', 'Jennifer', 'Christopher']
    popular_in_1990 = ['Michael', 'Christopher', 'Jessica', 'Ashley', 'Matthew', 'Joshua', 'Brittany', 'Amanda', 'Daniel', 'David']

    if popularInYear(1980) == popular_in_1980 and popularInYear(1990, 10) == popular_in_1990:
        print('[P7] GOOD! popularInYear seems to work')
    else:
        print('[P7] Be sure that popularInYear is correctly sorting names by popularity')

# PROBLEM 8 TESTS
if propery_loaded_baby_names:
    stephen_popular = [1951, 1952, 1949, 1950, 1953, 1955, 1954, 1956, 1948, 1957,
    1967, 1958, 1968, 1947, 1969, 1966, 1970, 1965, 1959, 1960, 1961, 1962, 1964,
    1963, 1971, 1946, 1972, 1984, 1985, 1945, 1983, 1974, 1986, 1973, 1975, 1976,
    1987, 1988, 1978, 1977, 1982, 1944, 1989, 1990, 1981, 1979, 1943, 1980, 1942,
    1991, 1941, 1992, 1993, 1940, 1994, 1995, 1996, 1939, 1997, 1998, 1938, 1999,
    1914, 1915, 1912, 1913, 1916, 1911, 2000, 1917, 1937, 1909, 1918, 1936, 1907,
    1905, 1908, 1910, 1919, 1882, 1921, 1920, 1897, 1902, 1903, 1899, 1886, 1887,
    1880, 1898, 1888, 1885, 1881, 1884, 1883]

    bob_popular = [1934, 1936, 1932, 1935, 1933, 1931, 1937, 1930, 1939, 1938,
    1929, 1928, 1940, 1927]

    jill_popular = [1966, 1968, 1967, 1965, 1977, 1969, 1970, 1964, 1975, 1978, 1976, 1971, 1974, 1963, 1962, 1979, 1972, 1961, 1973, 1960, 1959, 1980, 1958, 1957, 1981, 1982, 1983]

    if nameMostPopularYears('Stephen', 100) == stephen_popular and nameMostPopularYears('Bob', 100) == bob_popular and nameMostPopularYears('Jill', 100) == jill_popular:
        print('[P8] GOOD! nameMostPopularYears is giving what we expect')
    else:
        print('[P8] nameMostPopularYears does not seem to produce what we expect')
        
# PROBLEM 9 TESTS
if first_message == 'This problem might use the accumulation pattern, like many problems do':
    print('[P9] GOOD!')
else:
    print('[P9] first_message has the wrong value')

# PROBLEM 10 TESTS
if second_name == 'John Smythe':
    print('[P10] GOOD!')
else:
    print('[P10] second_name has the wrong value')
    
# PROBLEM 11 TESTS
if senders == ['Jane Smith', 'John Smythe']:
    print('[P11] GOOD!')
else:
    print('[P11] senders has the wrong value')

# %%



