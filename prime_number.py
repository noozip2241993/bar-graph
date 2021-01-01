import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import math

minValue = 1000
maxValue = 1050


            
# generate random number from min to max value
def getRandomInt():
    return random.randint(minValue, maxValue)

# generate x number of random number
def randomGenerateData(dataRange):
    data = []
    for j in range(0, dataRange):
        value = getRandomInt()
        data.append(value)
    return data

# check prime number
def findPrimeNumber(number):
    if number > 1:
        for i in range(2, math.floor(number**1/2)):
            if (number % i) == 0:
                return 1
        else:
            return 0
    return 1

# find all prime number from array of data
def findAllPrimeNumber(data):
    primeList = []
    for value in data:
        isPrime = findPrimeNumber(value)
        if isPrime == 0:
            primeList.append(value)
            
    return primeList

#------ execution code -------

#generate 10000 random number    
randomData = randomGenerateData(10000)

#find list of prime number from random 10000 number
primeList = findAllPrimeNumber(randomData)


def graphing_bar(title = 'Frequency Distribution',x_label = "",y_label="",data =[],data_labels= True, vertical=True ):
    
    x_label = 'Prime Number'
    y_label = 'Frequency'
    this_data = data
    
    
    values,frequencies = np.unique(this_data,return_counts=True)
    sns.set_style('whitegrid')
    axes = sns.barplot(x = values, y = frequencies, palette= 'bright')
    axes.set_title(title)
    axes.set(xlabel = x_label,ylabel = y_label)
    axes.set_ylim(top=max(frequencies)*1.10)

    for bar,frequency in zip(axes.patches,frequencies):
        text_x = bar.get_x() + bar.get_width()/2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency/len(this_data):.3%}'
        axes.text(text_x,text_y,text,
                                    fontsize= 11, ha='center',va='bottom')
    plt.show()
graphing_bar(title = 'Frequency Distribution',x_label = "",y_label="",data =primeList,data_labels= True, vertical=True )