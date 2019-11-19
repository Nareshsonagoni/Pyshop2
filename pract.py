# title_list = ['S', ' ', 'W', 'A', 'R', ' ',  'A']
# guess = input("Enter: ").upper()
# title_index = title_list.index(guess)
# if guess in title_list:
# print(title_index)


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print("Hi I am", self.name)
#
#
# person = Person("Naresh")
# person.talk()

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print("FIzzBuzz")
    elif input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    return input


input_number = int(input("Input: "))
fizz_buzz(input_number)





