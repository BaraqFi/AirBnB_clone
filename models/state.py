from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class State(BaseModel):
    """Represents a state"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new State"""

        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """
        Getter method that returns a list of City instances
        where the city's state_id attribute matches the id
        attribute of the current State instance.
        """
        from models.city import City
        from models import storage

        cities = []

        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities.append(city)

        return cities

    def __str__(self):
        """Return a string representation of a State"""

        return "[State] ({}) {}".format(self.id, self.__dict__)

# Create a new instance of the FileStorage class
storage = FileStorage()

# Reload any previously-saved instances of the State class
storage.reload()

# You can now use the State class and the FileStorage instance to create, modify, and save instances of the State class to the file storage database. For example:
new_state = State()
new_state.name = "California"
storage.new(new_state)
storage.save()
