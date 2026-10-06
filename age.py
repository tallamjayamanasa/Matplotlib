import matplotlib.pyplot as plt 
ages=[
    18,19,20,21,22,
    23,24,25,26,27,
    28,29,30,31,32,
    33,34,35,36,37,
]
plt.hist(ages, bins=10, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()  
