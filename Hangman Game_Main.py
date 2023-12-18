import random
from hangman_art import stages,logo
from hangman_words import word_list

print(logo)
hangman_words = random.choice(word_list).lower()
check_list = []
for letter in range(0,len(hangman_words)):
    check_list += "_"
print('\n',check_list,'\n')
end_of_game = False
chance = 0
while not end_of_game:
    user_letter = str(input("Guess a letter:")).lower()

    if user_letter in check_list:
        print(f"The letter {user_letter} is already guessed before")

    for position in range(0,len(hangman_words)):
        if user_letter == hangman_words[position]:
            check_list[position] = hangman_words[position]
    print('\n',check_list,'\n')

    if user_letter not in hangman_words:
        chance -= 1
        print(f"\n The Letter {user_letter} is not present and you lose a life")
        print(stages[chance])

    if '_' not in check_list:
        print("\n Congratulations on completing the game")
        end_of_game = True
    elif chance ==-7:
        print("Better Luck Next Time")
        end_of_game = True












