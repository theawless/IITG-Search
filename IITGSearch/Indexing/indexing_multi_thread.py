# import whoosh
from whoosh.index import create_in
from whoosh.fields import *
from bs4 import BeautifulSoup
from mechanize import Browser
import string
import sys, urllib2, urllib, socket, urllib3
import nltk
import threading

lock = threading.Lock()
from HTMLParser import HTMLParser
from whoosh.qparser import QueryParser

timeout = 3
socket.setdefaulttimeout(timeout)
ana = analysis.StemmingAnalyzer()
schema = Schema(title=TEXT(analyzer=ana, spelling=True), path=ID(stored=True), content=TEXT)
ix = create_in("data2", schema)
writer = ix.writer()
count = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, i, j):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.i = i
        self.j = j

    def run(self):
        print "Starting " + self.name
        indexing(self.name, self.i, self.j)
        print "Exiting " + self.name


def indexing(thread_name, i, j):
    global count, writer, ix, schema, lock
    current_line_number = 0
    with open('mix_links.txt') as fp:
        for line in fp:
            # Jump at line number i and break at line number j
            current_line_number += 1
            if current_line_number < i:
                continue
            elif current_line_number > j:
                break
            count += 1
            url = line
            if ".pdf" not in url and ".jpg" not in url and ".doc" not in url and ".c" not in url and ".cpp" not in url and ".tar" not in url and "zip" not in url and ".exe" not in url and ".asm" not in url and ".JPG" not in url and ".bin" not in url and ".PDF" not in url:
                try:
                    http = urllib3.PoolManager()
                    r = http.request('GET', url)
                    html_content = r.data.decode('utf-8')
                    # f = urllib.urlopen(url)
                    # content1 = f.read()
                    # print content1.info()
                    # print nltk.clean_html(content1)
                    soup = BeautifulSoup(html_content)
                    content_text = soup.get_text()
                    print content_text
                    # soup.find('title')
                    # body = soup.find('h2')
                    # print unicode(soup.get_text().renderContents())
                    lock.acquire()
                    writer.add_document(title=unicode(url, "utf-8"), path=unicode("/" + url, "utf-8"),
                                        content=unicode(content_text, "utf-8"))
                    writer.add_document(title=unicode(url, "utf-8"), path=unicode("/" + url, "utf-8"),
                                        content=unicode(url, "utf-8"))
                    lock.release()
                # writer.add_document(title=u"Second document", path=u"/b",content=u"The second one is even more interesting!")
                #	with ix.searcher() as searcher:
                #		query = QueryParser("content", ix.schema).parse("Time table")
                #		results = searcher.search(query)
                #		print results
                except Exception as e:
                    print "Caught exception e at " + url
            print str(count) + " in " + thread_name + " URL:" + url


# Create new threads
a = []
a0 = 0
for i in range(1, 1000):
    th = myThread(1, "Thread-" + str(i), a0 + 1, a0 + 30)
    a.append(th)
    a0 += 30

# Start new Threads
for i in range(1, 1000 - 1):
    a[i].start()

# Add threads to thread list
threads = []
print "Appending to threads*******************************************************************************"
for i in range(1, 1000 - 1):
    threads.append(a[i])

# Wait for all threads to complete
print "Joining threads*******************************************************************************"
for i in range(1, 1000 - 1):
    a[i].join()
print "Joining of threads completed*******************************************************************************"

writer.commit()

print "Indexing Completed.........................................Exiting Main Thread"