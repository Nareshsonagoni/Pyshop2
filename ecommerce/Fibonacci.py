# Fibonacci

# a, b = 0, 1
# for i in range(1, 20):
#     print(a)
#     a, b = b, a + b

# fizz buzz

# for num in range(1, 101):
#     if num % 5 == 0 and num % 3 == 0:
#         print("Fizz Buzz")
#     elif num % 5 == 0:
#         print("Fizz")
#     elif num % 3 == 0:
#         print("Buzz")
#     else:
#         print(num)

# my_set = {1, 1, 43, 34, 43, 45, 54, 34, 34, 45, 56}
# for i in my_set:
#     print(i)

# libraries

# my_library = {"name": "Naresh",
#               "age": 30,
#               "occupation": "Student",
#               "education": "Masters",
#               "email": "naresh@gmail.com"}
# for key, values in my_library.items():
#     # output = my_library.get(key, "Not in list !!")
#     print(f" My {key} is {values}")

# List
import random


# room_mates = ["Naresh", "Dattu", "Sham", "Pranav", "Vindo", "Praveen"]
# room = ["Prudhvi", "Harsha", "Tarun"]
# room.extend(room_mates)
# room.remove('Pranav')
# print(room)

# for i in range(15):
#     leader = random.choice(room)
#     print(leader)

from pathlib import Path

path = Path()
for file in path.glob('*.*'):
    print(file)
