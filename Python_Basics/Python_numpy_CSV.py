import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


x,y = np.loadtxt("example2.csv",unpack=True,skiprows=1,delimiter=',')

print(x,y)


plt.subplot(211)
plt.plot(x,y,color='red')
plt.subplot(212)
plt.plot(x,y,color='green')
plt.show()

