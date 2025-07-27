from datetime import datetime

def log_mood():
    print("\n💬 How are you feeling today?")
    mood = input("Enter your mood (e.g., Happy, Sad, Stressed, Excited): ")

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")

    with open("mood_log.txt", "a") as file:
        file.write(f"{date_str} - Mood: {mood}\n")

    print("✅ Mood logged successfully!")

log_mood()
