#import whoosh
from whoosh.index import create_in
from whoosh.fields import *
from bs4 import BeautifulSoup
from mechanize import Browser
import string
import sys,urllib2,urllib,socket,urllib3
import nltk
import threading
from HTMLParser import HTMLParser
from whoosh.qparser import QueryParser



timeout = 3
socket.setdefaulttimeout(timeout)


schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = create_in("data", schema)
writer = ix.writer()

count = 0

class myThread (threading.Thread):
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
	global count, writer, ix, schema
	current_line_number = 0
	with open('mix_links.txt') as fp:
	    for line in fp:
		# Jump at line number i and break at line number j
		current_line_number += 1
		if current_line_number<i:
			continue
		elif current_line_number>j:
			break
		count = count + 1
		url = line
		if ".pdf" not in url and ".jpg" not in url and ".doc" not in url:
			#print line
			try:
				http = urllib3.PoolManager()
				r = http.request('GET', url)
				html_content = r.data.decode('utf-8')
			#	f = urllib.urlopen(url)
			#	content1 = f.read()
			#	print content1.info()
				#print nltk.clean_html(content1)
				soup = BeautifulSoup(html_content)
				content_text = soup.get_text() 
				#print content_text
				#soup.find('title')
				#body = soup.find('h2')
				#print unicode(soup.get_text().renderContents())

				writer.add_document(title=unicode(url,"utf-8"), path=unicode("/"+url,"utf-8"),content=unicode(content_text))
				writer.add_document(title=unicode(url,"utf-8"), path=unicode("/"+url,"utf-8"),content=unicode(url))
				#writer.add_document(title=u"Second document", path=u"/b",content=u"The second one is even more interesting!")
			#	with ix.searcher() as searcher:
			#		query = QueryParser("content", ix.schema).parse("Time table")
			#		results = searcher.search(query)
			#		print results
			except Exception as e:
				print "Caught exception e"
		print str(count) + "In" + thread_name




# Create new threads
a = []
a0=0
for i in range(1,1000):
	th = myThread(1, "Thread-" + str(i), a0 + 1, a0 + 35)
	a.append(th)
	a0 += 35


#thread1 = myThread(1, "Thread-1", 1, 6000)
#thread2 = myThread(2, "Thread-2", 6000, 12000)
#thread3 = myThread(3, "Thread-3", 12000, 18000)
#thread4 = myThread(4, "Thread-4", 18000, 24000)
#thread5 = myThread(5, "Thread-5", 24000, 3000)
#thread6 = myThread(6, "Thread-6", 30000, 35000)

# Start new Threads
for i in range(1,1000):
	a[i].start()

#thread1.start()
#thread2.start()
#thread3.start()
#thread4.start()
#thread5.start()
#thread6.start()


# Add threads to thread list
for i in range(1,1000):
	threads.append(a[i])

#threads.append(thread1)
#threads.append(thread2)
#threads.append(thread3)
#threads.append(thread4)
#threads.append(thread5)
#threads.append(thread6)

# Wait for all threads to complete
for t in threads:
    t.join()

writer.commit()

print "Indexing Completed.........................................Exiting Main Thread"





