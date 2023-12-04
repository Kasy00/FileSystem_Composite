from src.Component import FileSystemComponent


class File(FileSystemComponent):
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

    def display(self, level=0):
        print("  " * level + f"{self.name}")

    def display_ls(self):
        print(f"{self.name}", end=" ")

    def set_content(self, content):
        self.content = content
