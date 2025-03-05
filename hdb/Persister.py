from .dataclasses import binary

def convert_to_binary(data: str) -> bytes:
    """
    Convert a string to binary data.
    
    :param data: The string to convert.
    :return: The binary representation of the string.
    """
    return data.encode('utf-8')  # Convert string directly to bytes

class Persister:
    def __init__(self, filename: str):
        """
        Initialize the Persister with a filename.
        
        :param filename: The name of the file to save/load data.
        """
        self.filename = f"{filename}.hdb"
        self.data = binary.start + binary.end  # Directly concatenate bytes objects

    def save(self):
        with open(self.filename, 'wb') as file:
            file.write(self.data)

    def load(self):
        with open(self.filename, 'rb') as file:
            return file.read()  # Read entire file