from marvin.helpers.starting import startUpTasks
from threading import Thread
from marvin import core

'''
Run Flask App for Marvin GUI
'''


if __name__ == '__main__':
    thread_start = Thread(target=startUpTasks)
    thread_start.start()

    core.marvinGui().run()
