#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:51:27 2020

@author: tiwari13
"""

#Setting up current directory
#import os
#os.getcwd()
# '/home/tiwari13'
#os.chdir('/home/tiwari13/ABE65100/07-graphical-analysis-with-python-roccabye')

#The directory where Input csv (Earthquake_30day.csv)file is stored.
pathname = "/home/tiwari13/ABE65100/07-graphical-analysis-with-python-roccabye/Input/Earthquake_30day.csv"

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

# 1. Open and read the contents of the file into Python.
data= pd.read_table(pathname, sep= ',', header=0)
Earthquake_30day = data.dropna(axis=0, subset =['mag'])                       # remove the rows with NaN values

# 2. Using matplotlib conduct the following graphical analysis of the data:

'''Generate a histogram of earthquake magnitude, using a bin width of 1 and a range of 0 to 10. 
(hint: how does the selction of bin size and range affect what the historgram displays? 
what does the histogram suggest about the distribution of the data?)
'''

plt.hist(Earthquake_30day['mag'], bins= list(range(0,11)), facecolor ='pink', 
         edgecolor= 'black', alpha = 0.5)                                     # Plot histogram with bin width 1 with range of 0 and 10
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Magnitude of Earthquake', fontsize=15)                                         # Label x-axis
plt.ylabel('Count', fontsize=15)                # Label y-axis
plt.title('Histogram of Earthquake Magnitude \nfrom Feb. 01 to March 02, 2020', fontsize=16) # Title
plt.savefig("/home/tiwari13/ABE65100/07-graphical-analysis-with-python-roccabye/Output/Histogram.png")
plt.close()

'''Generate a KDE plot for the same data. 
(hint: indicate selections for the kernel type and kernel width, and comment on 
similarities and differences between the histogram and the KDE plot)
'''
# kernel type is gaussian to generate denesity kernel = 'gau'
# kernel width is 0.2 'bw =0.2'
sns.kdeplot(Earthquake_30day['mag'],kernel ='gau', bw = 0.2, color = 'r', shade = True, label = 'Earthquake Magnitude') 
plt.xlabel('Magnitude', fontsize=15)
plt.ylabel('Density', fontsize=15)
plt.title('KDE Plot for Magnitude', fontsize=16)
print("Kernel Type: Gaussian; Kernel Width: 0.2")
plt.savefig("/home/tiwari13/ABE65100/07-graphical-analysis-with-python-roccabye/Output/KDE.png")
plt.close()

'''
Plot latitude versus longitude for all earthquakes. 
(hint: comment on the distribution of those points. 
be sure that you put longitude on the x-axis and latitude on the y-axis, why?)
'''
plt.plot(Earthquake_30day["longitude"], Earthquake_30day["latitude"], 'r^') #Display plot
plt.xlabel('Longitude', fontsize=15)
plt.ylabel('Latitude', fontsize=15)
plt.title('Distribution of Earthquakes', fontsize=16)
plt.savefig("/home/tiwari13/ABE65100/07-graphical-analysis-with-python-roccabye/Output/Earthquake_Distribution.png")
plt.close()

'''
Generate a normalized cumulative distribution plot of earthquake depths. 
(hint: comment on what this plot indicates about the distribution of earthquake depths)
'''
 
plt.hist(Earthquake_30day['depth'], bins= 600,color = 'tab:orange',
                          cumulative=True, histtype ='step')                  # Plot CDF for earhquake depths
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Depth (km)', fontsize=10)                                         # Label x-axis
plt.ylabel('Cumulative Frequency', fontsize=10)                               # Label y-axis
plt.title('Normalized Cumulative Distribution \nof Earthquake Depths from Feb. 01 to March 02, 2020', 
          fontsize=10, wrap = 'True')                                         # Title
plt.savefig("/home/tiwari13/ABE65100/07-graphical-analysis-with-python-roccabye/Output/CDF.png")
plt.close()

'''
Generate a scatter plot of earthquake magnitude (x-axis) with depth (y-axis). 
(hint: comment on how depth and magnitude are related)
'''

# Scatter plot of Depth vs. Magnitude of Earthquakes
plt.scatter(Earthquake_30day['mag'], Earthquake_30day['depth'], 
            c= 'coral', marker="^")                                           # Scatter plot
plt.xlabel('Magnitude of Earthquakes',fontsize=15)
plt.ylabel('Depth (km)', fontsize=15)
plt.title('Depth vs. Magnitude',fontsize=16)
plt.savefig("/home/tiwari13/ABE65100/07-graphical-analysis-with-python-roccabye/Output/Scatter.png")
plt.close()

'''
Generate a quantile or Q-Q plot of the earthquake magnitudes. 
(hint: what statistical distribution does your Q-Q plot assume?
does your data comply with that distribution?)
'''

stats.probplot(Earthquake_30day['mag'], plot= plt, dist='norm')               # Q-Q plot for the magnitude of earthquakes
plt.xlabel('Theoretical Quantiles',fontsize=15)
plt.ylabel('Sample Quantiles', fontsize=15)
plt.title('Normal Q-Q Plot',fontsize=16)
plt.savefig("/home/tiwari13/ABE65100/07-graphical-analysis-with-python-roccabye/Output/Q-Qplot.png")
plt.close()
