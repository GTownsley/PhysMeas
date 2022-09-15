#import libraries
import pandas as pd
import numpy as np
import math
import scipy
import matplotlib.pyplot as plt
import time

starttime = time.time()

#creates path to the file downloaded directly from lab computer
path = r"C:\Users\gtown\OneDrive\Documents\decaysA.txt"
#converts file to .csv, so it's usuable in Python
muondata = pd.read_csv(path, header=None, prefix = 'Col_', usecols=[0], sep=' ')

#organize data into something useful
arr = muondata.values
decays = []
vals = np.zeros(40)
i=0
while i<len(arr):
	if (arr[i]<40000 and arr[i]>0):
		decays.append(arr[i])
		if(arr[i]<500):
			vals[0] = vals[0]+1
		elif(arr[i]<1000):
			vals[1] = vals[1]+1
		elif(arr[i]<1500):
			vals[2] = vals[2]+1
		elif(arr[i]<2000):
			vals[3] = vals[3]+1
		elif(arr[i]<2500):
			vals[4] = vals[4]+1
		elif(arr[i]<3000):
			vals[5] = vals[5]+1
		elif(arr[i]<3500):
			vals[6] = vals[6]+1
		elif(arr[i]<4000):
			vals[7] = vals[7]+1
		elif(arr[i]<4500):
			vals[8] = vals[8]+1
		elif(arr[i]<5000):
			vals[9] = vals[9]+1
		elif(arr[i]<5500):
			vals[10] = vals[10]+1
		elif(arr[i]<6000):
			vals[11] = vals[11]+1
		elif(arr[i]<6500):
			vals[12] = vals[12]+1
		elif(arr[i]<7000):
			vals[13] = vals[13]+1
		elif(arr[i]<7500):
			vals[14] = vals[14]+1
		elif(arr[i]<8000):
			vals[15] = vals[15]+1
		elif(arr[i]<8500):
			vals[16] = vals[16]+1
		elif(arr[i]<9000):
			vals[17] = vals[17]+1
		elif(arr[i]<9500):
			vals[18] = vals[18]+1
		elif(arr[i]<10000):
			vals[19] = vals[19]+1
		elif(arr[i]<10500):
			vals[20] = vals[20]+1
		elif(arr[i]<11000):
			vals[21] = vals[21]+1
		elif(arr[i]<11500):
			vals[22] = vals[22]+1
		elif(arr[i]<12000):
			vals[23] = vals[23]+1
		elif(arr[i]<12500):
			vals[24] = vals[24]+1
		elif(arr[i]<13000):
			vals[25] = vals[25]+1
		elif(arr[i]<13500):
			vals[26] = vals[26]+1
		elif(arr[i]<14000):
			vals[27] = vals[27]+1
		elif(arr[i]<14500):
			vals[28] = vals[28]+1
		elif(arr[i]<15000):
			vals[29] = vals[29]+1
		elif(arr[i]<15500):
			vals[30] = vals[30]+1
		elif(arr[i]<16000):
			vals[31] = vals[31]+1
		elif(arr[i]<16500):
			vals[32] = vals[32]+1
		elif(arr[i]<17000):
			vals[33] = vals[33]+1
		elif(arr[i]<17500):
			vals[34] = vals[34]+1
		elif(arr[i]<18000):
			vals[35] = vals[35]+1
		elif(arr[i]<18500):
			vals[36] = vals[36]+1
		elif(arr[i]<19000):
			vals[37] = vals[37]+1
		elif(arr[i]<19500):
			vals[38] = vals[38]+1
		else:
			vals[39] = vals[39]+1
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

rho = -(tp/tm)*((tm-tobs)/(tp-tobs))
a = ((utp*tobs*(tobs-tm))/(tm*(tp-tobs)*(tp-tobs)))
b = ((utobs*tp*(tp-tm))/(tm*(tp-tobs)*(tp-tobs)))
c = ((utm*tobs*tp)/(tm*tm*(tp-tobs)))
d = a**2 + b**2 + c**2
urho = math.sqrt(d)

#tpd = 640
#tmd = 620
#ud = 5

#rhod = -(tpd/tmd)*((tmd-tobs)/(tpd-tobs))
#e = ((ud*tobs*(tobs-tmd))/(tmd*(tpd-tobs)*(tpd-tobs)))
#f = ((utobs*tpd*(tpd-tmd))/(tmd*(tpd-tobs)*(tpd-tobs)))
#g = ((ud*tobs*tpd)/(tmd*tmd*(tpd-tobs)))
#h = e**2 + f**2 + g**2
#urhod = math.sqrt(h)


print(len(decays))
#print(len(decays)/9600)
print(len(decays)/10835)
print(tobs)
print(stdev)
print(utobs)
print(rho)
print(urho)

bins = np.array([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500,
 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000,
 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500,
 18000, 18500, 19000, 19500, 20000])

plt.fill_between(bins,np.concatenate(([0],vals)), step="pre")
plt.title("Muon Time Decay Histogram for Data Set B")
plt.xlabel("Observed Decay Time [ns]")
plt.ylabel("Count")
plt.show()


print(time.time()-starttime)
