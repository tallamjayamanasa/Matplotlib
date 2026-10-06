import matplotlib.pyplot as plt 
products=["laptop","desktop","keyboard"]
sales=[2000,4000,8000]

plt.bar(products,sales)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.legend()
plt.show()