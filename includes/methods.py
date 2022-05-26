

import time as times
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
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
    return math.copysign(1, a)


def sqrt(a):
    return math.sqrt(a)


def pow(a, b):
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


def atan2(a, b):
    return math.atan2(a, b)


def sinh(a):
    return math.sinh(a)


def cosh(a):
    return math.cosh(a)


def tanh(a):
    return math.tanh(a)


def asinh(a):
    return math.asinh(a)


def acosh(a):
    return math.acosh(a)


def atanh(a):
    return math.atanh(a)


def random(a):
    return random.random()


def randomInt(a, b):
    return random.randint(a, b)


def randomFloat(a, b):
    return random.uniform(a, b)


def randomGaussian(a, b):
    return random.gauss(a, b)


#####################################################
# array functions                                   #
#####################################################


def init(a):
    return [0] * a


def append(a, b):
    return a.append(b)


def insert(a, b, c):
    return a.insert(b, c)


def remove(a, b):
    return a.remove(b)


def removeAt(a, b):
    return a.pop(b)


def pop(a):
    return a.pop()


def tail(a):
    return a[1:]


def head(a):
    return a[0]


def clear(a):
    return a.clear()


def reverse(a):
    return a.reverse()


def sort(a):
    return a.sort()


def toString(a):
    return str(a)


def indexOf(a, b):
    return a.index(b)


def valueOf(a, b):
    return a[b]


def toArray(a):
    return list(a)


#####################################################
# selenium functions                                #
#####################################################


def firefox(width, height, headless):
    firefox = webdriver.Firefox()
    firefox.set_window_size(width, height)
    if headless:
        firefox.set_window_position(0, 0)
        firefox.set_window_size(1, 1)
    return firefox


def chrome(width, height, headless):
    chrome = webdriver.Chrome()
    chrome.set_window_size(width, height)
    if headless:
        chrome.set_window_position(0, 0)
        chrome.set_window_size(1, 1)
    return chrome


def get(driver, url):
    driver.get(url)


def getTitle(driver):
    return driver.title


def getUrl(driver):
    return driver.current_url


def getPageSource(driver):
    return driver.page_source


def getCurrentWindowHandle(driver):
    return driver.current_window_handle


def getWindowHandles(driver):
    return driver.window_handles


def findElement(driver, by, value):
    if by == "id":
        return driver.find_element_by_id(value)
    elif by == "name":
        return driver.find_element_by_name(value)
    elif by == "class":
        return driver.find_element_by_class_name(value)
    elif by == "css":
        return driver.find_element_by_css_selector(value)
    elif by == "xpath":
        return driver.find_element_by_xpath(value)
    elif by == "link":
        return driver.find_element_by_link_text(value)
    else:
        return driver.find_element_by_tag_name(value)


def findElements(driver, by, value):
    if by == "id":
        return driver.find_elements_by_id(value)
    elif by == "name":
        return driver.find_elements_by_name(value)
    elif by == "class":
        return driver.find_elements_by_class_name(value)
    elif by == "css":
        return driver.find_elements_by_css_selector(value)
    elif by == "xpath":
        return driver.find_elements_by_xpath(value)
    elif by == "link":
        return driver.find_elements_by_link_text(value)
    else:
        return driver.find_elements_by_tag_name(value)



def close(driver):
    driver.close()


def quit(driver):
    driver.quit()


def sendKeys(element, keys):
    keysDict = {
        "ENTER": Keys.ENTER,
        "TAB": Keys.TAB,
        "SPACE": Keys.SPACE,
        "BACKSPACE": Keys.BACKSPACE,
        "DELETE": Keys.DELETE,
        "ESCAPE": Keys.ESCAPE,
        "PAGE_UP": Keys.PAGE_UP,
        "PAGE_DOWN": Keys.PAGE_DOWN,
        "END": Keys.END,

        "HOME": Keys.HOME,
        "LEFT": Keys.LEFT,
        "UP": Keys.UP,
        "RIGHT": Keys.RIGHT,
        "DOWN": Keys.DOWN,
        "INSERT": Keys.INSERT,
        "F1": Keys.F1,
        "F2": Keys.F2,
        "F3": Keys.F3,
        "F4": Keys.F4,
        "F5": Keys.F5,
        "F6": Keys.F6,
        "F7": Keys.F7,
        "F8": Keys.F8,
        "F9": Keys.F9,
        "F10": Keys.F10,
        "F11": Keys.F11,
        "F12": Keys.F12,
    }
    if(keys in keysDict):
        element.send_keys(keysDict[keys])
    else:
        element.send_keys(keys)


def clear(element):
    element.clear()


def click(element):
    element.click()


def submit(element):
    element.submit()


#####################################################
# time functions                                    #
#####################################################

def wait(seconds):
    times.sleep(seconds)
def time():
	return str(times.time() * 1000)
def timestamp():
	return str(times.time())
def date():
	return str(times.strftime("%Y-%m-%d"))