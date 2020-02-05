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
        '''
        Download .mp4 file and split and write the audio 
        '''

        newVideoName = self.nameFile(video.title)

        tempPath = self.basePath.joinpath(
            'marvin',
            'static',
            'music',
            'library',
            'temp',
            newVideoName +
            '.mp4')
        finalPath = self.basePath.joinpath(
            'marvin', 'static', 'music', 'library', newVideoName + '.mp3')

        video = pafy.new(links)
        bestMp4 = video.getbest(preftype='mp4')
        bestMp4.download(tempPath)

        vid = moviepy.editor.VideoFileClip(tempPath)
        audio = vid.audio
        audio.write_audiofile(finalPath)

        os.remove(tempPath)

    def writeDataFile(self, videoName, link='-', bestlink='-', title='-', author='-', origin='-', playlists=['-'], downloadedPath='-'):
        '''
        Write data files for music files
        '''
        
        filePath = self.basePath.joinpath(
            'marvin',
            'static',
            'music',
            'library',
            'data',
            videoName +
            '.marvin')

        with open(filePath, 'w') as f:
            f.write(f'{videoName.rstrip()}\n')
            f.write(f'{title.rstrip()}\n')
            f.write(f'{author.rstrip()}\n')
            f.write(f'{origin.rstrip()}\n')
            f.write(f'{link.rstrip()}\n')
            f.write(f'{bestlink.rstrip()}\n')
            f.write(f'{downloadedPath.rstrip()}\n')
            for items in playlists:
                f.write(f'{items.rstrip()}\n')

    def readDataFile(self, videoName):
        '''
        Read data files for music files
        '''

        filePath = self.basePath.joinpath(
            'marvin',
            'static',
            'music',
            'library',
            'data',
            videoName +
            '.marvin')

        with open(filePath, 'r') as f:
            lines = f.readlines()

        title = lines[1]
        author = lines[2]
        origin = lines[3]
        link = lines[4]
        bestlink = lines[5]
        downloadedPath = lines[6]
        playlists = []
        for count in range(7, len(lines)):
            playlists.append(lines[counts])

    def nameFile(self, videoName):
        '''
        Hash file names to make names more standard
        '''

        hashed = hashlib.sha224(videoName.encode('utf-8'))
        return hashed.hexdigest()


class PlaylistProcessor(MusicProccessor):

    def __init__(self):
        self.links = []
        self.basePath = (
            pathlib.Path(
                os.path.dirname(__file__))).resolve().parents[1]

    def playlistScraper(self, url):
        '''
        Webscrape youtube playlist and save all video links in a self.links
        '''

        requestedPlaylist = requests.get(url)
        bsoup = bs(requestedPlaylist.text, 'lxml')

        for link in bsoup.find_all('a'):
            linkFound = link.get('href')
            if('watch' in linkFound and 'https://www.youtube.com' + linkFound not in self.links and 'index' in linkFound):
                self.links.append('https://www.youtube.com' + linkFound)

    def writePlaylistFile(self, playlistName):
        '''
        Write data files for playlist files
        '''

        playlistName = self.cleanName(playlistName)
        filePath = self.basePath.joinpath(
            'marvin',
            'static',
            'music',
            'playlist',
            playlistName +
            '.marvin')

    def readPlaylistFile(self, playlistName):
        '''
        Read data files for playlist files
        '''

        playlistName = self.cleanName(playlistName)
        filePath = self.basePath.joinpath(
            'marvin',
            'static',
            'music',
            'playlist',
            playlistName +
            '.marvin')

    def cleanName(self, name):
        '''
        Make more standardized/consistent playlist name files
        '''

        cleanedName = 'marvin'

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
