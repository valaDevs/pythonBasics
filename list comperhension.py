myname = "vala"
myList = []
for i in myname:
    myList.append(i)

print(myList)


# fllaten out for loop

myList = [letter for letter in myname]
print(myList)

li = [x for x in "hello world"]
print(li)
a = [num**2 for num in range(1,10)]
print(a)

x = [x for x in range(0, 11) if x % 2 == 0]
print(x)


# convert celcius in farenheit
celcius = [0, 10, 20, 34.6]
farenheit = [((9/5) * temp + 32) for temp in celcius]


