import random

numbers = []
for i in range(10):
    numbers.append(random.randint(0, 100))

print("Numbers: ", numbers)

numbers.sort(reverse=True)
print("Top three: ", numbers[:3])