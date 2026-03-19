import numpy as np

#constants
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

# seed for repeatability
np.random.seed(1)

# generate salaries
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print("Salaries:", salaries)

# add 5000
salariesPlus = salaries + 5000
print("Salaries + 5000:", salariesPlus)

# increase by 5%
salariesMult = salaries * 1.05
newSalaries = salariesMult.astype(int)
print("Salaries + 5%:", newSalaries)