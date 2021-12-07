t = (1, 2, 3, 4)
list = [1, 2, 3]

print(type(t))
print(type(list))
print(len(t))

t = ('a', 'a', 'c')
print(t.count('a'))
print(t.index('a'))
print(t.index('c'))

# we cant assign items
# immtablilty

a = "vala"
print(a.upper())

a = "vala"

if type(a) == str:
    print("ok")
