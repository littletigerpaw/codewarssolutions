tasks = []

def show_menu():
   print("\n--- Task Manager ---")
   print("1. Add Task")
   print("2. View Tasks")
   print("3. Delete Task")
   print("4. Quit")

def add_task():
   task = input("Enter a new task: ")
   tasks.append(task)
   print("Task added!")

def view_tasks():
   if not tasks:
       print("No tasks yet.")
   else:
       print("\nYour Tasks:")
       for i, task in enumerate(tasks, start=1):
           print(f"{i}. {task}")

def delete_task():
   view_tasks()
   if tasks:
       try:
           task_num = int(input("Enter task number to delete: "))
           removed = tasks.pop(task_num - 1)
           print(f"Deleted task: {removed}")
       except (ValueError, IndexError):
           print("Invalid task number.")

def main():
   print("Welcome to the Command Line Task Manager! 🎉")

   while True:
       show_menu()
       choice = input("Choose an option (1-4): ")

       if choice == "1":
           add_task()
       elif choice == "2":
           view_tasks()
       elif choice == "3":
           delete_task()
       elif choice == "4":
           print("Goodbye! 👋")
           break
       else:
           print("Invalid choice. Try again.")

main()