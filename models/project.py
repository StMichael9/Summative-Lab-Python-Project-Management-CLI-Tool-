from models.task import Task

class Project:
    id_counter = 1
    def __init__(self, title, description, due_date ):

        self.id = Project.id_counter
        Project.id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date
        # Initialized an empty list to store multiple Task objects later
        self.tasks = [] 

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [task.to_dict() for task in self.tasks]
        }
    @classmethod
    def from_dict(cls, data):
        project = cls(data.get("title"), data.get("description"), data.get("due_date"))
        project.id = data.get("id", project.id)
        if project.id >= cls.id_counter:
            cls.id_counter = project.id + 1

        raw_tasks = data.get("tasks", [])

        for task in raw_tasks:
            rebuilt_task = Task.from_dict(task)
            project.add_task(rebuilt_task)
        return project
