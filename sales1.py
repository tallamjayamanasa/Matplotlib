import matplotlib.pyplot as plt
x=["jan","feb","mar","apr","may"]
sales=["$1000","$2000","$3000","$4000","$5000"]

plt.plot(x, sales,linestyle='--', marker='o', color='b')
plt.title("Sales data")
plt.xlabel("Month")
plt.ylabel("Sales (in thousands)")
plt.legend(["Sales"])
plt.show()