from webbrowser import open as webopen
from time import sleep as delay
from threading import Thread
from marvin import app

'''
Run Flask App for Marvin GUI
'''

def startGUI():
    delay(2)
    webopen('http://127.0.0.1:9090/')

if __name__ == '__main__':
    thread_start = Thread(target=startGUI)
    thread_start.start()

    app.run(
        port=9090
    )
