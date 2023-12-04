class CommandInterpreter:
    @staticmethod
    def interpret_command(command, file_system):
        command_parts = command.split()

        if command_parts[0] == "touch":
            if len(command_parts) == 2:
                file_system.touch(command_parts[1])
            else:
                print("Error: Invalid number of arguments for touch.")
        elif command_parts[0] == "mkdir":
            if len(command_parts) == 2:
                file_system.mkdir(command_parts[1])
            else:
                print("Error: Invalid number of arguments for mkdir.")
        elif command_parts[0] == "cp":
            if len(command_parts) == 3:
                file_system.cp(command_parts[1], command_parts[2])
            else:
                print("Error: Invalid number of arguments for cp.")
        elif command_parts[0] == "more":
            if len(command_parts) == 2:
                file_system.more(command_parts[1])
            else:
                print("Error: Invalid number of arguments for more.")
        elif command_parts[0] == "tree":
            if len(command_parts) == 1:
                file_system.tree()
            else:
                print("Error: Invalid arguments for tree.")
        elif command_parts[0] == "mv":
            if len(command_parts) == 3:
                file_system.mv(command_parts[1], command_parts[2])
            else:
                print("Error: Invalid number of arguments for mv.")
        elif command_parts[0] == "cd":
            if len(command_parts) == 2:
                file_system.cd(command_parts[1])
            else:
                print("Error: Invalid number of arguments for cd.")
        elif command_parts[0] == "ls":
            if len(command_parts) == 1:
                file_system.ls()
            else:
                print("Error: Invalid arguments for ls.")
        elif command_parts[0] == "nano":
            if len(command_parts) == 2:
                file_system.nano(command_parts[1])
            else:
                print("Error: Invalid arguments for nano.")
        else:
            print("Error: Unknown command")