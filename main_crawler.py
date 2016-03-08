import urllib.parse
import urllib.request
from queue import Queue
from bs4 import BeautifulSoup

q = Queue()

def crawl(url):
    response = urllib.request.urlopen(url)
    html_bytes = response.read()
    soup = BeautifulSoup(html_bytes,'html.parser')
    #print(soup.prettify())
    for link in soup.findAll('a'):
        l = link.get('href')
        print(l)
        if 0:
            continue
            print("B")
        #crawl(l)
        q.put(l)

while not q.empty():
    print(q.get())

r = Queue()
print("Creating queue")
r.put("abhi1")
r.put("abhi2")
r.put("abhi3")
r.put("abhi4")
print(r.get())
print(r.get())
print(r.get())


crawl("http://iitg.ernet.in")
