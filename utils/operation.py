from utils import common


def mult(left, right):
    if(common.getType(left) == "int" and common.getType(right) == "int"):
        return int(left * right)
    if(common.getType(left) == "float" and common.getType(right) == "float"):
        return float(left * right)
    if(common.getType(left) == "int" and common.getType(right) == "float"):
        return float(left * right)
    if(common.getType(left) == "float" and common.getType(right) == "int"):
        return float(left * right)
    if(common.getType(left) == "string" and common.getType(right) == "int"):
        return left * right
    if(common.getType(left) == "int" and common.getType(right) == "string"):
        return left * right
    common.error(f"Cannot multiply {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")
        

def div(left, right):
    if((common.getType(left) in ["int","float"] ) and (common.getType(right) in ["int","float"] )):
        if(left == 0 or right == 0):
            common.error(f"Cannot divide {left} by {right}")
    if(common.getType(left) == "int" and common.getType(right) == "int"):
        return float(left / right)
    if(common.getType(left) == "float" and common.getType(right) == "float"):
        return float(left / right)
    if(common.getType(left) == "int" and common.getType(right) == "float"):
        return float(left / right)
    if(common.getType(left) == "float" and common.getType(right) == "int"):
        return float(left / right)
    common.error(f"Cannot divide {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")

def mod(left, right):
    if((common.getType(left) in ["int","float"] ) and (common.getType(right) in ["int","float"] )):
        if(left == 0 or right == 0):
            common.error(f"Cannot divide {left} by {right}")
    if(common.getType(left) == "int" and common.getType(right) == "int"):
        return int(left % right)
    if(common.getType(left) == "float" and common.getType(right) == "float"):
        return int(left % right)
    if(common.getType(left) == "int" and common.getType(right) == "float"):
        return int(left % right)
    if(common.getType(left) == "float" and common.getType(right) == "int"):
        return int(left % right)
    common.error(f"Cannot mod {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")

def add(left, right):
    if(common.getType(left) == "string" and common.getType(right) == "string"):
        return left + right
    if(common.getType(left) == "int" and common.getType(right) == "int"):
        return int(left + right)
    if(common.getType(left) == "float" and common.getType(right) == "float"):
        return float(left + right)
    if(common.getType(left) == "int" and common.getType(right) == "float"):
        return float(left + right)
    if(common.getType(left) == "float" and common.getType(right) == "int"):
        return float(left + right)
    if(common.getType(left) == "string" and common.getType(right) == "int"):
        return left + right
    if(common.getType(left) == "int" and common.getType(right) == "string"):
        return left + right
    if(common.getType(left) == "string" and common.getType(right) == "float"):
        return left + right
    if(common.getType(left) == "float" and common.getType(right) == "string"):
        return left + right
    if(common.getType(left) == "string" and common.getType(right) == "bool"):
        return left + right
    if(common.getType(left) == "bool" and common.getType(right) == "string"):
        return left + right
    common.error(f"Cannot add {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")


def sub(left, right):
    if(common.getType(left) == "int" and common.getType(right) == "int"):
        return int(left - right)
    if(common.getType(left) == "float" and common.getType(right) == "float"):
        return float(left - right)
    if(common.getType(left) == "int" and common.getType(right) == "float"):
        return float(left - right)
    if(common.getType(left) == "float" and common.getType(right) == "int"):
        return float(left - right)
    common.error(f"Cannot subtract {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")

def lt(left, right):
    if(common.getType(left) == "int" and common.getType(right) == "int"):
        return left < right
    if(common.getType(left) == "float" and common.getType(right) == "float"):
        return left < right
    if(common.getType(left) == "int" and common.getType(right) == "float"):
        return left < right
    if(common.getType(left) == "float" and common.getType(right) == "int"):
        return left < right
    common.error(f"Cannot compare {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")

def gt(left, right):
    if(common.getType(left) == "int" and common.getType(right) == "int"):
        return left > right
    if(common.getType(left) == "float" and common.getType(right) == "float"):
        return left > right
    if(common.getType(left) == "int" and common.getType(right) == "float"):
        return left > right
    if(common.getType(left) == "float" and common.getType(right) == "int"):
        return left > right
    common.error(f"Cannot compare {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")


def le(left, right):
    if(common.getType(left) == "int" and common.getType(right) == "int"):
        return left <= right
    if(common.getType(left) == "float" and common.getType(right) == "float"):
        return left <= right
    if(common.getType(left) == "int" and common.getType(right) == "float"):
        return left <= right
    if(common.getType(left) == "float" and common.getType(right) == "int"):
        return left <= right
    common.error(f"Cannot compare {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")


def ge(left, right):
    if(common.getType(left) == "int" and common.getType(right) == "int"):
        return left >= right
    if(common.getType(left) == "float" and common.getType(right) == "float"):
        return left >= right
    if(common.getType(left) == "int" and common.getType(right) == "float"):
        return left >= right
    if(common.getType(left) == "float" and common.getType(right) == "int"):
        return left >= right
    common.error(f"Cannot compare {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")

def eq(left, right):
    if(common.getType(left) == "int" and common.getType(right) == "int"):
        return left == right
    if(common.getType(left) == "float" and common.getType(right) == "float"):
        return left == right
    if(common.getType(left) == "int" and common.getType(right) == "float"):
        return left == right
    if(common.getType(left) == "float" and common.getType(right) == "int"):
        return left == right
    if(common.getType(left) == "string" and common.getType(right) == "string"):
        return left == right
    if(common.getType(left) == "bool" and common.getType(right) == "bool"):
        return left == right
    common.error(f"Cannot compare {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")


def ne(left, right):
    if(common.getType(left) == "int" and common.getType(right) == "int"):
        return left != right
    if(common.getType(left) == "float" and common.getType(right) == "float"):
        return left != right
    if(common.getType(left) == "int" and common.getType(right) == "float"):
        return left != right
    if(common.getType(left) == "float" and common.getType(right) == "int"):
        return left != right
    if(common.getType(left) == "string" and common.getType(right) == "string"):
        return left != right
    if(common.getType(left) == "bool" and common.getType(right) == "bool"):
        return left != right
    common.error(f"Cannot compare {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")

def and_(left, right):
    if(common.getType(left) == "bool" and common.getType(right) == "bool"):
        return left and right
    common.error(f"Cannot compare {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")

def or_(left, right):
    if(common.getType(left) == "bool" and common.getType(right) == "bool"):
        return left or right
    common.error(f"Cannot compare {left} and {right}:\n\t{common.getType(left)} and {common.getType(right)} are not compatible")



