import matplotlib.pyplot as plt
months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales=[10000, 15000, 12000, 18000, 20000, 22000, 25000, 30000, 28000, 26000, 24000, 22000]
fig, axes = plt.subplots(2, 2, figsize=(10, 7))
axes[0, 0].plot(months, sales) 
axes[0, 0].set_title("Line") 
axes[0, 1].bar(months, sales) 
axes[0, 1].set_title("Bar") 
axes[1, 0].hist(sales) 
axes[1, 0].set_title("Histogram") 
axes[1, 1].scatter(range(len(months)), sales)
axes[1, 1].set_title("Scatter") 
plt.tight_layout() 
plt.show()