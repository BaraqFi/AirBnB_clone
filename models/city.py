import models.base_model
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city, which is a geographical location that contains places.
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new City instance.
        """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the City instance.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        Returns a dictionary representation of the City instance.
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            if key != "_sa_instance_state":
                dictionary[key] = value
        dictionary["__class__"] = type(self).__name__
        return dictionary
