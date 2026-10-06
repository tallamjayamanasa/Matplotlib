import matplotlib.pyplot as plt 
months=['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales=[100,150,120,180,200]
plt.bar(months, sales)
plt.title("Annotation Example")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.annotate(    "Highest Sales",    xy=("May", 200),    xytext=("Feb", 170),    arrowprops={"arrowstyle": "->"} )
plt.show()