#import whoosh
from whoosh.index import create_in
from whoosh.fields import *
from bs4 import BeautifulSoup
from mechanize import Browser
import string
import sys,urllib2,urllib,socket
import nltk
from HTMLParser import HTMLParser
from whoosh.qparser import QueryParser



timeout = 3
socket.setdefaulttimeout(timeout)


schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = create_in("test", schema)
writer = ix.writer()

count = 0
with open('links2.txt') as fp:
    for line in fp:
	count = count + 1
	url = line
	if ".pdf" not in url:
		print line
		try:
			f = urllib.urlopen(url)
			content1 = f.read()
			#print nltk.clean_html(content1)
			soup = BeautifulSoup(content1)
			title = soup.get_text() 
			#print title
			#soup.find('title')
			#body = soup.find('h2')
			#print unicode(soup.get_text().renderContents())

			writer.add_document(title=unicode(url,"utf-8"), path=unicode("/"+url,"utf-8"),content=unicode(title))
			#writer.add_document(title=u"Second document", path=u"/b",content=u"The second one is even more interesting!")

		#	with ix.searcher() as searcher:
		#		query = QueryParser("content", ix.schema).parse("Time table")
		#		results = searcher.search(query)
		#		print results


		except Exception as e:
			print "Caught exception e"
	print count
writer.commit()




