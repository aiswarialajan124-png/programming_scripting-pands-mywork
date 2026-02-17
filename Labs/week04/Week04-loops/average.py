numbers = []

number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)
    number = int(input("Enter another (0 to quit): "))

for n in numbers:
    print(n)

average = sum(numbers) / len(numbers)
print("The average is", average)