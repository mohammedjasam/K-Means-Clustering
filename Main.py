import os
import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt

print("Running Kmeans using SSE")
print("=======================================")
subprocess.call(" python Kmeans.py 1", shell=True)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
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
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# import csv
# ##---VISUALIZATION---##
# with open('Kmeans_cosine_SSE.csv') as f1:
#     r=csv.reader(f1,delimiter=',')
#     a=0
#     for row in r:
#         a1=row
#     for x in a1:
#         a+=float(x)
# print(a)
#
# with open('Kmeans_Jaccard_SSE.csv') as f1:
#     r=csv.reader(f1,delimiter=',')
#     b=0
#     for row in r:
#         a1=row
#     for x in a1:
#         b+=float(x)
# print(b)
#
# with open('Kmeans_Euclidean_SSE.csv') as f1:
#     r=csv.reader(f1,delimiter=',')
#     c=0
#     for row in r:
#         a1=row
#     for x in a1:
#         c+=float(x)
# print(c)
#
# with open('Kmeans_SSE.csv') as f1:
#     r=csv.reader(f1,delimiter=',')
#     d=0
#     for row in r:
#         a1=row
#     for x in a1:
#         d+=float(x)
# print(d)
#
#
# # data to plot
# n_groups = 5
# # create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.3
# opacity = 0.8
#
# rects1 = plt.bar(index, a, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  label='KNN')
# rects2 = plt.bar(index + bar_width, b, bar_width,
#                  alpha=opacity,
#                  color='r',
#                  label='KNN_Varying_K')
# rects3 = plt.bar(index + bar_width+ bar_width, c, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='Decision Tree')
# rects3 = plt.bar(index + bar_width + bar_width+ bar_width, d, bar_width,
#                  alpha=opacity,
#                  color='o',
#                  label='Decision Tree')
#
#
# plt.xlabel('Folds')
# plt.ylabel('Accuracy')
# plt.title('Accuracy by Algorithm')
# plt.xticks(index + bar_width, ('1', '2', '3', '4','5'))
# plt.legend()
#
# plt.tight_layout()
# plt.show()
