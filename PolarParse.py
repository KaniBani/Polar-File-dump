'''
This file converts set of xfoil generated polar files to a single file
containing Re CL CD in 3 columns. 
File output is clcd_dump.txt and all the txt files will be appended
to the output file.

As this data is supposed to be interpolated only data between cl_min and
cl_min are filtered and written to the dump file.

Status:
Works fine : 6-jun-2016
'''


import numpy as np
import glob
import os


def parse_single_polar(filename):

	#strip the Re number
    
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
	
	

def parse_all_polar():
        
    for filename in glob.glob('*.txt'):
        parse_single_polar(filename)

parse_all_polar()
