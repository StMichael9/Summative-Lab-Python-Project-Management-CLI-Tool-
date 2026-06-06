import argparse
from utils.storage import load_data, save_data
from models.user import User
from models.project import Project
from models.task import Task
from rich import print

users = load_data()

def add_user(args):
    user = User(args.name, args.email)
    users.append(user)
    save_data(users)
    print(f"User '{args.name}' created.")

def list_users(args):
    for user in users:
        print(f"{user.id}: {user.name} ({user.email})")

def add_project(args):
    user = next((u for u in users if u.name == args.user), None)
    if not user:
        print("User not found.")
        return
    project = Project(args.title, args.description, args.due_date)
    user.add_project(project)
    save_data(users)
    print(f"Project '{args.title}' added to {args.user}.")

def list_projects(args):
    user = next((u for u in users if u.name == args.user), None)
    if not user:
        print("User not found.")
        return
    for project in user.projects:
        print(f"{project.id}: {project.title} - {project.description} (Due: {project.due_date})")

def add_task(args):
    user = next((u for u in users if u.name == args.user), None)
    if not user:
        print("User not found.")
        return
    project = user.get_project_by_title(args.project)
    if not project:
        print("Project not found.")
        return
    task = Task(args.title, args.assigned_to)
    project.add_task(task)
    save_data(users)
    print(f"Task '{args.title}' added to project '{args.project}'.")

def complete_task(args):
    user = next((u for u in users if u.name == args.user), None)
    if not user:
        print("User not found.")
        return
    project = user.get_project_by_title(args.project)
    if not project:
        print("Project not found.")
        return
    task = next((t for t in project.tasks if t.title == args.title), None)
    if not task:
        print("Task not found.")
        return
    task.complete()
    save_data(users)
    print(f"Task '{args.title}' marked complete.")

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers()

    u = subparsers.add_parser("add-user")
    u.add_argument("--name")
    u.add_argument("--email")
    u.set_defaults(func=add_user)

    lu = subparsers.add_parser("list-users")
    lu.set_defaults(func=list_users)

    p = subparsers.add_parser("add-project")
    p.add_argument("--user")
    p.add_argument("--title")
    p.add_argument("--description")
    p.add_argument("--due_date")
    p.set_defaults(func=add_project)

    lp = subparsers.add_parser("list-projects")
    lp.add_argument("--user")
    lp.set_defaults(func=list_projects)

    t = subparsers.add_parser("add-task")
    t.add_argument("--user")
    t.add_argument("--project")
    t.add_argument("--title")
    t.add_argument("--assigned_to")
    t.set_defaults(func=add_task)

    ct = subparsers.add_parser("complete-task")
    ct.add_argument("--user")
    ct.add_argument("--project")
    ct.add_argument("--title")
    ct.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


