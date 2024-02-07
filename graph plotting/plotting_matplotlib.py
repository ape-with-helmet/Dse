import matplotlib.pyplot as plt
import numpy as np
guests=np.array([23,32,27,50,22,18,11,65])
subs=np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"])
plt.plot(subs,guests,marker='o',color='#6834E2')
plt.xlabel("Month/Year")
plt.ylabel("Visitors")
plt.legend(['No.of Visitors'])
plt.show()
