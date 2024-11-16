class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False
    def mark_as_completed(self):
        """Відмічає завдання як виконане."""
        self.completed = True

    def __str__(self):
        """Повертає строкове представлення завдання."""
        status = "Виконано" if self.completed else "Не виконано"
        return f"Завдання: {self.title}\nОпис: {self.description}\nДедлайн: {self.deadline}\nСтатус: {status}\n"



class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Додає завдання до списку."""
        self.tasks.append(task)

    def remove_task(self, task_title):
        """Видаляє завдання зі списку за назвою."""
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def mark_task_completed(self, task_title):
        """Відмічає завдання як виконане за назвою."""
        for task in self.tasks:
            if task.title == task_title:
                task.mark_as_completed()

    def show_tasks(self):
        """Виводить список всіх завдань."""
        if not self.tasks:
            print("Немає завдань.")
        else:
            for task in self.tasks:
                print(task)