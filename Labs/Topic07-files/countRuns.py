FILENAME = "count.txt"

def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
    
def writeNumber(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

# main
num = readNumber()
num += 1

print(f"We have run this program {num} times")

writeNumber(num)