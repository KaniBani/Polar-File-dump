import numpy as np

filename="E205  (10.48%)_T1_Re0.100_M0.00_N9.0.txt"


Re = open(filename).readlines()[7]
Re = Re[Re.find("Re")+5:Re.find("Ncrit")]
Re = Re.replace(" ", "")
Re = float(Re)

#strip cl and cd data set
cl,cd = np.loadtxt(filename, usecols = (1,2), unpack=True, skiprows=11)

#filtering out up to upper and lower stall limits.
#otherwise cd will not be a proper function. (double rule)

clmax_index=np.argmax(cl)+1
clmin_index=np.argmin(cl)

cl=cl[clmin_index:clmax_index]
cd=cd[clmin_index:clmax_index]

Re=np.ones(len(cl))*Re

with open("clcd_dump.txt", "a") as dumpfile:
	np.savetxt(dumpfile, np.c_[Re,cl,cd])
