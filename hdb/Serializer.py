# Custom Encoding and Decoding from binary to JSON

# Structured Data:
# in the beginning, we have a info about the database until the first 0x04
# after that, we have a list of tables starts with 0x01 and ends with 0x04
# each table has a name and a list of columns and a primary keys and unique
# and the columns data gonna be a string
# the string format gonna be like this:
# name:type:default:primary:unique

{
    "columns": {
        "id": {
            "type": "int",
            "default": 0,
            "primary": True,
            "unique": True
        },
        "name": {
            "type": "str",
            "default": "",
            "primary": False,
            "unique": False
        }
    },
    "primary_keys": ["id"],
    "primary_key_indices": {
        "id": 0
    },
    "unique_columns": ["id"],
    "index_map": {
        "id": 0,
        "name": 1
    }
}