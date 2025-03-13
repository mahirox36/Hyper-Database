

class columns:
    
    def __init__(self, ColumnName:str, ColumnType:str, ColumnDataType:str|list):
        self.Types = {
                    "Text" : str,
                    "Integer" : int,
                    "Real" : float,
                    "Bool" : bool
                    }
    
        self.DataType = {
                        "Not Null":False,
                        "Primary Key":False,
                        "Primary Key AUTOINCREMENT":False,
                        "Unique":False
                        }
        
        self.ColumnName = ColumnName
        self.ColumnType = self.Types[ColumnType]

        if isinstance(ColumnDataType, list):
            for type in ColumnDataType:
                self.DataType[type] = True

            self.ColumnDataType = [k for k, v in self.DataType.items() if v == True]

        elif isinstance(ColumnDataType, str):
            self.DataType[ColumnDataType] = True
            self.ColumnDataType = next((k for k, v in self.DataType.items() if v == True), None)
    