import requests
from bs4 import BeautifulSoup as bs
import pafy
import moviepy.editor
import os

class PlaylistProcessor():
    links = []

    def __init__(self):
        pass

    def playlistScraper(self):
        requestedPlaylist = requests.get('https://www.youtube.com/playlist?list=PL96cyyGcpt5Xk4WEq0tTG109lQC41bJD3')
        bsoup = bs(requestedPlaylist.text, 'lxml')

        for link in bsoup.find_all('a'):
            linkFound = link.get('href')
            if('watch' in linkFound and 'https://www.youtube.com' + linkFound not in self.links and 'index' in linkFound):
                self.links.append('https://www.youtube.com' + linkFound)

class PlaylistDownloader():

    def __init__(self):
        pass

    def download(self, videoLinks):
        for links in videoLinks:
            video = pafy.new(links)
            bestMp4 = video.getbest(preftype='mp4')
            bestMp4.download(video.title + '.mp4')
            vid = moviepy.editor.VideoFileClip(video.title + '.mp4')
            audio = vid.audio
            audio.write_audiofile(video.title + '.mp3')
            os.remove(video.title + '.mp4')

if __name__ == '__main__':

    testOBJ = PlaylistProcessor()
    testOBJ.playlistScraper()
    #for items in testOBJ.links:
    #    print(items)
    testOBJ1 = PlaylistDownloader()
    testOBJ1.download(testOBJ.links)