# plotchinese
Python code to show Chinese characters in Matplotlib and Seaborn

```python
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import pandas as pd
import matplotlib
reload(matplotlib)
import matplotlib.pyplot as plt
import seaborn as sns

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
        
%matplotlib inline
```
