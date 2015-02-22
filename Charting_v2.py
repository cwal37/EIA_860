# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 11:14:26 2015

@author: Connor
"""

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import pdb

def scatterByZ(df, xname, yname, Zname, Zspecific, yunit, xunit, diagline, save = True, save_loc = r"./"):
    
    #df = df[df['Exclusion'] == 0]    
    if Zspecific == "no":
        title = xname + " vs. " + yname
    else:
        title = Zspecific + ": " + xname + " vs. " + yname
    filename = xname + " vs. " + yname + "(" + Zspecific +").png"    
    
    Zfield = df[Zname]
    xfield = df[xname]
    yfield = df[yname]
    
    setlist = list(Zfield)
    Zset = set(setlist)
    Zsetlist = list(Zset)
    Zlength = len(Zsetlist)
    
    xlim_max = np.amax(xfield) + 1
    xlim_min = np.amin(xfield) - 1
    ylim_max = np.amax(yfield) + 1
    ylim_min = np.amin(yfield) - 1
   
    colors = cm.spectral(np.linspace(0,1,len(Zsetlist)))
    
    labellist = list()
    
    fig, ax = plt.subplots() 
    
    if Zspecific == "no":
        i=0      
        for i in range (0, Zlength):
            newdf = df[df[Zname]==Zsetlist[i]]
    
            a = ax.scatter(newdf[xname], newdf[yname], c = colors[i], label=Zsetlist[i], s = 25)
            a.set_alpha(0.65)        
            plt.legend(loc = 2, title=Zname)
            labellist.append(Zsetlist[i])  
            
            xlm,xlx = plt.xlim(xlim_min,xlim_max)
            ylm,ylx = plt.ylim(ylim_min,ylim_max)
               
            i = i+1
    if Zspecific != "no":
            newdf = df[df[Zname]!=Zspecific]
            a = ax.scatter(newdf[xname], newdf[yname], c = 'lightgray', edgecolor = 'none', label="All", s = 25, alpha = 0.8)
            a.set_alpha(0.65)        
            plt.legend(loc = 2, title=Zname)
           
            Zdf = df[df[Zname]==Zspecific]
            a = ax.scatter(Zdf[xname], Zdf[yname], c = 'b', label=Zspecific, s = 25)
            a.set_alpha(0.65)        
            plt.legend(loc = 2, title=Zname)
            
            xlm,xlx = plt.xlim(xlim_min,xlim_max)
            ylm,ylx = plt.ylim(ylim_min,ylim_max)
    
    if diagline =='yes':
        plt.plot([0, 15000], [0, 15000], ls="--", c=".3")
        
    plt.title(title)
    if xunit != "":
        plt.xlabel(xname + "(" + xunit + ")")
    else:
        plt.xlabel(xname)
        
    if yunit != "":
        plt.ylabel(yname + "(" + yunit + ")")
    else:
        plt.ylabel(yname)
        
    if save == True:
        #plt.savefig(save_loc + filename, dpi = 400, bbox_inches = 'tight')
        plt.savefig(save_loc + filename, bbox_inches = 'tight')
        plt.close()
        #plt.clf()
    else: return plt
    
def lineByZ(df, xname, yname, Zname, Zspecific, yunit, xunit, diagline, save = True, save_loc = r"./"):
    
    #df = df[df['Exclusion'] == 0]    
    if Zspecific == "no":
        title = xname + " vs. " + yname
    else:
        title = Zspecific + ": " + xname + " vs. " + yname
    filename = xname + " vs. " + yname + "(" + Zspecific +").png"    
    
    Zfield = df[Zname]
    xfield = df[xname]
    yfield = df[yname]
    
    setlist = list(Zfield)
    Zset = set(setlist)
    Zsetlist = list(Zset)
    Zlength = len(Zsetlist)
    
    xlim_max = np.amax(xfield)
    xlim_min = np.amin(xfield)
    ylim_max = np.amax(yfield) * 1.01
    ylim_min = 0 #np.amin(yfield) * 0.99
   
    colors = cm.spectral(np.linspace(0,1,len(Zsetlist)))
    
    labellist = list()
    
    fig, ax = plt.subplots() 
    
    if Zspecific == "no":
        i=0      
        for i in range (0, Zlength):
            newdf = df[df[Zname]==Zsetlist[i]]
    
            a = ax.plot(newdf[xname], newdf[yname], linestyle = '-', c = colors[i], label=Zsetlist[i])
            #a.set_alpha(0.65)        
            plt.legend(loc = 2, title=Zname)
            labellist.append(Zsetlist[i])  
            
            xlm,xlx = plt.xlim(xlim_min,xlim_max)
            ylm,ylx = plt.ylim(ylim_min,ylim_max)
               
            i = i+1
    if Zspecific != "no":
            newdf = df[df[Zname]!=Zspecific]
            a = ax.plot(newdf[xname], newdf[yname], c = 'lightgray', edgecolor = 'none', label="All", alpha = 0.8)
            a.set_alpha(0.65)        
            plt.legend(loc = 2, title=Zname)
           
            Zdf = df[df[Zname]==Zspecific]
            a = ax.plot(Zdf[xname], Zdf[yname], c = 'b', label=Zspecific)
            a.set_alpha(0.65)        
            plt.legend(loc = 2, title=Zname)
            
            xlm,xlx = plt.xlim(xlim_min,xlim_max)
            ylm,ylx = plt.ylim(ylim_min,ylim_max)
    
    if diagline =='yes':
        plt.plot([0, 15000], [0, 15000], ls="--", c=".3")
        
    plt.title(title)
    if xunit != "":
        plt.xlabel(xname + "(" + xunit + ")")
    else:
        plt.xlabel(xname)
        
    if yunit != "":
        plt.ylabel(yname + "(" + yunit + ")")
    else:
        plt.ylabel(yname)
        
    if save == True:
        #plt.savefig(save_loc + filename, dpi = 400, bbox_inches = 'tight')
        plt.savefig(save_loc + filename, bbox_inches = 'tight')
        plt.close()
        #plt.clf()
    else: return plt




def barByX(df, xname, yvar, title, xlabel, save = True, save_loc = r"./"):
    
    #pdb.set_trace()
    
    df = df[df['Exclusion'] == 0]    

    #title = xname 
    filename = xname + ".png"    
    
    xfield = df[xname]
    setlist = list(xfield)
    xset = set(setlist)
    xsetlist = list(xset)    
    xlength = len(xsetlist)    
    
    ind = np.arange(xlength)  
    
    fig, ax = plt.subplots() 
    
    grouped = df.groupby(xname)
    percentages =  (grouped[yvar].agg([np.sum]) / grouped['Fitted'].agg([np.sum]))*100
    
    percentages = percentages['sum']      
    
    plt.bar(range(len(percentages)), percentages)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.xticks(ind, percentages.index, rotation = 37)
    plt.xlim(0,xlength)
    if save == True:
       # plt.savefig(save_loc + filename, dpi = 400, bbox_inches = 'tight')
        plt.savefig(save_loc + filename, bbox_inches = 'tight')
        plt.close()
        #plt.clf()
    else: return plt