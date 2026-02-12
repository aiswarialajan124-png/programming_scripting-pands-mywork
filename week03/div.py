x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

answer = x // y
remainder = x % y

print("{} divided by {} is {} with remaider {}".format(x, y, answer, remainder))