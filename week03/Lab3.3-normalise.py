rawString = input("please enter a string: ")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print(f"That String normalised is :{normalisedString}")
print(f"we reduced the input string from {lengthOfRawString} to {lengthOfNormalised} characters")
