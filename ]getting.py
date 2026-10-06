import matplotlib.pyplot as plt 

n, bins, patches = plt.hist(data, bins=3) 
print("Frequency:", n) 
print("Bins:", bins) 
plt.show()