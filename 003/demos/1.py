# list
numbers = [1, 2, 3]

# tuple
names = ("Alice", "Bob", "Charlie")

# str
text = "Python"

# dict
user = {
    "name": "Alice",
    "age": 25
}

# set
values = {10, 20, 30}

for number in numbers:
    print(number)

from collections.abc import Iterable

numbers = [1, 2, 3]
text = "Python"
number = 100

print(isinstance(numbers, Iterable))
print(isinstance(text, Iterable))
print(isinstance(number, Iterable))

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

from collections.abc import Iterable, Iterator

numbers = [1, 2, 3]
iterator = iter(numbers)

print(isinstance(numbers, Iterable))
print(isinstance(numbers, Iterator))

print(isinstance(iterator, Iterable))
print(isinstance(iterator, Iterator))