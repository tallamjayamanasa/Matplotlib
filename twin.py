import matplotlib.pyplot as plt 
moths=["Jan", "Feb", "Mar", "Apr", "May"]
sales=[10000, 15000, 12000, 18000, 20000]
customers=[100, 150, 120, 180, 200]
plt.plot(moths, sales)
plt.title("Monthly Sales")  
fig, ax1 = plt.subplots() 
ax1.plot(moths, sales) 
ax1.set_xlabel("Month") 
ax1.set_ylabel("Sales") 
ax2 = ax1.twinx() 
ax2.plot(moths, customers) 
ax2.set_ylabel("Customers") 
plt.show()