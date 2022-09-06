#import libraries
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import time

starttime = time.time()

#creates path to the file downloaded directly from lab computer
path = r"C:\Users\gtown\OneDrive\Documents\muon.txt"
#converts file to .csv, so it's usuable in Python
muondata = pd.read_csv(path, header=None, prefix = 'Col_', usecols=[0], sep=' ')

#organize data into something useful
arr = muondata.values
decays = []
i=0
while i<len(arr):
	if arr[i]<40000:
		decays.append(arr[i])
		i=i+1
	else:
		i=i+1

tobs = np.average(decays)
stdev = np.std(decays)
utobs = stdev/(np.sqrt(len(decays)))

tp = 2140
tm = 2030
utp = 170
utm = 10

rho = -(tp/tm)*((tm*tobs)/(tp-tobs))
a = ((utp*tobs)/(tp-tobs))*(tp/(tp-tobs)-1)
b = ((utobs*tp)/(tp-tobs))*(tobs/(tp-tobs)+1)
c = a**2 + b**2
urho = math.sqrt(c)

print(tobs)
print(stdev)
print(utobs)
print(rho)
print(urho)

#plt.hist(decays, bins = 10)
#plt.show()

print(time.time()-starttime)
