import random

word_list = ["afreen", "rizwana", "sulthana"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
place_holder = ["_"] * word_length

print("Guess the word: " + " ".join(place_holder))

while "_" in place_holder:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        # Loop through each position using range
        for position in range(word_length):
            if chosen_word[position] == guess:
                place_holder[position] = guess
        print("Right! " + " ".join(place_holder))
    else:
        print("Wrong! Try again.")

print("Congratulations! You guessed the word:", chosen_word)