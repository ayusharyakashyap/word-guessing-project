import random

def display_welcome_message():
    welcome_message = [
        "Welcome to Hangman! A word will be chosen at random and",
        "you must try to guess the word correctly letter by letter",
        "before you run out of attempts. Good luck!"
    ]
    for line in welcome_message:
        print(line)

def get_random_word(words_list):
    return random.choice(words_list).lower()

def display_hangman(attempts_left, hangman_stages):
    if attempts_left < len(hangman_stages):
        print(hangman_stages[-attempts_left-1])
    else:
        print(hangman_stages[0])

def get_player_guess(guessed_letters):
    while True:
        player_guess = input("\nPlease select a letter between A-Z\n> ").lower()
        if not player_guess.isalpha():
            print("That is not a letter. Please try again.")
        elif len(player_guess) > 1:
            print("That is more than one letter. Please try again.")
        elif player_guess in guessed_letters:
            print("You have already guessed that letter. Please try again.")
        else:
            return player_guess

def update_word_guessed(chosen_word, player_guess, word_guessed):
    for index, letter in enumerate(chosen_word):
        if letter == player_guess:
            word_guessed[index] = player_guess

def play_game(words, hangman_stages, total_attempts):
    chosen_word = get_random_word(words)
    guessed_letters = []
    word_guessed = ["-" for _ in chosen_word]
    attempts_left = total_attempts

    while attempts_left > 0 and "-" in word_guessed:
        print(f"\nYou have {attempts_left} attempts remaining")
        print("".join(word_guessed))
        player_guess = get_player_guess(guessed_letters)
        guessed_letters.append(player_guess)

        if player_guess in chosen_word:
            update_word_guessed(chosen_word, player_guess, word_guessed)
        else:
            attempts_left -= 1
            display_hangman(attempts_left, hangman_stages)

    if "-" not in word_guessed:
        print(f"\nCongratulations! {chosen_word} was the word")
    else:
        print(f"\nUnlucky! The word was {chosen_word}.")

def main():
    display_welcome_message()

    words = [
        "hangman", "chairs", "backpack", "bodywash", "clothing",
        "computer", "python", "program", "glasses", "sweatshirt",
        "sweatpants", "mattress", "friends", "clocks", "biology",
        "algebra", "suitcase", "knives", "ninjas", "shampoo"
    ]
# The words have been hard coded for the easiness of both the host and the player
    hangman_stages = [
        """
        -----
        |   |
        |
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |  -+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\\
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\\
        |   |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\\
        |   |
        |   |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\\
        |   |
        |   |
        |  |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\\
        |   |
        |   |
        |  |
        |  |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\\
        |   |
        |   |
        |  | |
        |  |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\\
        |   |
        |   |
        |  | |
        |  | |
        |
        --------
        """
    ]

    total_attempts = 15  # Set the desired number of attempts here, in this case it is 15

    play_again = True
    while play_again:
        play_game(words, hangman_stages, total_attempts)
        response = input("\nWould you like to play again? (yes/no)\n> ").lower()
        play_again = response in ("yes", "y")

if __name__ == "__main__":
    main()
