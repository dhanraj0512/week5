import matplotlib.pyplot as plt
import numpy as np 

x=np.linspace(1,5,11)
y=x**2

fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])



axes.plot(x,x**2,label="x square")
axes.plot(x,x**3,label="x cubed")


axes.legend(loc=0)# we can change the the legend location from this 

plt.show()