from models.project import Project

class User:
    id_counter = 1
    
    def __init__(self, name, email):
        # Track and advance the unique user id_counter
        self.id = User.id_counter
        User.id_counter += 1

        # Assign name and email attributes
        self.name = name
        self.email = email
        
        #Set up an empty list to manage multiple Project objects
        self.projects = []
        

    def add_project(self, project):
        # 4. How do you append a project object to this user's list?
        self.projects.append(project)
      

    def get_project_by_title(self, title):
        # 5. This needs to loop through self.projects. 
        for project in self.projects:
            if project.title == title:
                return project
        return None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [project.to_dict() for project in self.projects],
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"], data["email"])
        user.id = data.get("id", user.id)
        user.projects = [Project.from_dict(project) for project in data.get("projects", [])]
        if user.id >= cls.id_counter:
            cls.id_counter = user.id + 1
        return user
