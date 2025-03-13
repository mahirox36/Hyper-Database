from enum import Enum, auto



class ColumnType(Enum):
    """
    Enum for column types.
    """
    STRING = auto()
    INTEGER = auto()
    FLOAT = auto()
    BOOLEAN = auto()
    DATE = auto()
    TIME = auto()
    DATETIME = auto()
    TIMESTAMP = auto()
    JSON = auto()

class ColumnDataType(Enum):
    """
    Enum for column data types.
    """
    NOT_NULL = auto()
    PRIMARY_KEY = auto()
    AUTOINCREMENT = auto()
    UNIQUE = auto()
    DEFAULT = auto()
    FOREIGN_KEY = auto()