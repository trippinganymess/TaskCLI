from Utils import Util
from controller import Commands
import os
from  datetime import datetime
from exceptions import InvalidCommandLength
from config import FILE_NAME

def main():

   if not os.path.exists(FILE_NAME):
        print("new database file getting created")
        Util.dump_data([])
   while(True):
        commands_input = Util.get_commands(input("task-cli : "))
        if("exit" in commands_input):
            break
        command_obj = Commands(commands_input)
        try:
            match commands_input[0]:
                case 'add':
                    if(len(commands_input) < 3):
                        raise InvalidCommandLength("The length of the command should be 3")
                    else:
                        command_obj.add()
                case 'update':
                    if(len(commands_input) < 4):
                        raise InvalidCommandLength("The length of the command should be 4")
                    else:
                        command_obj.update()
                case "delete":
                    if(len(commands_input) < 2):
                        raise InvalidCommandLength("The length of the command should be 2")
                    else:
                        command_obj.delete()
                case "ls":
                        command_obj.list()
                case _:
                    print("Wrong command, follow format - command:ID:status:description")
        except InvalidCommandLength as e:
            print(e)
                  
                
if __name__ == "__main__":
    main()