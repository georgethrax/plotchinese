# plotchinese
Python code to show Chinese characters in Matplotlib and Seaborn

```python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import numpy as np
import pandas as pd
import matplotlib
reload(matplotlib)
import matplotlib.pyplot as plt
import seaborn as sns

myfont = matplotlib.font_manager.FontProperties(fname="/Library/Fonts/Songti.ttc")
sns.set(font=myfont.get_name())

# This function should be called every time a figure is plotted
# 该函数需要在每次画图后调用
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

# plot_list
```python
def print_unicode_list(a):
    print str(a).decode('unicode-escape')


def print_str_list(a):
    print str(a).decode('string-escape')


def print_list(a, decode_type = 'unicode-escape'):
	print str(a).decode(decode_type)

    
if __name__ == '__main__':
	langs = [
		'Hello, world!',
		'你好，世界！',
		'こんにちは世界',
		u'Hello, world!',
		u'你好，世界！',
		u'こんにちは世界'
	]
	print(langs)
	print_unicode_list(langs)
	print_str_list(langs)
	print_list(langs)
```

langs = [
		'Hello, world!',
		'你好，世界！',
		'こんにちは世界',
		u'Hello, world!',
		u'你好，世界！',
		u'こんにちは世界'
	]

In [21]: langs
Out[21]:
['Hello, world!',
 '\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81',
 '\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xe4\xb8\x96\xe7\x95\x8c',
 u'Hello, world!',
 u'\u4f60\u597d\uff0c\u4e16\u754c\uff01',
 u'\u3053\u3093\u306b\u3061\u306f\u4e16\u754c']

In [22]: print langs
['Hello, world!', '\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81', '\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xe4\xb8\x96\xe7\x95\x8c', u'Hello, world!', u'\u4f60\u597d\uff0c\u4e16\u754c\uff01', u'\u3053\u3093\u306b\u3061\u306f\u4e16\u754c']
    
In [23]: print_unicode_list(langs)
['Hello, world!', 'ä½ å¥½ï¼ä¸çï¼', 'ããã«ã¡ã¯ä¸ç', u'Hello, world!', u'你好，世界！', u'こんにちは世界']

In [24]: print_str_list(langs)
['Hello, world!', '你好，世界！', 'こんにちは世界', u'Hello, world!', u'\u4f60\u597d\uff0c\u4e16\u754c\uff01', u'\u3053\u3093\u306b\u3061\u306f\u4e16\u754c']

In [26]: print_list(langs)
['Hello, world!', 'ä½ å¥½ï¼ä¸çï¼', 'ããã«ã¡ã¯ä¸ç', u'Hello, world!', u'你好，世界！', u'こんにちは世界']
