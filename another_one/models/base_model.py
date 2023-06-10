from uuid import uuid4
from datetime import datetime

# Define BaseModel Class.
class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """ Initialize BaseModel Instance"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    
    def save(self):
        """records update time"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Return dictionary of the BaseModel Instance."""
        diction = {}
        diction = (self.__dict__).copy()
        diction["__class__"] = self.__class__.__name__
        diction["created_at"] = self.created_at.isoformat()
        diction["updated_at"] = self.updated_at.isoformat()
        return diction
    def __str__(self):
        """Returns string representation of object"""
        clssname = self.__class__.__name__
        return "[{}] ({}) {}".format(clssname, self.id, self.__dict__)
