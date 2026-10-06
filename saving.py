import matplotlib.pyplot as plt
months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
sales=[10000, 15000, 12000, 18000, 20000, 22000, 25000, 30000]
plt.plot(months, sales)
plt.savefig("sales_plot.png")
plt.savefig("sales_plot.pdf")
plt.show()