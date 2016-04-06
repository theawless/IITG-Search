# import whoosh
from whoosh.index import create_in
from whoosh.fields import *
from bs4 import BeautifulSoup
import string
import sys
import urllib2, urllib, socket, urllib3

from HTMLParser import HTMLParser
from whoosh.qparser import QueryParser


def indexing():
    timeout = 3
    socket.setdefaulttimeout(timeout)
    ana = analysis.StemmingAnalyzer()
    schema = Schema(title=TEXT(analyzer=ana, spelling=True), path=ID(stored=True), content=TEXT,
                    data=TEXT(spelling=True, analyzer=ana, stored=True))
    ix = create_in("data/image_data", schema)
    writer = ix.writer()
    count = 0

    with open('Final_Links/doc_links.txt') as fp:
        for line in fp:
            count += 1
            url = line
            try:
                writer.add_document(title=unicode(url, "utf-8"), path=unicode(url, "utf-8"),
                                    content=unicode(url), data=unicode(url))
            except Exception as e:
                print "Caught exception e at " + url + "exception : " + str(e)
            print str(count) + " in " + " URL:" + url
            # if count == 100:
            #    break
    writer.commit()
    print "Indexing Completed !"


indexing()
