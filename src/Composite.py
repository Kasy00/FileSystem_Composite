from src.Component import FileSystemComponent


class Directory(FileSystemComponent):
    def __init__(self, name, parent=None):
        self.name = name
        self.components = []
        self.parent = parent

    def add_component(self, component):
        component.parent = self
        self.components.append(component)

    def display(self, level=0):
        print("  " * level + f"{self.name}")
        for component in self.components:
            component.display(level + 1)

    def display_ls(self):
        print(f"{self.name}", end=" ")

    def find_child(self, name):
        for component in self.components:
            if component.name == name:
                return component
        return None