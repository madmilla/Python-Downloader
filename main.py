from urllib.parse import urlsplit
import requests
from sys import argv
import os
from bs4 import BeautifulSoup
script, albumlink  = argv

class downloader(object):
    pass

class listal_iterator(object):
    def __init__(self,link,folder):
        self.link = link
        self.folder = folder
        self.word_list = []
        self.loop_iterator()


    def loop_iterator(self):
        i = 1
        x = True
        while x:
            count = self.download_listal_album(i)

            print ( str(self.folder),'\t page:', i , ' \tCount: ', count)
            i += 1
            if count == 0:
                x = False
        print(' DONE ', str(self.folder))
        with open("test.txt", "w") as file:
            file.write(str(self.word_list))
        return

    def download_listal_album(self,page):
        html = requests.get(self.link +'/'+str(page)).text
        soup = BeautifulSoup(html, "lxml")
        i = 0
        for text in soup.find_all('div', class_='imagewrap-inner'):
            for links in text.find_all('a'):
                data = "https://ilarge.lisimg.com/image/"+links.get('href').rsplit('/', 1)[-1]+"/500000full-.jpg"
                self.appendList(data)
            i += 1
        return i

    def appendList(self, link):
        self.word_list.append(link)
        self.word_list.append(self.folder)

class iterator(object):

    def __init__(self, download_link, engine):
        self.download_link = download_link
        self.engine = engine
        self.where_to_store = input("Where do you want to store it?")
        if not os.path.exists(self.where_to_store):
            os.makedirs(self.where_to_store)

    def retrieve_all_links(self):
        print("Retrieve data")
        print(f"{self.where_to_store}")
        pass

    # data = [0,1,2,3,4,5]
    #
    # with open("test.txt", "w") as file:
    #     file.write(str(data))
    #
    # with open("test.txt", "r") as file:
    #     data2 = eval(file.readline())

class main(object):
    def __init__(self, link):
        self.stripped_downloadlink = self.strip_albumlink(link)
        self.actual_link = link
        self.crawler = 'None'
        print(self.stripped_downloadlink)
        print(self.actual_link)
        if self.stripped_downloadlink == "https://www.listal.com/":
            self.crawler = listal_iterator(self.actual_link, 'keri')

    def strip_albumlink(self, albumlink):
        url = albumlink
        base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
        return base_url


a_main = main(albumlink)
