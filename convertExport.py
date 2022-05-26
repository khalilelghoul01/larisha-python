with open("includes/methods.py", "r") as f:
    code = f.read().replace("export ", "def ").replace(";", ":\n\tpass")
with open("includes/methods.py", "w") as f:
    f.write(code)
