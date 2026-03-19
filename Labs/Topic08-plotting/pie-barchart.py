import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

possibleCounties = ['Mayo', 'Galway', 'Roscommon', 'Dublin', 'Donegal']

counties = np.random.choice(
    possibleCounties,
    p=[0.1, 0.3, 0.2, 0.12, 0.28],
    size=100
)

unique, counts = np.unique(counties, return_counts=True)

# Pie Chart
plt.pie(counts, labels=unique)
plt.title("County Distribution (Pie)")
plt.show()

# Bar Chart
plt.bar(unique, counts)
plt.title("County Distribution (Bar)")
plt.xlabel("County")
plt.ylabel("Count")
plt.show()