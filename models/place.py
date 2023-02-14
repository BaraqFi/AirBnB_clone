from models.base_model import BaseModel
from engines.file_storage import FileStorage


class Place(BaseModel):
    """Defines the Place class."""

    # Define the class attributes
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize the Place object."""
        super().__init__(*args, **kwargs)

    @property
    def city(self):
        """Return the City instance associated with this Place."""
        from models.city import City
        from models import storage

        return storage.get(City, self.city_id)

    @property
    def user(self):
        """Return the User instance associated with this Place."""
        from models.user import User
        from models import storage

        return storage.get(User, self.user_id)

    @property
    def amenities(self):
        """Return the list of Amenity instances associated with this Place."""
        from models.amenity import Amenity
        from models import storage

        amenities = []
        for amenity_id in self.amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            if amenity:
                amenities.append(amenity)

        return amenities
