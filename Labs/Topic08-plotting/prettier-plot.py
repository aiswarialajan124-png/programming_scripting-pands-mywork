import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

numberOfEntries = 100

salaries = np.random.randint(20000, 80000, numberOfEntries)
ages = np.random.randint(21, 65, numberOfEntries)

# Scatterplot
plt.scatter(ages, salaries, label="Salaries")

# x^2 line
x = np.array(range(1, 101))
y = x ** 2
plt.plot(x, y, color='red', label="x^2")

# labels and styling
plt.title("Salaries vs Ages with x^2 Curve")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)

# save file
plt.savefig("prettier-plot.png")

plt.show()