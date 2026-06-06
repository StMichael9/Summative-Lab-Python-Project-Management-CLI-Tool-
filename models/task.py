class Task:
    id_counter = 1

    def __init__(self, title, assigned_to=None):
        self.id = Task.id_counter
        # update counter by 1 so the next task gets a unique number
        Task.id_counter += 1

        self.title = title
        self.status = "pending"
        self.assigned_to = assigned_to

    def complete(self):
        self.status = "complete"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data.get("title"), data.get("assigned_to"))
        task.id = data.get("id", task.id)
        task.status = data.get("status", task.status)
        if task.id >= cls.id_counter:
            cls.id_counter = task.id + 1
        return task