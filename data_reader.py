import numpy as np
import csv

import matplotlib.pyplot as pl

filename = 'PointingData.csv'

f = open(filename,'r')
r = csv.reader(f)

# create lists
AzList = []
ElList = []
AzOffList = []
AzErrList = []
ElOffList = []
ElErrList = []

for row in r:
    AzList.append(eval(row[4]))
    ElList.append(eval(row[5]))
    AzOffList.append(eval(row[6]))
    AzErrList.append(eval(row[7]))
    ElOffList.append(eval(row[8]))
    ElErrList.append(eval(row[9]))

# create numpy arrays
az = np.array(AzList)
el = np.array(ElList)
azoff = np.array(AzOffList)
azerr = np.array(AzErrList)
eloff = np.array(ElOffList)
elerr = np.array(ElErrList)
 
pl.ion()
pl.plot(az,el,'o')
pl.xlabel('Azimuth')
pl.ylabel('Elevation')
pl.title('LMT Pointing Data - 2014')
