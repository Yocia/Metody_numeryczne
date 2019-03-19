#!/usr/bin/env python
# coding: utf-8

# In[3]:


from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
from decimal import *

y=[]
for x in range(56, 101):
    y.append(2*x**2 + 2*x + 2)
print(y)


# In[25]:


from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
from decimal import *
 
m=1
z = float(input("Type number to factor "))
if(z%1==0 and z>=0):
    z=int(z)
    for i in range(1, z+1):
        m = m*i
    print(m)
else:
    print("Provided number is inadequate to factor")


# In[27]:





# In[30]:


from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
from decimal import *



def zad3(lista):
    min=lista[0]
    n=[]
    for i in range(len(lista)):
        if min>=lista[i]:
            min=lista[i]
            n.append(i)
    n.remove(0)
    return min,n
lista=[58,42,384,628,111,285,46]
print(zad3(lista))


# In[36]:


from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
from decimal import *

x6 = int(input("Type chart begining "))
x5 = int(input("Type chart lenght "))
x = linspace(x6, x5*5, 500)
y = x**2+8*x
plot(x, y)
show()


# In[ ]:




