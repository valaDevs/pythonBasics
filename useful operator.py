import random
index = 0
letters = "abcde"
for i in enumerate(letters):
    print(i)


myList = [1, 2, 3]
myList2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
for i in zip(myList, myList2, mylist3):
    print(i)


print('a' in "vala")
print('x' in "hello")
print(1 in [1, 3, 4])
print('key1' in {"key1": 345})



dic = { "key1": 345 }
print(345 in dic.values())
print(345 in dic.keys())
print("key1" in dic.keys())

myList4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(min(myList4))
print(max(myList4))



print(random.randint(0, 100))


