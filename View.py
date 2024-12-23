from flask import render_template

def index():
    return render_template('index.html')

def blog():
    return render_template('blog.html')

def blog_page():
    return render_template('blog_page.html')

def chats():
    return render_template('chats.html')

def friend():
    return render_template('friend.html')

def popular():
    return render_template('popular.html')

def profile():
    return render_template('profile.html')

def register():
    return render_template('register.html')

# Interfaces for UI components
class Field:
    def assignType(self, type):
        pass

class Table:
    def initBase(self, rows, columns):
        pass

class Button:
    def assignAction(self, action):
        pass

class Layer:
    def assignType(self, type):
        pass

    def add(self, obj, x, y):
        pass

class InterfaceObject:
    def setParams(self, length, height):
        pass

    def process(self):
        pass

class InterfaceFabric:
    def createWindow(self):
        pass

    def createButton(self):
        pass

    def createField(self):
        pass

    def createTable(self):
        pass

    def createLayer(self):
        pass

# Classes for UI components
class DefaultInterface:
    def createWindow(self):
        pass

    def createButton(self):
        pass

    def createField(self):
        pass

    def createTable(self):
        pass

    def createLayer(self):
        pass

class Platform:
    def __init__(self, fabric):
        self.fabric = fabric
        self.windows = {}

    def createInterface(self):
        pass

    def processInterface(self):
        pass

    def showWindow(self, name):
        pass

    def getWindows(self):
        return self.windows

class RunPlatform:
    def runPlatform(self):
        pass
