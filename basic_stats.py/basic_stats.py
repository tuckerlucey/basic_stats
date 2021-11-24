#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
import numpy as np
from matplotlib import pyplot as plt

def basicstats(x):

    N = 0
    for numbers in x:
        N = N + 1
    sumofx = 0
    for numbers in x:
        sumofx = sumofx + numbers
    mean = sumofx/N
    x = [a - mean for a in x]
    x = [b ** 2 for b in x]
    y = x
    sumofy = 0
    for numbers in y:
        sumofy = sumofy + numbers
    NX = N - 1
    z = sumofy / NX
    standarddeviation = z ** 0.5
    print(mean)
    print(standarddeviation)
    h = mean + standarddeviation
    l = mean - standarddeviation
    c = 0
    for numbers in x:
        if numbers < h and numbers > l:
            c = c + 1
    distribution = c / N

    if distribution > 0.68:
        print("Data is normally distributed.")
    else:
        print("Data is NOT normally distributed.")
    data1 = np.array(x)

    plt.hist(data1)

    plt.title("Example Histogram")
    plt.xlabel("Numbers")
    plt.ylabel("Frequency")
    
    return

