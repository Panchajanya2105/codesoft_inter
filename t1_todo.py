class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task added: "{task}"')

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            old_task = self.tasks[index]
            self.tasks[index] = new_task
            print(f'Task updated from "{old_task}" to "{new_task}"')
        else:
            print("Task index out of range.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task deleted: "{removed_task}"')
        else:
            print("Task index out of range.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Your tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}: {task}")

def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '3':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
