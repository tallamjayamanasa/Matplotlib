import matplotlib.pyplot as plt 
salary=[ 
         25000,28000,30000,32000,
         35000,36000,38000,40000,
         42000,45000,50000,55000,
         60000,65000,80000,1200000
]
plt.hist(    salary,    bins=10, edgecolor='black' )
plt.title(" Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()