import random

fruits = ['Blueberry', 'Pineapple', 'Guava', 'Watermelon']

index = random.randint(0, len(fruits) -1)
fruit = fruits[index]

print("A Random Fruit:{}".format(fruit))