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

renewables = working[working['Prime Mover'] != 'ST']
renewables = renewables[renewables['Prime Mover'] != 'BA']
renewables = renewables[renewables['Prime Mover'] != 'CE']
renewables = renewables[renewables['Prime Mover'] != 'FW']
renewables = renewables[renewables['Prime Mover'] != 'GT']
renewables = renewables[renewables['Prime Mover'] != 'IC']
renewables = renewables[renewables['Prime Mover'] != 'CA']
renewables = renewables[renewables['Prime Mover'] != 'CT']
renewables = renewables[renewables['Prime Mover'] != 'CS']
renewables = renewables[renewables['Prime Mover'] != 'CC']
renewables = renewables[renewables['Prime Mover'] != 'CE']
renewables = renewables[renewables['Prime Mover'] != 'BT']

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

#print working['Utility ID']


##np.savetxt('O1O2M1.txt', O1O2M1)
##np.savetxt('plant.txt', plnt,  fmt = "%s")

##
#plt.scatter(Fitted, O1O2M1)
##plt.show()
#plt.savefig('plot of fitted v actual.png')
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
#scatterByZ(working, 'Fitted', yvar, 'res', 'low','$1000s','$1000s', 'no', save_loc = output_location)       

#scatterByZ(working, 'Fitted', yvar, 'Turbine', 'no','$1000s','$1000s', 'no', save_loc = output_location)
##scatterByZ(working, 'Fitted', yvar, 'PeerGroup', 'no','$1000s','$1000s', 'no' , save_loc = output_location)
##
#scatterByZ(working, 'ScaleFactor', yvar, 'PeerGroup', 'no','$1000s','$1000s', 'no' , save_loc = output_location)
#
#scatterByZ(working, 'Fitted', yvar, 'International', 'Not NA','$1000s','$1000s', 'no' , save_loc = output_location)
#
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
#    scatterByZ(working, xvar, 'pearson_residuals', 'Turbine', 'no','','', 'no', save_loc = output_location)
#    scatterByZ(working, xvar, 'pearson_residuals', 'PeerGroup','no','','', 'no', save_loc = output_location)
#    scatterByZ(working, xvar, 'deviance_residuals', 'Turbine','no','','', 'no', save_loc = output_location)
#    scatterByZ(working, xvar, 'deviance_residuals', 'PeerGroup','no','','', 'no', save_loc = output_location)
#    '$','',
#barByX(working, 'Turbine', yvar, 'Turbine Actual/Predicted', 'Turbine Technology', save_loc = output_location)
#barByX(working, 'PeerGroup', yvar, 'Peer Group Actual/Predicted', 'Peer Group', save_loc = output_location)
#barByX(working, 'Utility', yvar, 'Utility Actual/Predicted', 'Utility', save_loc = output_location)