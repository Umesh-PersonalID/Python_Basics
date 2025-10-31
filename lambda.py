print((lambda x: x + 1)(2))

#lambda arguments: expression


square = lambda x: x * x
print(square(5))   # 25


add = lambda a, b: a + b
print(add(3, 4))  # 7


say_hello = lambda: "Hello!"
print(say_hello())  # "Hello!"


nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]



words = ["apple", "banana", "cherry", "kiwi"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)  # ['kiwi', 'apple', 'banana', 'cherry']


check = lambda x: "even" if x % 2 == 0 else "odd"
print(check(7))  # "odd"


apply_twice = lambda f, x: f(f(x))
print(apply_twice(lambda y: y + 2, 3))  # 7


from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24


students = {'Alice': 85, 'Bob': 72, 'Chad': 90}
sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
print(sorted_students)
# [('Chad', 90), ('Alice', 85), ('Bob', 72)]


funcs = [lambda x, n=n: x + n for n in range(3)]
print([f(10) for f in funcs])  # [10, 11, 12  ]
