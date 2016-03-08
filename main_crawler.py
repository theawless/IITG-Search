import urllib.parse
import urllib.request
from queue import Queue
from bs4 import BeautifulSoup

q = Queue()

def crawl(url):
    response = urllib.request.urlopen(url)
    html_bytes = response.read()
    soup = BeautifulSoup(html_bytes,'html.parser')
    for link in soup.findAll('a'):
        l = link.get('href')
        if l != None:
            if "http://www.iitg.ernet" in l and ".pdf" not in l:
                q.put(l)
                print(l+"is addd to queue")
    while not q.empty():
        link_to_crawl = q.get()
        print(link_to_crawl)
        crawl(link_to_crawl)




crawl("http://iitg.ernet.in")
#crawl("http://www.iitg.ernet.in/director/dirmsg.html")

