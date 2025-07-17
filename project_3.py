import random

def get_directions():
    directions = {
        "north": "You head north into a forest with towering trees.",
        "south": "You walk south toward a calm beach.",
        "east": "You travel east and reach a bustling town.",
        "west": "You move west and find a steep mountain.",
    }

    print("📍 You are at a crossroad. Choose a direction: north, south, east, or west")

    while True:
        direction = input("➡️ Enter direction: ").lower()
        if direction in directions:
            print(directions[direction])
            break
        else:
            print("❌ Invalid direction. Try again.")

if __name__ == '__main__':
    get_directions()




