with open('newTest.txt', mode="r") as file:
    print(file.read())


with open('newTest.txt', mode="a") as f:
    f.write("\nOH this line is added to to file cool!!!!!")


# creates a new file for us the W mode
with open("alskjdasjdlasdjlasd.txt",mode="w") as w:
    w.write("i created this file")

with open("alskjdasjdlasdjlasd.txt", mode="r") as f:
    print(f.read())
