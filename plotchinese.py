import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import pandas as pd
import matplotlib
reload(matplotlib)
import matplotlib.pyplot as plt
import seaborn as sns

#显示中文的处理方法。其中display_chinese()需要每次调用
#method to show Chinese characters. The function display_chinese() needs to be called every time a figure is plotted.
myfont = matplotlib.font_manager.FontProperties(fname="/Library/Fonts/Songti.ttc")
sns.set(font=myfont.get_name())
def display_chinese(ax, myfont):
    labels = []
    if ax.get_xticklabels():
        labels += ax.get_xticklabels()
    if ax.get_yticklabels():
        labels += ax.get_yticklabels()
    if ax.legend():
        labels += ax.legend()
    if ax.title:
        labels += [ax.title]
    for label in labels: 
        print(label)
        label.set_fontproperties(myfont) 

# often used in jupyter notebook
%matplotlib inline
