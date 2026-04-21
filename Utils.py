import json
from config import FILE_NAME

class Util:
    def __init__(self, input_obj) -> None:
        self.input_obj = input_obj
        
    
    @staticmethod
    def get_commands(command):
        commands = command.split(':')
        return commands
    
    
    def save_to_Database(self):
        data = []
        with open(FILE_NAME, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        new_record = {
            "ID" : self.input_obj.ID,
            "status" : self.input_obj.status,
            "description" : self.input_obj.description,
            "createdAt" : self.input_obj.createdAt,
            "lastUpdate" : self.input_obj.lastUpdate
        }
        data.append(new_record)
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)
    @staticmethod
    def load_data():
        with open(FILE_NAME, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                    print("No data to be updated, add new data!!")
                    return
    @staticmethod
    def dump_data(data):
        with open(FILE_NAME, 'w') as f:
            return json.dump(data,f, indent=4)