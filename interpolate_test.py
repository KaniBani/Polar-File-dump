from scipy import interpolate
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt

clcd_data=np.loadtxt('clcd_dump.txt')

Re=clcd_data[:,0]
Re_log=np.log10(Re)
cl=clcd_data[:,1]
cd=clcd_data[:,2]


clcd = interpolate.interp2d(Re_log, cl,cd, kind='linear')

print clcd(1e5,0.3592)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Re_log,cd,cl)

ax.set_xlabel('Re')
ax.set_ylabel('Cd')
ax.set_zlabel('Cl')

plt.show()

