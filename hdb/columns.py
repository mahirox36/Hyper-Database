from .enums import ColumnType, ColumnDataType
from typing import List, Union


class columns:
    def __init__(self, ColumnName:str, ColumnType:ColumnType, ColumnDataType: Union[ColumnDataType, List[ColumnDataType]]):
        self.ColumnName = ColumnName
        self.ColumnType = ColumnType
