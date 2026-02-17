import random

fruits = ('Pear', 'Melon', 'Papaya', 'Rasberry')

index = random.randint(0, len(fruits) -1)
fruit = fruits[index]

print("A random fruit:{}".format(fruit))