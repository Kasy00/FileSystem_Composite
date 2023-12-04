
from src.Composite import Directory
from src.Leaf import File


class FileSystem:
    def __init__(self):
        self.current_directory = None
        self.root = Directory("root")
        self.current_directory = self.root

    def touch(self, name):
        if not self.component_exists(name):
            file = File(name)
            self.current_directory.add_component(file)
        else:
            print(f"Error: {name} already exists.")

    def mkdir(self, name):
        if not self.component_exists(name):
            directory = Directory(name)
            self.current_directory.add_component(directory)
        else:
            print(f"Error: {name} already exists.")

    def cp(self, source_name, destination_name):
        source = self.find_component(source_name)
        destination = self.find_component(destination_name)

        if source and destination and isinstance(destination, Directory):
            if isinstance(source, File):
                copy = File(source.name)
                destination.add_component(copy)
            else:
                print("Error: Source must be a file.")
        else:
            print("Error: Source or destination not found or destination is not a directory.")

    def more(self, file_name):
        file = self.find_component(file_name)
        if isinstance(file, File):
            print(' '.join(file.content))
        else:
            print(f"Error: {file_name} is not a file.")

    def tree(self):
        self.root.display()

    def mv(self, source_name, destination_name):
        source = self.find_component(source_name)
        destination = self.find_component(destination_name)

        if source and destination and isinstance(destination, Directory):
            destination.add_component(source)
            self.current_directory.components.remove(source)
        else:
            print("Error: Source or destination not found or destination is not a directory.")

    def cd(self, directory_name):
        if directory_name == "..":
            if self.current_directory != self.root:
                self.current_directory = self.root
                return
            else:
                print("Error: Already at the root directory.")
                return

        directory = self.find_component(directory_name)
        if directory and isinstance(directory, Directory):
            self.current_directory = directory
        else:
            print(f"Error: {directory_name} not found or is not a directory.")

    def ls(self):
        for component in self.current_directory.components:
            if isinstance(component, Directory) or isinstance(component, File):
                component.display_ls()
        print()

    def nano(self, name):
        file = self.find_component(name)
        if isinstance(file, File):
            print(f"Editing {file.name} Enter content and type exit to save.")
            content = []
            while True:
                line = input()
                if line.lower() == 'exit':
                    break
                content.append(line)
            file.set_content(content)
            print(f"Content saved to {file.name}.")
        else:
            print(f"Error: {file.name} is not a file.")

    def find_component(self, name):
        if not name:
            return None

        path_parts = name.split("/")
        current_directory = self.current_directory if name[0] != '/' else self.root

        for part in path_parts:
            if part == '..':
                if current_directory != self.root:
                    current_directory = current_directory.parent
            elif part and current_directory:
                component = current_directory.find_child(part)
                if component:
                    current_directory = component
                else:
                    return None

        return current_directory

    def component_exists(self, name):
        for component in self.current_directory.components:
            if component.name == name:
                return True
        return False

