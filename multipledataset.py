import matplotlib.pyplot as plt 
class_a=[1, 2, 2, 3, 3, 3, 4, 4, 5]
class_b=[2, 3, 3, 4, 4, 5, 5, 6, 7]
plt.hist(class_a, bins=5, alpha=0.5, label="Class A") 
plt.hist(class_b, bins=5, alpha=0.5, label="Class B") 
plt.legend() 
plt.show()