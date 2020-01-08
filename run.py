from marvin.helpers.starting import startGUI
from threading import Thread
from marvin import app

'''
Run Flask App for Marvin GUI
'''


if __name__ == '__main__':
    thread_start = Thread(target=startGUI)
    thread_start.start()

    app.run(
        port=9090
    )
