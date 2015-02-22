# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 15:21:04 2015

@author: Connor
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

# configure run
output_location = r"./2012_results/"


# load all data
base_data = pd.read_excel(r'./GeneratorY2012.xls', 'Operable', skiprows=1)

#print list(base_data.columns.values)



working = base_data
working = working[working['Operating Year'] > 1992]

renewables = ['HA', 'HB', 'HK', 'PV', 'WT', 'WS', 'FC']
traditional = ['ST', 'GT', 'IC', 'CA', 'CT', 'CS', 'CC', 'HY', 'BT']
storage = ['BA', 'CE', 'CE', 'FW', 'ES', 'CP', 'PS']

renew_data = working
trad_data = working

for tech in traditional:
    renew_data = renew_data[renew_data['Prime Mover'] != tech]

for tech in storage:
    renew_data = renew_data[renew_data['Prime Mover'] != tech]

for tech in renewables:
    trad_data = trad_data[trad_data['Prime Mover'] != tech]
    
for tech in storage:
    trad_data = trad_data[trad_data['Prime Mover'] != tech]

# Renewable Generation Start

capacities = pd.DataFrame(columns=renewables)
year = 1992
years = range(1992, 2013) 
i = 0  
for year in range (1992, 2013):
    
    current_year = renew_data[renew_data['Operating Year'] == year]    
    
   
    for tech in renewables:

        cap_add = current_year[current_year['Prime Mover'] == tech]
        capacity = cap_add['Nameplate Capacity (MW)'].sum()
        capacities.loc[i, tech] = capacity        

    year = year + 1
    i = i + 1

capacities = capacities.drop(['HA', 'HB', 'HK', 'WS'], 1)

renew_tech = list(capacities.columns.values)

x = range (0,21)
years = list(years)
for tech in renew_tech:
    plt.plot(x, capacities[tech], linewidth = 2, label = tech, linestyle = '--', marker = 'd')
    plt.title('20 Years of Renewable Capacity Additions')
    plt.xticks(x, years, rotation = 60)
    plt.ylabel('MW')
    plt.xlabel('Year')
plt.legend(loc = 2)        
plt.savefig('20 Years of Renewable Capacity Additions.png', bbox_inches = 'tight')
plt.close()



# Traditional Generation Start

capacities = pd.DataFrame(columns=traditional)
year = 1992
years = range(1992, 2013) 
i = 0  
for year in range (1992, 2013):
    
    current_year = trad_data[trad_data['Operating Year'] == year]    
    
   
    for tech in traditional:

        cap_add = current_year[current_year['Prime Mover'] == tech]
        capacity = cap_add['Nameplate Capacity (MW)'].sum()
        capacities.loc[i, tech] = capacity        

    year = year + 1
    i = i + 1

#capacities = capacities.drop(['HA', 'HB', 'HK', 'WS'], 1)

trad_tech = list(capacities.columns.values)

x = range (0,21)
years = list(years)
for tech in trad_tech:
    plt.plot(x, capacities[tech], linewidth = 2, label = tech)
    plt.title('20 Years of Traditional Capacity Additions')
    plt.xticks(x, years, rotation = 60)
    plt.ylabel('MW')
    plt.xlabel('Year')
plt.legend(loc = 2)        
plt.savefig('20 Years of Traditional Capacity Additions.png', bbox_inches = 'tight')
plt.close()








#states = working['State']

#print sorted(set(list(working['State'])))

#prime_movers = working.groupby('Prime Mover')
#capacities = prime_movers.sum()
#capacities.sort()
#
#pm_caps = capacities['Nameplate Capacity (MW)']
#
#pm_list = sorted(set(list(working['Prime Mover'])))
#plt.bar(range(len(pm_caps)), pm_caps)
#plt.xlabel('Prime Mover')
#plt.ylabel('MW')
#plt.title('Sum of Capacities by Prime Movers for 2012 (MW)')
#plt.xticks(range(len(pm_list)), pm_list, rotation = 60)
#
#
#plt.savefig('ugly bar.png')
#plt.close()
#plt.legend(loc=2, title = capacities['Prime Mover'])



#prime_movers = working.groupby('Prime Mover')
#
#op_year = prime_movers.groupby('Operating Year')
#capacities = op_year.sum()
#capacities.sort()
#
#pm_caps = capacities['Nameplate Capacity (MW)']
#
#pm_list = sorted(set(list(working['Prime Mover'])))
#plt.bar(range(len(pm_caps)), pm_caps)
#plt.xlabel('Prime Mover')
#plt.ylabel('MW')
#plt.title('Sum of Capacities by Prime Movers for 2012 (MW)')
#plt.xticks(range(len(pm_list)), pm_list, rotation = 60)
#
#
#plt.savefig('ugly bar.png')
#plt.close()


#
if not os.path.exists(output_location): 
    os.makedirs(output_location)
