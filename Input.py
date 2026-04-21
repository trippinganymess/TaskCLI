from exceptions import DescriptionTooLong
from exceptions import DescriptionTooShort
import json

class Input:
    def __init__(self, status, description, ID, createdAt, lastUpdate) -> None:
        self.status = status
        self.description = description
        self.ID = ID
        self.createdAt = createdAt
        self.lastUpdate = lastUpdate
    @property
    def status(self):
        return self._status.lower().strip()
    
    @property
    def description(self):
        return self._description.lower().strip()
    
    @status.setter
    def status(self, status):
        if status.lower().strip() in ["todo", "in-progress", "done"]:
           self._status = status
        else:
            raise ValueError("Wrong status value.")
    @description.setter
    def description(self, description):
        if(len(description) < 1 ):
            raise DescriptionTooShort("The description is too short")
        if(len(description) < 200):
            self._description = description
        else:
            raise DescriptionTooLong("The description is too long")
    
    
    @staticmethod
    def get_next_ID(filename):
            with open(filename, "r") as f:
                data = json.load(f)
            if not data:
                return 1
            last_id = data[-1]["ID"]
            return last_id + 1
    
                