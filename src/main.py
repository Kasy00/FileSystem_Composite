from src.CommandInterpreter import CommandInterpreter
from src.FileSystem import FileSystem

if __name__ == "__main__":
    file_system = FileSystem()

    file_system.mkdir("Documents")
    file_system.cd("Documents")
    file_system.touch("file1.txt")
    file_system.touch("file2.txt")

    file_system.cd("..")
    file_system.mkdir("Downloads")
    file_system.cd("Downloads")
    file_system.touch("file3.txt")

    file_system.cd("..")

    while True:
        user_input = input("Enter command (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        CommandInterpreter.interpret_command(user_input, file_system)
