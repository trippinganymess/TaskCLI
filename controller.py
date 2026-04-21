from Utils import Util
from Input import Input
from config import FILE_NAME
from datetime import datetime

class Commands:
    def __init__(self, commmands) -> None:
        self.commands = commmands
        self.time = datetime.now().isoformat()
    def add(self):
        ID = Input.get_next_ID(FILE_NAME)
        input_obj = Input(status=self.commands[1], description=self.commands[2], ID=ID, createdAt=self.time, lastUpdate=self.time) # status on pos 1, description on pos 2
        utility = Util(input_obj=input_obj)
        utility.save_to_Database()
    
    def update(self):
        data = []
        found = False
        data = Util.load_data()
        if data:
            for entry in data:
                    if entry.get("ID") == int(self.commands[1]): # command:ID:status:description
                        entry["status"] = self.commands[2] # ID on 2 position
                        entry["description"] = self.commands[3]
                        entry["lastUpdate"] = self.time # description on 3 position 
                        found = True
                
        if found:
                Util.dump_data(data)
                print("data was updated successfully!!")
        else:
                 print("ID not found")
        
    def delete(self):
            data = Util.load_data()
            if data:
                target_ID = int(self.commands[1])
                new_data = [entry for entry in data if entry['ID'] != target_ID]
                if(len(new_data) < len(data)):
                        Util.dump_data(new_data)
                        print(f"elements at {target_ID} has been successfully deleted!!")
            else:
                print("Wrong Index, data not found!!")
                
    def list(self):
        data = Util.load_data()
        if data:
            for entry in data:
                print(f"{entry['ID']:<5} | {entry['status']:<12} | {entry['description']}")
        else:
            print("no entries!!")
