from webbrowser import open as webopen
from time import sleep as delay


def startGUI():
    delay(2)
    webopen('http://127.0.0.1:9090/home')
