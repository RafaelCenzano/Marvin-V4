import os

def cacheCleaner():
    pathsToRemoveFiles = []
    pathsToRemoveDirs = []
    pathToFolder = os.getcwd()

    for (root,dirs,files) in os.walk('.', topdown=True):
        dirsChecking = root[2:]
        if root[2:6] != 'venv':
            for directories in dirs:
                if '__pycache__' == directories:
                    pathsToRemoveDirs.append(os.path.join(pathToFolder,dirsChecking,directories))
            for f in files:
                name, ext = os.path.splitext(f)
                if '.pyc' == ext:
                    pathsToRemoveFiles.append(os.path.join(pathToFolder,dirsChecking,f))
    for paths in pathsToRemoveFiles:
        if os.path.exists(paths):
            os.remove(paths)
    for paths in pathsToRemoveDirs:
        if os.path.exists(paths):
            os.rmdir(paths)

if __name__ == '__main__':
    while True:
        print('What do you want to clean?')
        print('1. Cache')
        print('2. Exit')
        WhattoDO = input('>')
        if WhattoDO == '1' or WhattoDO.lower() == 'cache':
            cacheCleaner()
        elif WhattoDO == '2' or WhattoDO.lower() == 'exit':
            break