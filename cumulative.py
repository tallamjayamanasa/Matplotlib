import matplotlib.pyplot as plt 
ages=[18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
plt.hist(    ages,    bins=10,    cumulative=True )
plt.show()