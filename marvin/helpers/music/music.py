import requests
from bs4 import BeautifulSoup as bs
import pafy
import moviepy.editor
import os
import hashlib
import pathlib


class MusicProccessor:

    def __init__(self):
        self.basePath = (
            pathlib.Path(
                os.path.dirname(__file__))).resolve().parents[1]

    def download(self, videoLink):
        # New video name using shortest hashing method.
        newVideoName = nameFile(video.title)

        # Paths for files
        tempPath = self.basePath.joinpath(
            'marvin',
            'static',
            'music',
            'library',
            'temp',
            newVideoName +
            '.mp4')
        tempPath = self.basePath.joinpath(
            'marvin', 'static', 'music', 'library', newVideoName + '.mp3')

        # Proccess and download videos
        video = pafy.new(links)
        bestMp4 = video.getbest(preftype='mp4')
        bestMp4.download(tempPath)

        vid = moviepy.editor.VideoFileClip(tempPath)
        audio = vid.audio
        audio.write_audiofile(finalPath)

        os.remove(tempPath)

    def writeDataFile(self, link, bestlink, videoName):
        filePath = self.basePath.joinpath(
            'marvin',
            'static',
            'music',
            'library',
            'data',
            videoName +
            '.marvin')

    def readDataFile(self, videoName):
        filePath = self.basePath.joinpath(
            'marvin',
            'static',
            'music',
            'library',
            'data',
            videoName +
            '.marvin')

    def nameFile(self, videoName):
        hashed = hashlib.sha224(videoName.encode('utf-8'))
        return hashed.hexdigest()


class PlaylistProcessor(MusicProccessor):

    def __init__(self):
        self.links = []
        self.basePath = (
            pathlib.Path(
                os.path.dirname(__file__))).resolve().parents[1]

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
        filePath = self.basePath.joinpath(
            'marvin',
            'static',
            'music',
            'playlist',
            playlistName +
            '.marvin')

    def readPlaylistFile(self, playlistName):
        playlistName = self.cleanName(playlistName)
        filePath = self.basePath.joinpath(
            'marvin',
            'static',
            'music',
            'playlist',
            playlistName +
            '.marvin')

    def cleanName(self, name):
        # Add marvin in front to make sure all file names start with something
        # consistent that won't mess with things
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
    testOBJ = MusicProccessor()
    testOBJ.test()
    testOBJ1 = PlaylistProcessor()
    testOBJ1.test()
