class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.task_counter = 1  # Ensures unique task IDs

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\n=== Task List ===")
            for task_id, task in self.tasks.items():
                status = "✅ Completed" if task["completed"] else "❌ Pending"
                print(f"{task_id}. {task['name']} (Priority: {task['priority']}) - {status}")
            print("=================")

    def add_task(self):
        task_name = input("Enter task name: ").strip()
        priority = input("Enter task priority (High/Medium/Low): ").strip().capitalize()

        if priority not in {"High", "Medium", "Low"}:
            print("Invalid priority. Defaulting to 'Low'.")
            priority = "Low"

        self.tasks[self.task_counter] = {"name": task_name, "priority": priority, "completed": False}
        print(f"Task added successfully with ID {self.task_counter}.")
        self.task_counter += 1

    def update_task(self):
        self.display_tasks()
        try:
            task_id = int(input("Enter task ID to update: "))
            if task_id in self.tasks:
                task_status = input("Enter 'completed' to mark as completed, 'pending' to mark as pending: ").strip().lower()
                if task_status == "completed":
                    self.tasks[task_id]["completed"] = True
                    print("Task marked as completed.")
                elif task_status == "pending":
                    self.tasks[task_id]["completed"] = False
                    print("Task marked as pending.")
                else:
                    print("Invalid status. No changes made.")
            else:
                print("Invalid task ID.")
        except ValueError:
            print("Please enter a valid numeric task ID.")

    def delete_task(self):
        self.display_tasks()
        try:
            task_id = int(input("Enter task ID to delete: "))
            if task_id in self.tasks:
                del self.tasks[task_id]
                print(f"Task ID {task_id} deleted successfully.")
            else:
                print("Invalid task ID.")
        except ValueError:
            print("Please enter a valid numeric task ID.")

    def search_tasks(self):
        search_term = input("Enter keyword to search for: ").strip().lower()
        results = {tid: task for tid, task in self.tasks.items() if search_term in task["name"].lower()}

        if results:
            print("\n=== Search Results ===")
            for task_id, task in results.items():
                status = "✅ Completed" if task["completed"] else "❌ Pending"
                print(f"{task_id}. {task['name']} (Priority: {task['priority']}) - {status}")
            print("======================")
        else:
            print("No tasks match the search term.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Exit")
        print("=======================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            todo_list.add_task()
        elif choice == "3":
            todo_list.update_task()
        elif choice == "4":
            todo_list.delete_task()
        elif choice == "5":
            todo_list.search_tasks()
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


