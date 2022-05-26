

import math
import os
import shutil
import sys
from includes.override import printf
import requests


#####################################################
# IO functions                                      #
#####################################################


def readFile(file):
    with open(file, "r") as f:
        return f.read()


def writeFile(file, data):
    with open(file, "w") as f:
        f.write(data)


def appendFile(file, data):
    with open(file, "a") as f:
        f.write(data)


def deleteFile(file):
    os.remove(file)


def renameFile(oldPath, newPath):
    os.rename(oldPath, newPath)


def createFile(path):
    with open(path, "w") as f:
        f.write("")


def copyFile(oldPath, newPath):
    shutil.copyfile(oldPath, newPath)


def moveFile(oldPath, newPath):
    shutil.move(oldPath, newPath)


def existsFile(path):
    return os.path.exists(path)


def isFile(path):
    return os.path.isfile(path)


def isDir(path):
    return os.path.isdir(path)


def createDir(path):
    os.mkdir(path)


def deleteDir(path):
    shutil.rmtree(path)


def getCurrentDir():
    return os.getcwd()


#####################################################
# http functions                                    #
#####################################################


def httpGet(url):
    return requests.get(url).text


def httpPost(url, data):
    return requests.post(url, data).text


def httpPut(url, data):
    return requests.put(url, data).text


def httpDelete(url):
    return requests.delete(url).text


def httpHead(url):
    return requests.head(url).text


def httpOptions(url):
    return requests.options(url).text


def httpPatch(url, data):
    return requests.patch(url, data).text


def httpGetJson(url):
    return requests.get(url).json()


def httpPostJson(url, data):
    return requests.post(url, data).json()


def httpPutJson(url, data):
    return requests.put(url, data).json()


def httpDeleteJson(url):
    return requests.delete(url).json()


def httpHeadJson(url):
    return requests.head(url).json()


def httpOptionsJson(url):
    return requests.options(url).json()


def httpPatchJson(url, data):
    return requests.patch(url, data).json()


#####################################################
# IO functions                                      #
#####################################################


def println(data):
    printf(data)


def print(data):
    printf(data, end="")


def readLine(data):
    return input(data)


def printErr(data):
    printf(data, file=sys.stderr)


def exit(code):
    sys.exit(code)


def argv():
    return sys.argv


#####################################################
# String functions                                 #
#####################################################


def replace(a, b):
    return a.replace(b, "")


def split(a, b):
    return a.split(b)


def join(a, b):
    return a.join(b)


def trim(a):
    return a.strip()


def trimLeft(a):
    return a.lstrip()


def trimRight(a):
    return a.rstrip()


def trimAll(a):
    return a.strip().lstrip().rstrip()


def match(a, b):
    return a.match(b)


def matchAll(a, b):
    return a.findall(b)


def equals(a, b):
    return a == b


def toLower(a):
    return a.lower()


def toUpper(a):
    return a.upper()


def count(a, b):
    return a.count(b)


def indexOf(a, b):
    return a.index(b)


def lastIndexOf(a, b):
    return a.rindex(b)


def substring(a, b, c):
    return a[b:c]


def endsWith(a, b):
    return a.endswith(b)


def startsWith(a, b):
    return a.startswith(b)


def isEmpty(a):
    return len(a) == 0


def isNumber(a):
    return a.isdigit()


def isInteger(a):
    return a.isdigit()


def isLower(a):
    return a.islower()


def isUpper(a):
    return a.isupper()


def isAlpha(a):
    return a.isalpha()


def isAlphaNumeric(a):
    return a.isalnum()


def isWhitespace(a):
    return a.isspace()


def swapCase(a):
    return a.swapcase()


#####################################################
# Math functions                                    #
#####################################################

def floor(a):
	return math.floor(a)
def ceil(a):
	return math.ceil(a)
def round(a):
	return math.round(a)
def abs(a):
	return math.fabs(a)
def sign(a):
	return math.copysign(1,a)
def sqrt(a):
	return math.sqrt(a)
def pow(a,b):
	return a**b
def exp(a):
	return math.exp(a)
def log(a):
	return math.log(a)
def log2(a):
	return math.log2(a)
def log10(a):
	return math.log10(a)
def sin(a):
	return math.sin(a)
def cos(a):
	return math.cos(a)
def tan(a):
	return math.tan(a)
def asin(a):
	return math.asin(a)
def acos(a):
	return math.acos(a)
def atan(a):
	return math.atan(a)
def atan2(a,b):
	return  math.atan2(a,b)
def sinh(a):
	return math.sinh(a)
def cosh(a):
	return math.cosh(a)
def tanh(a):
	return math.tanh(a)
def asinh(a):
	return math.asinh(a)
def acosh(a):
	return  math.acosh(a)
def atanh(a):
	return  math.atanh(a)
def random(a):
	return random.random()
def randomInt(a,b):
	return random.randint(a,b)
def randomFloat(a,b):
	return random.uniform(a,b)
def randomGaussian(a,b):
	return random.gauss(a,b)
