from dataclasses import dataclass


@dataclass
class binary:
    """
    Binary class for storing binary data.
    """
    start: bytes = b"\x01" # Start of Heading
    end: bytes = b"\x04" # End of Transmission