# import openpyxl as xl
#
#
# wb = xl.load_workbook('transactions.xlsx')
# sheet = wb['Sheet1']
# cell = sheet['a1']
# cell = sheet.cell(1, 1)
# print(cell.value),
import random

title_list = ['S', 'W', 'A', 'R', 'A']
title_copy = []
title_index = title_list[0]


def game_tolly(title_word):
    title_words = [title_word, ' ']
    random_word = random.choice(title_words)
    return random_word


title_with_blanks = ' '
for word in title_list:
    char2 = game_tolly(word)
    title_with_blanks += char2 + " "
    title_blanks_index = title_with_blanks[0]
print(title_with_blanks)
guess = input(">").upper()
guess_indes = title_list.index(guess)
if guess != " ":

guess_count = 0
for item in title_list:
    if guess == item:
        guess_index = title_list[0]  #This should return the index of the guessed letter
        output_title = ' '
        for letter in blank_title_list:
            if item == ' ':
                guess_index = item



    # if guess in title_list:
    #     if guess == char3[item]:
#
#     else:
#         guess = input(" ")
#         guess_count += 1
#         else:t
#
#     for num in title_list:
#         if num not in title_copy:
#             title_copy.append(num)
#             print(title_copy)
#
# if num == guess:







