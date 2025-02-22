class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            print(f'Task updated to "{new_task}".')
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            todo_list.add_task(input("Enter the task: "))
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                index = int(input("Enter task number to update: ")) - 1
                todo_list.update_task(index, input("Enter the new task: "))
            except ValueError:
                print("Invalid number.")
        elif choice == '4':
            todo_list.view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                todo_list.delete_task(index)
            except ValueError:
                print("Invalid number.")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()