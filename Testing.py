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

objects = (1,2,3,4)
y_pos = np.arange(len(objects))

performance = [4163.3, 1849.2, 1063.2, 682.0, 369.2, 369.2]
width = 0.2
plt.bar(y_pos, l, width, align='center', color='b')
plt.xticks(y_pos, objects)
plt.ylabel('Withinness(Scale Normalized)')
plt.xlabel('Iteration')
plt.title('Sum of Square Error KMeans Algorithm execution V/s Withinness')

plt.show()
