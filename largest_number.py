try:
    with open("count", "r") as file:
        numbersList = [float(line.strip()) for line in file]
    largestNumber = max(numbersList)
    print("The largest number is:", largestNumber)
except FileNotFoundError:
    print("ERROR. File Count not found")
except ValueError:
    print("ERROR. File Count contains non-numeric values")