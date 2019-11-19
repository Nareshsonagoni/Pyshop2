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
