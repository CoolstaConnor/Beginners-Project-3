def word_guess_game():
    word_to_guess = "SNAKE"
    max_attempts = 6
    black = "⬛️"
    yellow = "🟨"
    green = "🟩"

    print("Welcome to Wordle! You have 6 chances to guess a 5-letter word.")

    for attempt in range(max_attempts):
        guess = input(f"Attempt {attempt + 1}: Guess a word: ").strip().upper()
        
        if len(guess) < 5:
            print("Not enough letters!")
            continue
        if len(guess) > 5:
            print("Only 5-letter words!")
            continue
        if not guess.isalpha():
            print("Letters only!")
            continue
        
        feedback = ""
        for i in range(5):
            if guess[i] == word_to_guess[i]:
                feedback += green  # Correct letter and position
            elif guess[i] in word_to_guess:
                feedback += yellow  # Correct letter but wrong position
            else:
                feedback += black  # Letter not in the word
        print(feedback)
        if word_to_guess == guess:
            print(f"Congratulations! You guessed {word_to_guess} correctly!")
            exit()
    
    print(f"Unfortunate! The word was '{word_to_guess}'.")

word_guess_game()