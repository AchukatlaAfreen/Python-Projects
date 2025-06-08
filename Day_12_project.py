from random import randint

guess_the_number_logo = '''
   ____     _   _U _____ u____    ____          _____   _   _ U _____ u      _   _       _   _   __  __     ____  U _____ u   ____     
U /"___|uU |"|u| \| ___"|/ __"| u/ __"| u      |_ " _| |'| |'|\| ___"|/     | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u  
\| |  _ / \| |\| ||  _|"<\___ \/<\___ \/         | |  /| |_| |\|  _|"      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/  
 | |_| |   | |_| || |___ u___) | u___) |        /| |\ U|  _  |u| |___      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <    
  \____|  <<\___/ |_____||____/>>|____/>>      u |_|U  |_| |_| |_____|      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\   
  _)(|_  (__) )(  <<   >> )(  (__))(  (__)     _// \\_ //   \\ <<   >>      ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_  
 (__)__)     (__)(__) (__|__)    (__)         (__) (__|_") ("_|__) (__)     (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__) 
'''
print(guess_the_number_logo)

# Constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_guess):
    if user_guess > actual_guess:
        print("Too High 😱.")
        return False
    elif user_guess < actual_guess:
        print("Too low 🥲")
        return False
    else:
        print(f"You got it! The answer was {actual_guess} 🎉")
        return True

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game 🎲!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1, 100)

    
    turns = set_difficulty()
    guessed_correctly = False

    while turns > 0 and not guessed_correctly:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        guessed_correctly = check_answer(guess, answer)
        turns -= 1 if not guessed_correctly else 0

    if not guessed_correctly:
        print(f"😔 You've run out of guesses. The number was {answer}.")


game()

                                                                                                                                       
