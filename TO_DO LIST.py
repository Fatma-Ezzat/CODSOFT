import json
import os
from datetime import datetime


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def loadTasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


def saveTasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def showTasks(tasks):
    if not tasks:
        print("No tasks existed.")
        return

    print("Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['title']} - {task['status']}")


def addTask(tasks):
    title = input("Enter task title: ")
    new_task = {
        "title": title,
        "status": "Not Started",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    saveTasks(tasks)
    print("Task added successfully.")


def update_task(tasks):
    showTasks(tasks)
    taskIndex = int(input("Enter task number to update: ")) - 1

    if taskIndex < 0 or taskIndex >= len(tasks):
        print("Invalid task number.")
        return

    task = tasks[taskIndex]
    print(f"Selected task: {task['title']} - {task['status']}")
    new_status = input("Enter new status (e.g., Not Started, In Progress, Completed): ")
    task['status'] = new_status
    task['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    saveTasks(tasks)
    print("Task updated successfully.")


def delete_task(tasks):
    showTasks(tasks)
    task_index = int(input("Enter task number to delete: ")) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return

    task = tasks.pop(task_index)
    saveTasks(tasks)
    print(f"Deleted task: {task['title']}")


def main():
    tasks = loadTasks()

    while True:
        clearScreen()
        print("To-Do List")
        print("1.Show All Tasks")
        print("2.Create Task")
        print("3.Edit Task")
        print("4.Remove Task")
        print("5.Exit")

        choice = input("Enter the number of your desired operation: ")

        if choice == "1":
            clearScreen()
            showTasks(tasks)
            input("Press Enter to continue...")
        elif choice == "2":
            clearScreen()
            addTask(tasks)
            input("Press Enter to continue...")
        elif choice == "3":
            clearScreen()
            update_task(tasks)
            input("Press Enter to continue...")
        elif choice == "4":
            clearScreen()
            delete_task(tasks)
            input("Press Enter to continue...")
        elif choice == "5":
            clearScreen()
            print("See you soon^")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()