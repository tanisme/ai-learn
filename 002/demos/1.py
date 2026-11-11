import copy

a = [
    [1, 2],
    [3, 4]
]

b = copy.copy(a)

print(a is b)
print(a[0] is b[0])
print(a[1] is b[1])

print("=" * 100)
b[0].append(100)
print(a)
print(b)

print("=" * 100)
b = copy.deepcopy(a)

print(a is b)
print(a[0] is b[0])
print(a[1] is b[1])


print("=" * 100)
data = []

data.append(data)

new_data = copy.deepcopy(data)

print(data is new_data)

print(new_data is new_data[0])

print(data is data[0])



print("=" * 100)
shared = [1, 2, 3]

data = {
    "first": shared,
    "second": shared
}

new_data = copy.deepcopy(data)

print(data["first"] is data["second"])

print(new_data["first"] is new_data["second"])

print(data["first"] is new_data["first"])