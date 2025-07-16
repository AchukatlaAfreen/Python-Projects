import csv
from datetime import datetime

FILE_NAME = 'expenses.csv'


def initialize_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ") or datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (e.g., food, travel): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description (optional): ")

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!")

def view_expenses():
    print("\n📋 All Expenses:")
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def summary():
    totals = {}
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cat = row['Category']
            amt = float(row['Amount'])
            totals[cat] = totals.get(cat, 0) + amt

    print("\n📊 Expense Summary by Category:")
    for category, amount in totals.items():
        print(f"{category}: ₹{amount:.2f}")

def main():
    initialize_file()
    while True:
        print("""
========= Expense Tracker =========
1. Add Expense
2. View All Expenses
3. Show Summary
4. Exit
        """)
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary()
        elif choice == '4':
            print("👋 Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()



todos = []

def add_task():
    task = input("Enter task: ")
    todos.append({"task": task, "status": "Pending"})
    print("✅ Task added!")

def view_tasks():
    print("\n📝 To-Do List:")
    for i, t in enumerate(todos, 1):
        print(f"{i}. {t['task']} - {t['status']}")

def mark_done():
    view_tasks()
    try:
        i = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= i < len(todos):
            todos[i]['status'] = 'Done'
            print("✅ Task marked as done!")
        else:
            print("❌ Invalid task number")
    except ValueError:
        print("❌ Please enter a valid number")

def delete_task():
    view_tasks()
    try:
        i = int(input("Enter task number to delete: ")) - 1
        if 0 <= i < len(todos):
            removed = todos.pop(i)
            print(f"🗑️ Deleted: {removed['task']}")
        else:
            print("❌ Invalid task number")
    except ValueError:
        print("❌ Please enter a valid number")

def main():
    while True:
        print("""
========= To-Do List Manager =========
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
        """)
        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()


