"""

"""
import string

# create a points dictionary using a list of points and a list of letters
alpha = list(string.ascii_lowercase)
beta = list(range(1, 27))
points_dictionary = dict(zip(alpha, beta))


def high(x):
    str_lst = x.split(' ')

    high_word = ''
    high_points = 0

    for word in str_lst:
        current_word = word
        current_points = 0
        for letter in word:
            current_points += points_dictionary.get(letter)
        if current_points > high_points:
            high_points = current_points
            high_word = current_word

    return(high_word)