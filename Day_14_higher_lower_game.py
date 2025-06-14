
logo = r"""
   __  ___       __             
  / / / (_)___ _/ /_  ___  _____
 / /_/ / / __ `/ __ \/ _ \/ ___/
/ __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/    
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

"""

print(logo)


from Day_14_Data import data  # Your data list of accounts
import random

def format_data(account): 
    """Format the account data into printable string"""
    name = account["name"]
    profession = account["profession"]
    country = account["country"]
    return f"{name}, a {profession}, from {country}"

def check_answer(user_guess, a_followers, b_followers):
    """Check if user guessed correctly"""
    if a_followers > b_followers:
        return user_guess == "A"
    else:
        return user_guess == "B"

# Game start
print(logo)
score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data (account_a)}")
    print("VS")
    print(f"Against B: {format_data (account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_followers = account_a["followers"]
    b_followers = account_b["followers"]

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"✅ You're right! Current score: {score}.")
    else:
        print(f"❌ Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

exit()
