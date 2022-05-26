import os
import sys
from antlr4 import *
from dist.LarishaLexer import LarishaLexer
from dist.LarishaParser import LarishaParser
from dist.LarishaVisitor import LarishaVisitor
from larisha import run_code
args = sys.argv[1:]
if len(args) == 0:
    print("Usage: larisha.py <file>")
    sys.exit(1)
path = args[0]
currentWorkingDir = os.path.dirname(os.path.realpath(path))
with open(path, "r") as f:
    code = f.read()
os.chdir(currentWorkingDir)
run_code(code)
