import matplotlib.pyplot as plt
x=[2021,2022,2023,2024,2025]
y=[50, 75, 100,  150,125]

plt.plot(x, y,linestyle='--', marker='o', color='b')
plt.title("Sales data")
plt.xlabel("Year")
plt.ylabel("Sales (in thousands)")
plt.grid("True")
plt.show()