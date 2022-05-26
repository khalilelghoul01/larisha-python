import re

def parse(value:str):
    if value.isdecimal():
        return int(value)
    if re.match(r'^-?\d+(?:\.\d+)$', value) is not None:
        return float(value)
    if value == "true" or value == "false":
        return value == "true"
    if value[0] == "'" and value[-1] == "'":
        return value[1:-1]
    if value[0] == '"' and value[-1] == '"':
        return value[1:-1]


def getType(value):
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "string"
    if isinstance(value, bool):
        return "bool"
    error(f"Unknown type for {value}")


class breakpoint:
    def __init__(self):
        pass

class returnpoint:
    def __init__(self, value = None):
        self.value = value
    
    def getValue(self):
        return self.value

    def __str__(self) -> str:
        return f"returnpoint({self.value})"

def error(msg:str):
    print("\033[91m[ERROR] " + msg + "\033[0m")
    exit(1)