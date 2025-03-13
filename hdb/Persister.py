from .dataclasses import *

def convert_to_binary(data: str) -> bytes:
    """Convert a string to binary data."""
    return data.encode('utf-8')

def convert_to_string(data: bytes) -> str:
    """Convert binary data to a string."""
    return data.decode('utf-8')

class Persister:
    
    def __init__(self, filename: str):
        """Initialize the Persister with a filename."""
        self.filename = f"{filename}.hdb"
        self.data = b""  # Store binary data

    def save(self) -> None:
        """
        Save data with a binary wrapper.
        :param filename: The name of the file to save/load data.
        """
        with open(self.filename, "rb+") as file:
            file.seek(0)
            self.data = binary.start + file.read() + binary.end
            file.seek(0)  # Move to start
            file.write(self.data)
            file.truncate()  # Remove excess data

    def load(self) -> bytes:
        """Load and return binary data from the file."""
        with open(self.filename, 'rb') as file:
            return file.read()

    def write_binary(self, text: str) -> None:
        """Write binary data from a string."""
        with open(self.filename, "wb") as file:
            file.write(convert_to_binary(text))

    def read_binary(self) -> str:
        """Read binary data and return it as a string."""
        with open(self.filename, "rb") as file:
            return convert_to_string(file.read())
