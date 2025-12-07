import matplotlib.pyplot as plt
import numpy as np 

x=np.linspace(1,5,11)
y=x**2

fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])


ax.plot(x,y,color='green',lw=2,ls='--')
ax.set_xlim([0,1])
ax.set_ylim([0,5])

plt.show()