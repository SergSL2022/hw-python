fruitsList = ["apple", "pear", "cherry", "banana", "orange", "kiwi"]

fruitToFind = input("Input fruit to find: ")

if fruitToFind in fruitsList:
    print(f"Yes, the element '{fruitToFind}' exists.")
else:
    print(f"No, the element '{fruitToFind}' does not exist.")