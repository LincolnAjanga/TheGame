
# coding: utf-8

# In[1]:


import time
import webbrowser

max_break = 3
break_count = 0

while(break_count < max_break):
    time.sleep(5)
    webbrowser.open('file:///home/lincoln/Documents/SwineSniper-TheGame/index.html')
    break_count = break_count +1

