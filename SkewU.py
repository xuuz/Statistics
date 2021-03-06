# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Niam Moltta
# UY - 2017
# License: MIT
# Calculating Skewness Statistic

import pandas as pd
import matplotlib.pylab as plt
from sklearn import preprocessing
from scipy.stats import skew
import numpy as np
import seaborn
import re

print ' '
print ' '
print '                 Welcome to SkewU.py'
print '                 --by Niam Moltta--'
print '                      ~~/\//V\ '
print ' '
print ' '
print ' '
print 'Application: SKEWNESS CALCULATION.\n\nINSTRUCTIONS:\n\n- Select file, select column.\n- Returns skewness value.\n- Returns skewness representation graph.\n\n'

fhand = raw_input('Enter .csv file name: ')

if fhand == '':
    print ' '
    print 'Arrivederci!'
    print ' '
    exit()

print ' '

filehand = str(fhand)
data = pd.read_csv(filehand) 

frame = pd.DataFrame(data)

coolist = frame.columns
columns = np.asarray(coolist)

while True:

    print ' '
    print 'Columns in', re.findall('(.+?).csv', filehand), 'are:\n'
    print columns
    print ' '
    
    fh = raw_input('Enter column header: ')
    
    column = str(fh)

    if (column == '') | (column == 'ya'):
        break
    

    else:

        # Just in case, replace Missing Values with zero:
    
        data[column].fillna(0,inplace=True)
    
        print 'Missing values replaced with zeros.'
        print ' '
        
        Col = preprocessing.scale(data[column]) 
        
        skness = skew(Col)
        xlabel = str(skness) 
        figure = plt.figure()
        print 'Skewness =', skness
        figure.add_subplot(121)   
        plt.hist(Col,facecolor='lightblue',alpha=0.75) 
        plt.xlabel(" Skewness greater than zero shows large skewed distribution --> ") 
        plt.title(column) 
        plt.text(2,100000,"Skewness: {0:.2f}".format(skness)) 
        
        figure.add_subplot(122) 
        plt.boxplot(Col)
        plt.title("Skewed Distribution")
        plt.xlabel(xlabel)
        plt.show()

print '\nHasta la vista, human.\n'
