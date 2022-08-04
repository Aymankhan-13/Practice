import random


def play():
    user = input("p for paper, r for rock, s for scissors.")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie.'

    if is_win(user, computer):
        return 'You won!'

    return ''