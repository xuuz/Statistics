# MoCT.py
**Retrieving, Processing, and Visualizing Data with Python**

<b><u>Capstone project</u></b>: To write a program that can read, analyze and visualize data, using the skills from the <a href="https://www.coursera.org/learn/python-data-visualization/home/welcome">course</a>, and apply statistics knowledge to get results from a real investigation. 

To use this for your own data, you'll need to install these packages:

:package: <a href="https://docs.python.org/2/library/math.html" window="_blank">math</a>  
:package: <a href="https://pypi.python.org/pypi/numpy" target="_blank">numpy</a>  
:package: <a href="https://pypi.python.org/pypi/pandas/0.20.3" target="_blank">pandas</a>  
:package: <a href="https://pypi.python.org/pypi/scipy/0.19.1" target="_blank">scipy</a>  
:package: <a href="https://pypi.python.org/pypi/matplotlib/2.0.2" target="_blank">matplotlib</a>  

- When you run the program, you'll see a set of easy instructions to follow:

    - Make sure that the .txt file is in the same folder of this script, otherwise it won't be found.
    - To start, enter the name of the file without "quotes" and ending with .txt (example: scores.txt).
    - The name of the file will be the legend on the first plot, I recommend you to choose the name wisely.  
    - Later, when you are done selecting values for sample distribution, type "ya", hit Return and the program will finish nicely.  

After entering the name of the file you want to analyze, you'll get:

- **N**  
- **Mean**  
- **Sum of squares**  
- **Variance**  
- **Population Standard Deviation**  
- **Standard Error**  
- :chart_with_downwards_trend: **Graph for population distribution**  

Then you can choose sample means and values to see how far they are from the mean... and get:

- **Standard Error for each sample**  
- **Z-score**  
- **Z-table value for that score**  
- **Probability of getting that value** 
- **Confidence interval**
- **Margin of error**
- :chart_with_upwards_trend: **Graph for sample distribution**  

* * *

You can download <a href="https://github.com/TaniaMol/Statistics/blob/master/scores.txt"><b>scores.txt</b></a> to test the script :ballot_box_with_check:
<br><br>
Demo:

<img src="https://user-images.githubusercontent.com/22894897/29638445-b0a8abf2-882d-11e7-920d-362fb643a2ff.gif" width="100%">
<br>
Code <i>preview</i> (See <a href="https://github.com/TaniaMol/Statistics/blob/master/MoCT.py"><b>MoCT.py</b></a>, which will be constantly updated, not the code below):  <br><br>

```Python
# -*- coding: utf-8 -*-
#!/usr/bin/python
# Author: Tania M. Molina - UY/2017
# MIT License

import math
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm
import scipy.stats as stats
import scipy.stats as st
import matplotlib
import matplotlib.pyplot as plt

print(' ')
print(' Welcome to MoCTpy! ')
print(' --by Tania Mol-- ')
print(' ')
print("INSTRUCTIONS:\n \n- Make sure that the .txt file is in the same folder of this script, otherwise it won't be found.\n- To start, enter the name of the file without 'quotes' and ending with .txt (example: scores.txt).\n- Later, when you are done selecting values for sample distribution, type 'ya', hit Return and the program will finish nicely.\n")
fhand = raw_input('Now, enter the file name: ')

numbers = open(fhand)

A = list()
for number in numbers :
    value = float(number)
    A.append(value)

sigma = sum(A) #sumation
n = len(A) #total of elements
mean = sigma / n
Dev = list()
AbsDev = list()
SqDev = list()
for number in A :
    val = number - mean
    Dev.append(val) #Deviation from the mean
    
for element in Dev :
    val = abs(element)
    AbsDev.append(val) # Absolute Deviation
    
for element in AbsDev :
    val = (element**2)
    SqDev.append(val) #Square Deviations

SS = sum(SqDev) #Sum of Squares
Var = SS / n #Variance
StdDev = math.sqrt(Var) #Standard Deviation
StdE = StdDev / math.sqrt(n) #Standard Error

print ('---------------------------------------------')
print ('MEASURES OF CENTRAL TENDENCY for:'), fhand
print (' ')
print ('N ='), n
print ('Mean ='), mean
print ('Sum of Squares ='), SS
print ('Variance ='), Var
print ('Population Standard Deviation ='), StdDev
print ('Standard Error ='), StdE
print ('---------------------------------------------')
print(' ')
Array = np.asarray(A)
Array.sort()
pdf = stats.norm.pdf(Array, mean, StdDev)
fig = plt.plot(Array, pdf)
plt.title("Population distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
print ('To continue, you must save the figure and close it.\n')
plt.show(fig)

while True:
    fh = raw_input('Enter value for sample distribution: ')
    if fh[0] == '#':
        continue
    if fh == 'ya':
        break
    newn = float(fh)
    newdeviation = StdDev / math.sqrt(newn)
    print(' ')
    print 'The Standard Error for', newn,'is: ', newdeviation
    print('------------------------------------------------------')
    print(' ')
    anyvalue = raw_input('Enter a value to see how far it is from the mean: ')
    if anyvalue[0] == '#':
        continue
    if anyvalue == 'ya':
        break
    newmean = float(anyvalue)
    rest = newmean - mean
    zscore = rest / newdeviation
    print ' '
    print '| The z-score for', anyvalue, 'is:', zscore, '|'
    pvalue = st.norm.cdf(zscore)
    print('---------------------------------------------')
    print '| Z table value =', pvalue, '|'
    print('---------------------------------------------')
    greater = 1 - pvalue
    print 'The probability of getting at least', anyvalue,'is:'
    print 'p =', greater
    print 'p = ', greater*100, '%'
    print('---------------------------------------------')
    pdf2 = stats.norm.pdf(Array, mean, newdeviation)
    fig2 = plt.plot(Array, pdf2)
    plt.title("Sampling distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    print ('To continue, you must save the figure and close it, or just close it.\n')
    plt.show(fig2)
    continue
print(' ')
print 'It was a pleasure to make your life easier,\nHasta la vista, baby!'
print(' ')
```
<br>
<br>
<p align="center"><a href="https://lastralab.github.io/website/timeline/index.html" target="_blank"><br><button><img src="http://i.imgur.com/ERyS5Xn.png" alt="l'astra lab icon" width="50px" background="transparent" opacity="0.5" padding="0;"/></button></a></p><br><br>
