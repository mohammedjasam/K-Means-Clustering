import os
import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt

print("Running Kmeans using Euclidean Distance")
print("=======================================")
subprocess.call(" python Kmeans_Euclidean.py 1", shell=True)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
time.sleep(1) # Delay for 5 seconds
print("Running Kmeans using Jaccard Distance")
print("=======================================")
subprocess.call(" python Kmeans_Jaccard.py 1", shell=True)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
time.sleep(1)
print("Running Kmeans using Cosine Distance")
print("=======================================")
subprocess.call(" python Kmeans_Cosine.py 1", shell=True)
subprocess.call(" python k-means_Cosine.py 1", shell=True)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
import csv
##---VISUALIZATION---##

with open('Kmeans_cosine_SSE.csv') as f1:
    r=csv.reader(f1,delimiter=',')
    a=0
    for row in r:
        a1=row
    for x in a1:
        a+=float(x)
# print(a)

with open('Kmeans_Jaccard_SSE.csv') as f1:
    r=csv.reader(f1,delimiter=',')
    b=0
    for row in r:
        a1=row
    for x in a1:
        b+=float(x)
# print(b)

with open('Kmeans_Euclidean_SSE.csv') as f1:
    r=csv.reader(f1,delimiter=',')
    c=0
    for row in r:
        a1=row
    for x in a1:
        c+=float(x)
# print(c)


import numpy as np
import matplotlib.pylab as plt
import csv
with open('Kmeans_cosine_SSE.csv') as f1:
    r=csv.reader(f1,delimiter=',')
    a=0
    for row in r:
        a1=row
    for x in a1:
        a+=float(x)
# print(a)

with open('Kmeans_Jaccard_SSE.csv') as f1:
    r=csv.reader(f1,delimiter=',')
    b=0
    for row in r:
        a1=row
    for x in a1:
        b+=float(x)
# print(b)

with open('Kmeans_Euclidean_SSE.csv') as f1:
    r=csv.reader(f1,delimiter=',')
    c=0
    for row in r:
        a1=row
    for x in a1:
        c+=float(x)
# print(c)

with open('Kmeans_SSE.csv') as f1:
    r=csv.reader(f1,delimiter=',')
    d=0
    for row in r:
        a1=row
    for x in a1:
        d+=float(x)
# print(d)
l=[]
l.append(a)
l.append(b)
l.append(c)
l.append(d)

# l=list(a,b,c,d)

objects = ("Cosine","Jaccard","Euclidean","K-means")#(1,2,3,4)
y_pos = np.arange(len(objects))

width = 0.35
plt.bar(y_pos, l, width, align='center', color='b')
plt.xticks(y_pos, objects)
plt.ylabel('Withinss(Scale Normalized)')
plt.xlabel('Distance Metric')
plt.title('Sum of Square Error K-means Clustering Algorithm V/s Distance Metric')

plt.show()

os.remove('Kmeans_cosine_SSE.csv')
os.remove('Kmeans_Euclidean_SSE.csv')
os.remove('Kmeans_Jaccard_SSE.csv')
