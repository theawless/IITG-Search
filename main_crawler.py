import urllib.parse
import urllib.request
from queue import Queue
from bs4 import BeautifulSoup


class MainCrawler:

    def __int__(self, search_key_word):
        self.to_search = search_key_word
        self.list_of_links_to_crawl = Queue()
        self.crawled_links = {"#"}

    def crawl(self, url):
        response = urllib.request.urlopen(url)
        html_bytes = response.read()
        soup = BeautifulSoup(html_bytes,'html.parser')

        for link in soup.findAll('a'):
            l = link.get('href')
            if l is not None:
                if l not in self.crawled_links:
                    if "http://www.iitg.ernet" in l and ".pdf" not in l:
                        self.list_of_links_to_crawl.put(l)
                        print(l+"is addd to queue")
        while not self.list_of_links_to_crawl.empty():
            link_to_crawl = self.list_of_links_to_crawl.get()
            print(link_to_crawl)
            self.crawled_links.add(link_to_crawl)
            self.crawl(link_to_crawl)

    def tryit(self):
        self.crawl("http://iitg.ernet.in")


