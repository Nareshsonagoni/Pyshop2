import random


# def title():
#     title_first = ['S', ' ']
#     ch_s = random.choice(title_first)
#     title_first = ['W', ' ']
#     ch_w = random.choice(title_first)
#     title_first = ['A', ' ']
#     ch_a = random.choice(title_first)
#     title_first = ['D', ' ']
#     ch_d = random

import random


name_titles = {1: "Varudu",
               2: "Manmadhudu",
               3: "Orange",
               4: "Rangasthalam",
               5: "Valmiki"}

# try:

# except ValueError:
#     print("Invalid value! please enter only numbers: ")
# select = name_titles.get(choice, 'Invali d no.')

choice = int(input("Choose any title from the list with its no: "))
title_list = ['S', 'W', 'A', 'D', 'E', 'S', 'H']


title_copy = title_list.copy()
title_index = title_list[0]
length_title = len(title_list)


def game_tolly(word_title):
    title_first = [word_title, ' ']
    char = random.choice(title_first)
    return char



char3 = ' '
for word in title_list:
    char2 = game_tolly(word)
    char3 += char2 + " "
print(char3)

# char4 = ''
# for num in char3:
#     if num not in title_copy:
#         title_copy.append(num)
# print(title_copy)
#
# secret_number = 7
# guess_count = 0
# guess_limit = 7
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if secret_number == guess:
#         print("Well done! ")
#         break
# else:
#     print("Sorry you failed! ")
