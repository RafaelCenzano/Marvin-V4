import requests
from bs4 import BeautifulSoup as bs
import pafy
import moviepy.editor
import os
import hashlib

class PlaylistProcessor():
    links = []

    def __init__(self):
        pass

    def playlistScraper(self):
        # Request and proccess webpage
        requestedPlaylist = requests.get('https://www.youtube.com/playlist?list=PL96cyyGcpt5Xk4WEq0tTG109lQC41bJD3')
        bsoup = bs(requestedPlaylist.text, 'lxml')

        # Search and find all video links
        for link in bsoup.find_all('a'):
            linkFound = link.get('href')
            if('watch' in linkFound and 'https://www.youtube.com' + linkFound not in self.links and 'index' in linkFound):
                self.links.append('https://www.youtube.com' + linkFound)

class PlaylistDownloader():

    def __init__(self):
        pass

    def download(self, videoLinks):
        for links in videoLinks:
            # New video name
            newVideoName = hashlib.sha512(video.title).hexdigest()

            # Paths for files
            tempPath = os.path.join('marvin', 'static', 'music', 'library', 'temp') + newVideoName + '.mp4'
            dataPath = os.path.join('marvin', 'static', 'music', 'library', 'data') + newVideoName + '.txt'
            finalPath = os.path.join('marvin', 'static', 'music', 'library') + newVideoName + '.mp3'

            # Proccess and download videos
            video = pafy.new(links)
            bestMp4 = video.getbest(preftype='mp4')
            bestMp4.download(tempPath)

            vid = moviepy.editor.VideoFileClip(tempPath)
            audio = vid.audio
            audio.write_audiofile(finalPath)

            os.remove(tempPath)

if __name__ == '__main__':

    testOBJ = PlaylistProcessor()
    testOBJ.playlistScraper()
    #for items in testOBJ.links:
    #    print(items)
    testOBJ1 = PlaylistDownloader()
    testOBJ1.download(testOBJ.links)