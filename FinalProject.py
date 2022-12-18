# %%
import json
import pandas as pd

file = open('FBI_CrimeData_2016.json')
crime_list_file = file.read()
crime_list = json.loads(crime_list_file)
      
murder_by_region = accum_crime('Region', 'Murder', crime_list)
violent_by_region = accum_violent_crime('Region', crime_list)
nonviolent_by_region = accum_nonviolent_crime('Region', crime_list)

print("Murders by Region")
print_dict(murder_by_region)
print("Violent Crimes by Region")
print_dict(violent_by_region)
print("Nonviolent Crimes by Region")
print_dict(nonviolent_by_region)

violent_by_state = accum_violent_crime('State', crime_list)
crime_sum = 0
for key in violent_by_state:
    crime_sum += violent_by_state[key]
    
mean = crime_sum/51
output_format = '{0:<20} {1:>7} {2:>19}'
print('National Average Violent Crime ', mean)
print(output_format.format('State','Crimes','Distance From Mean'))
for key in violent_by_state:
    print(output_format.format(key, violent_by_state[key], violent_by_state[key] - mean))

# %%
def accum_crime(key, crime, crime_list):
    data = {}
    for dictionary in crime_list:
        if not (dictionary[key] in data):
            data[dictionary[key]] = 0
            
        data[dictionary[key]] += int(dictionary[crime])
        
    return data

# %%
def accum_nonviolent_crime(key, crime_list):
    data = {}
    for dictionary in crime_list:
        if not (dictionary[key] in data):
            data[dictionary[key]] = 0
            
        data[dictionary[key]] += int(dictionary['Burglary']) + int(dictionary['Theft']) + int(dictionary['Vehicle_Theft'])
        
    return data

# %%
def accum_violent_crime(key, crime_list):
    data = {}
    for dictionary in crime_list:
        if not (dictionary[key] in data):
            data[dictionary[key]] = 0
            
        data[dictionary[key]] += int(dictionary['Assault']) + int(dictionary['Rape']) + int(dictionary['Robbery']) + int(dictionary['Murder'])
        
    return data

# %%
def print_dict(dictionary):
    amount = list(dictionary.values())
    region = list(dictionary.keys())
    pdDict = {"Region":pd.Series(region), "Incidents":pd.Series(amount)}
    df = pd.DataFrame(pdDict)
    print(df)
    df.plot.bar(x='Region',y = 'Incidents', legend=False)
    

# %%



