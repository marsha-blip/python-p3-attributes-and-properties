APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name: str = "Dog", breed: str = "Beagle"):
        # Use the property setters to initialize, which will validate
        self.name = name
        self.breed = breed

    @property
    def name(self) -> str:
        """Get the dog's name."""
        return self._name

    @name.setter
    def name(self, value: str):
        # Validate that it's a string of length 1–25
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def breed(self) -> str:
        """Get the dog's breed."""
        return self._breed

    @breed.setter
    def breed(self, value: str):
        # Validate that it’s in the approved list
        if value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value
