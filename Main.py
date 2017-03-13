import os
import subprocess
import time
print("Running Kmeans using Euclidean Distance")
print("=======================================")
subprocess.call(" python Kmeans_Euclidean.py 1", shell=True)
print("------------------------------------------------------------------------------------------------------------------------")
time.sleep(1) # Delay for 5 seconds
print("Running Kmeans using Jaccard Distance")
print("=======================================")
subprocess.call(" python Kmeans_Jaccard.py 1", shell=True)
print("------------------------------------------------------------------------------------------------------------------------")
time.sleep(1)
print("Running Kmeans using Cosine Distance")
print("=======================================")
subprocess.call(" python Kmeans_Cosine.py 1", shell=True)
print("------------------------------------------------------------------------------------------------------------------------")
