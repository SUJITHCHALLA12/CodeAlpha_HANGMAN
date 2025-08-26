HANGMAN = ["First stage", "Second stage", "..."]  # Your hangman images/stages
chosen_word = "apple"
word_guessed = ["_"] * len(chosen_word)
guessed_letters = []
attempts = len(HANGMAN) - 1

while attempts != 0 and "_" in word_guessed:
    print("\nYou have {} attempts remaining".format(attempts))
    print(" ".join(word_guessed))

    player_guess = input("Please select a letter between A-Z: ").lower()
    if not player_guess.isalpha():
        print("That is not a letter. Please try again.")
        continue
    if len(player_guess) > 1:
        print("Please enter only a single letter.")
        continue
    if player_guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    guessed_letters.append(player_guess)

    if player_guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if letter == player_guess:
                word_guessed[idx] = player_guess
    else:
        print("Incorrect guess.")
        attempts -= 1

    if "_" not in word_guessed:
        print("Congratulations! You guessed the word:", chosen_word)
        break

if "_" in word_guessed:
    print("Game over! The word was:", chosen_word)