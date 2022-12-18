# %%
#text file organized as follows
#1.State, 2.Region, 3.Population in millions, 4.GDP in billions, 5.Personal Income in billions,
#6.Subsidies in millions, 7.Compensation of Employees in billions, 8.Taxes on Productions and Imports in billions

state_data = open("Economic_Data_2010.txt","r")

region = input("Please enter Region Name: ")
empty_flag = False
states = []
population = {}
gdp = {}
income = {}
for line in state_data:
    data = line.split(',')
    if data[1] == region:
        states.append(data[0])
        population[data[0]] = float(data[2])
        gdp[data[0]] = float(data[3])
        income[data[0]] = float(data[4])
        empty_flag = True

if empty_flag:
    
    states.sort()
    region_states = ""
    for state in states:
        region_states += state + ", "
    region_states = region_states[:-2]
    
    print("Economic Statistics for the ", region, " region: ")
    print("States in Region:   ", region_states)
    print("Total Population:   ", round(calc_total_pop(population), 4), " million")
    print("Average Population: ", round(calc_total_pop(population)/len(states), 4), " million")
    print("Total GDP:          ", round(calc_total_gdp(gdp), 4), " billion")
    print("Average PI:         ", round((calc_total_phi(income)/calc_total_pop(population))*1000, 2))
else:
    print("Invalid Region")

state_data.close()

# %%
def calc_total_pop(pop_dict):
    total_pop = 0
    for key in pop_dict:
        total_pop += pop_dict[key]
    return total_pop

# %%
def calc_total_gdp(gdp_dict):
    total_gdp = 0
    for key in gdp_dict:
        total_gdp += gdp_dict[key]
    return total_gdp

# %%
def calc_total_phi(phi_dict):
    total_pi = 0
    for key in phi_dict:
        total_pi += phi_dict[key]
    return total_pi

# %%



