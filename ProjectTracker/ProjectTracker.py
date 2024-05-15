""" contains the project tracker class"""

import sqlite3


class ProjectTracker:
    """The class for the project tracker"""

    def __init__(self, username: str) -> None:
        self.conn = sqlite3.connect("projects.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS projects (
                project_name TEXT PRIMARY KEY,
                project_description TEXT,
                project_status TEXT
            )"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS updates (
                project_name TEXT,
                update_description TEXT,
                FOREIGN KEY (project_name) REFERENCES projects (project_name)
            )"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS tobedone (
                project_name TEXT,
                tobedone_description TEXT,
                FOREIGN KEY (project_name) REFERENCES projects (project_name)
            )"""
        )

        self.conn.commit()

    def add_project(self, project_name: str, project_description: str) -> None:
        """Adds a project to the project tracker

        Args:
            project_name (str): The project name
            project_description (str): The project description
        """
        self.cursor.execute(
            "INSERT INTO projects VALUES (?, ?, ?)",
            (project_name, project_description, "In Progress"),
        )
        self.conn.commit()

    def update_project(self, project_name: str, update_description: str) -> None:
        """Adds an update to the project

        Args:
            project_name (stsr): The project name
            update_description (str): The update description
        """
        self.cursor.execute(
            "INSERT INTO updates VALUES (?, ?)",
            (project_name, update_description),
        )
        self.conn.commit()

    def tobedone_project(self, project_id: int, tobedone_description: str) -> None:
        """Adds a to be done note to the project

        Args:
            project_id (int): The project id
            tobedone_description (str): The to be done description
        """
        self.cursor.execute(
            "INSERT INTO tobedone VALUES (?, ?)",
            (project_id, tobedone_description),
        )
        self.conn.commit()

    def get_projects(self, current_only: bool = False) -> list[dict]:
        """Gets all the projects in the project tracker

        Returns:
            list[dict]: The list of projects
        """
        if current_only:
            self.cursor.execute(
                "SELECT * FROM projects WHERE project_status = 'In Progress'"
            )
        else:
            self.cursor.execute("SELECT * FROM projects")
        return self.cursor.fetchall()

    def get_update(self, project_name: str) -> list[dict]:
        """Gets all the updates for a project

        Args:
            project_name(str): The project name

        Returns:
            list[dict]: The list of updates
        """
        self.cursor.execute(
            "SELECT updates.update_description FROM updates, projects WHERE projects.project_name = ?",
            (project_name,),
        )
        return self.cursor.fetchall()


x = ProjectTracker("test")
x.update_project("Project 1", "This is the first update")
# x.add_project("Project 1", "This is the first project")
print(x.get_update("Project 1"))
