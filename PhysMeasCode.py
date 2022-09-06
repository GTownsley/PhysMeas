#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

starttime = time.time()

#creates path to the file downloaded directly from lab computer
path = r"C:\Users\gtown\OneDrive\Documents\muon.txt"
#converts file to .csv, so it's usuable in Python
muondata = pd.read_csv(path, header=None, prefix = 'Col_', nrows=100, usecols=[0], sep=' ')

#organize data into something useful
arr = muondata.values
decays = []
i=0
while i<len(arr):
	if arr[i]<40000:
		decays.append(arr[i])
		i=i+1
		continue
	else:
		i=i+1
		continue

mean = np.average(decays)
stdev = np.std(decays)
sterr = stdev/(np.sqrt(len(decays))

#print(mean)
#print(stdev)
#print(sterr)

#plt.hist(decays, bins = 10)
#plt.show()

#print(time.time()-starttime)