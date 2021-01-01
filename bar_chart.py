import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
rolls = 6000
def rolling_a_dice(n):
    """Rolling a dice 600 times"""
    return [random.randrange(1,7) for i in range(n)]


def graphing_bar(title = 'Frequency Distribution',x_label = "",y_label="",data =[],data_labels= True, vertical=True ):
    
    x_label = 'Dice Value'
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
graphing_bar(title = 'Frequency Distribution',x_label = "",y_label="",data =rolling_a_dice(600),data_labels= True, vertical=True )