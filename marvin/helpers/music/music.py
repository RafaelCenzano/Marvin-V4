import requests
from bs4 import BeautifulSoup as bs
import pafy
import moviepy.editor
import os
import hashlib

class MusicProccessor:

    def __init__(self):
        pass

    def download(self, videoLink):
        # New video name using shortest hashing method.
        newVideoName = hashlib.sha224(video.title.encode('utf-8')).hexdigest()

        # Paths for files
        tempPath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'marvin', 'static', 'music', 'library', 'temp') + newVideoName + '.mp4'
        finalPath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'marvin', 'static', 'music', 'library') + newVideoName + '.mp3'

        # Proccess and download videos
        video = pafy.new(links)
        bestMp4 = video.getbest(preftype='mp4')
        bestMp4.download(tempPath)

        vid = moviepy.editor.VideoFileClip(tempPath)
        audio = vid.audio
        audio.write_audiofile(finalPath)

        os.remove(tempPath)

    def writeDataFile(self, link, bestlink, videoName):
        dataPath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'marvin', 'static', 'music', 'library', 'data') + videoName + '.marvin'

    def readDataFile(self, videoName):
        dataPath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'marvin', 'static', 'music', 'library', 'data') + videoName + '.marvin'

class PlaylistProcessor(MusicProccessor):

    def __init__(self):
        self.links = []

    def playlistScraper(self, url):

        # Request and proccess webpage
        requestedPlaylist = requests.get(url)
        bsoup = bs(requestedPlaylist.text, 'lxml')

        # Search and find all video links
        for link in bsoup.find_all('a'):
            linkFound = link.get('href')
            if('watch' in linkFound and 'https://www.youtube.com' + linkFound not in self.links and 'index' in linkFound):
                self.links.append('https://www.youtube.com' + linkFound)

    def writePlaylistFile(self, playlistName):
        playlistName = self.cleanName(playlistName)
        os.path.isfile(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'marvin', 'static', 'music', 'playlist', playlistName + '.marvin'))

    def readPlaylistFile(self, playlistName):
        playlistName = self.cleanName(playlistName)
        os.path.isfile(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'marvin', 'static', 'music', 'playlist', playlistName + '.marvin'))

    def cleanName(self, name):
        # Add marvin in front to make sure all file names start with something consistent that won't mess with things
        cleanedName = 'marvin'

        # loop through and replace spaces with '_'
        count = 0
        while count < len(name):

            if name[count:count + 1] == ' ':
                cleanedName += '_'
            else:
                cleanedName += name[count:count + 1]
            count += 1

        return cleanedName

if __name__ == '__main__':
    pass
