# task_manager_app/task.py

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def to_dict(self):
        """Convert Task object into dictionary for saving."""
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task object from dictionary data."""
        return cls(
            data.get("name", ""),
            data.get("description", ""),
            data.get("priority", "")
        )