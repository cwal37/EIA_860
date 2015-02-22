# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 15:21:04 2015

@author: Connor
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from Charting_v2 import *
import os

# configure run
output_location = r"./2012_results/"


# load all data
base_data = pd.read_excel(r'./GeneratorY2012.xls', 'Operable', skiprows=1)

#print list(base_data.columns.values)


# clean data based on desired analysis parameters
working = base_data
working = working[working['Operating Year'] > 1992]

renewables = ['HA', 'HB', 'HK', 'PV', 'WT', 'WS', 'FC']
traditional = ['ST', 'GT', 'IC', 'CA', 'CT', 'CS', 'CC', 'HY', 'BT']
storage = ['BA', 'CE', 'CE', 'FW', 'ES', 'CP', 'PS']

renew_data = working

for tech in traditional:
    renew_data = renew_data[renew_data['Prime Mover'] != tech]

for tech in storage:
    renew_data = renew_data[renew_data['Prime Mover'] != tech]


year = 1992

years = range(1992, 2013) 

for year in range (1992, 2013):
    
    current_year = renew_data[renew_data['Operating Year'] == year]    
        
    for tech in renewables:
        cap_add = 
    
    year = year + 1

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

PMs = renewables.groupby("Prime Mover")
#op_year = PMs.groupby('Operating Year')
capacities = op_year.sum()

Technologies = PMs.groups.keys()
renewables = renewables.sort(['Operating Year'])
#print Technologies
#print PMs
#
for technology in Technologies:
    scatterByZ(renewables, 'Operating Year', 'Nameplate Capacity (MW)', 'Prime Mover', 'no', 'Tech','MW', 'yes', save_loc = output_location)
#


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


##
#plt.hist(res, bins = 10)
##plt.show()
#plt.savefig('hist of res.png')
#plt.close()
#
#plt.hist(ans_res, bins = 10)
##plt.show()
#plt.savefig('hist of anscombe res.png')
#plt.close()
#
#
#plt.hist(dev_res, bins = 10)
##plt.show()
#plt.savefig('hist of deviance res.png')
#plt.close()

#
##plot results
#
if not os.path.exists(output_location): 
    os.makedirs(output_location)
#
#scatterByZ(working, 'Fitted', yvar, 'Utility', 'high','$1000s','$1000s', 'no', save_loc = output_location)

#aaa = working.groupby("Utility")
#utilities = aaa.groups.keys()
#utilities.sort()
#
#for utility in utilities:
#    scatterByZ(working, 'Fitted', yvar, 'Utility', utility, '$1000s','$1000s', 'yes', save_loc = output_location)
#
#for xvar in xvars:
#    scatterByZ(working, xvar, 'residuals', 'Turbine', 'no', '','', 'no', save_loc = output_location)
#    scatterByZ(working, xvar, 'residuals', 'PeerGroup','no','','', 'no', save_loc = output_location)


#barByX(working, 'Utility', yvar, 'Utility Actual/Predicted', 'Utility', save_loc = output_location)

#renew_data = working[working['Prime Mover'] != traditional]
#renewables = renewables[renewables['Prime Mover'] != 'BA']
#renewables = renewables[renewables['Prime Mover'] != 'CE']
#renewables = renewables[renewables['Prime Mover'] != 'FW']
#renewables = renewables[renewables['Prime Mover'] != 'GT']
#renewables = renewables[renewables['Prime Mover'] != 'IC']
#renewables = renewables[renewables['Prime Mover'] != 'CA']
#renewables = renewables[renewables['Prime Mover'] != 'CT']
#renewables = renewables[renewables['Prime Mover'] != 'CS']
#renewables = renewables[renewables['Prime Mover'] != 'CC']
#renewables = renewables[renewables['Prime Mover'] != 'CE']
#renewables = renewables[renewables['Prime Mover'] != 'BT']