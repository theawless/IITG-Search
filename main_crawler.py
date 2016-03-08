import sys
import urllib.parse
import urllib.request
from queue import Queue
from bs4 import BeautifulSoup
import BgThread
import setlog

logger = setlog.logger

number_of_threads = 10


class MainCrawler:
    def __init__(self, search_key_word=None):
        self.to_search = search_key_word
        self.list_of_links_to_crawl = Queue()
        self.crawled_links = {"#"}

        self.threads = []
        print(str(number_of_threads))
        for i in range(number_of_threads):
            print(str(i))
            self.threads.append(BgThread.BackgroundThread(self))

    def spider_job(self, url):

        try:
            response = urllib.request.urlopen(url)
            html_bytes = response.read()
        except urllib.error.HTTPError:
            print("Exception : Can't download page")
            return
        # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa9 in position 12030: invalid start byte
        except UnicodeDecodeError:
            print("Exception : UnicodeDecodeError")
        else:
            soup = BeautifulSoup(html_bytes, 'html.parser')
            for link in soup.findAll('a'):
                l = link.get('href')
                if l is not None:
                    if l not in self.crawled_links:
                        if "http://www.iitg.ernet" in l and ".pdf" not in l and ".ppt" not in l:
                            self.list_of_links_to_crawl.put(l)
                            print(l + "is added to queue")
            while not self.list_of_links_to_crawl.empty():
                link_to_crawl = self.list_of_links_to_crawl.get()
                print(link_to_crawl)
                self.crawled_links.add(link_to_crawl)
                self.spider_job(link_to_crawl)

    def crawl_in_pages(self, url):
        response = urllib.request.urlopen(url)
        html_bytes = response.read()
        string = html_bytes.decode('utf-8')
        if self.to_search in string:
            print("Page found :D  :D " + url)
            sys.exit()


crawler = MainCrawler("inkulu")
crawler.spider_job("http://iitg.ernet.in")


'''
crawler.threads[0].start()
crawler.threads[1].start()

while crawler.list_of_links_to_crawl.qsize()<190:
    pass

logger.debug("A")
crawler.threads[0].join()
logger.debug("B")
crawler.threads[1].join()

logger.debug("*********************************************************************************")
while not crawler.list_of_links_to_crawl.empty():
    try:
        print(crawler.list_of_links_to_crawl.get())
    except:
        print("poop")
'''
