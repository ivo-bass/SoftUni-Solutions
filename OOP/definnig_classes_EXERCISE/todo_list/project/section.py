# from OOP.definnig_classes_EXERCISE.todo_list.project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        try:
            filtered_task = [t for t in self.tasks if t.name == task_name][0]
            filtered_task.completed = True
            return f"Completed task {filtered_task.name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        uncompleted = [t for t in self.tasks if not t.completed]
        count = len(self.tasks) - len(uncompleted)
        self.tasks = uncompleted
        return f"Cleared {count} tasks."

    def view_section(self):
        info = f"Section {self.name}:\n"
        for t in self.tasks:
            info += f"{t.details()}\n"
        return info

# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# print(section.complete_task("Go to University"))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
