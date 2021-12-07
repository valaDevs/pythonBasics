#            0         1         2       3         4         5
myList = ["apple", "banana", "grape", "cherry", "orange", "strawberry", "watermelon"]
print(myList[2:5]) # select from index 2 until 5 excluded
print(myList[:4])
print(myList[2:])

if "apple" in myList:
    print("yes apple is in the list")

# change list item
# myList[0] = "BlackBerry"
# print(myList)

myList[1:3] = ["peach","cucumber"]
print(myList)

myList.insert(2,"watermelon")
print(myList)