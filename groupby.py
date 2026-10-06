import pandas as pd
import matplotlib.pyplot as plt 
Departments = ['HR', 'Finance', 'IT', 'Marketing']
Salary = [50000, 60000, 70000, 55000]
df = pd.DataFrame({
    "Department": Departments,
    "Salary": Salary
})
summary = df.groupby('Department')['Salary'].mean()
plt.bar(summary.index, summary.values) 
plt.title("Average Salary by Department") 
plt.xlabel("Department") 
plt.ylabel("Average Salary") 
plt.show()