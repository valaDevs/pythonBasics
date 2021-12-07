myFile = open('test.txt')
mySecondFile = open("/home/vala/Documents/pythonUdemy/test.txt")
re = myFile.readlines()
res = myFile.read()

print(mySecondFile.readlines())

# print(re)
# print(res)

with open('test.txt', mode="r") as my_new_file:
    contents = my_new_file.read()

print(contents)

