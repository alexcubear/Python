user1 = str(input('What\'s the first players\'s name?')).capitalize()
user2 = str(input('And the second players\'s?')).capitalize()
user1turn = input(user1 + ', rock, paper or scissors?')
user2turn = input(user2 + ', rock, paper or scissors?')


def compare():
    if user1turn == user2turn:
        return 'It\'s a tie!'
    elif user1turn == 'rock':
        if user2turn == 'scissors':
            return 'Rock wins!'
        else:
            return 'Paper wins!'
    elif user1turn == 'scissors':
        if user2turn == 'paper':
            return 'Scissors win!'
        else:
            return 'Rock wins!'
    elif user1turn == 'paper':
        if user2turn == 'rock':
            return 'Paper wins!'
        else:
            return 'Scissors win!'
    else:
        return 'Try again.'

print(compare())
