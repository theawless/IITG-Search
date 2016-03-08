import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

def crawl(url):
    response = urllib.request.urlopen(url)
    html_bytes = response.read()
    html_string = ''
    html_string = html_bytes.decode("utf-8")
    #finder = LinkFinder(Spider.base_url, page_url)
    #finder.feed(html_string)
    #print(html_string)
    soup = BeautifulSoup(response)
    for link in soup.findAll('a'):
        print(link.get('href'))

crawl("https://en.wikipedia.org/wiki/Python_%28programming_language%29")
