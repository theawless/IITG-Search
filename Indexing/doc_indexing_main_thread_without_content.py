# import whoosh
from whoosh.index import create_in
from whoosh.fields import *
import sys
import urllib2, urllib, socket, urllib3
from whoosh.qparser import QueryParser
import re


def indexing():
    timeout = 5
    socket.setdefaulttimeout(timeout)
    ana = analysis.StemmingAnalyzer()
    schema = Schema(title=TEXT(analyzer=ana, spelling=True), path=ID(stored=True), content=TEXT,
                    data=TEXT(spelling=True, analyzer=ana, stored=True))
    ix = create_in("data/pdf_data_ without_content", schema)
    writer = ix.writer()
    count = 0

    with open('Final_Links/doc_links.txt') as fp, open('data/pdf_data/mytemp/doc_content.txt', 'w+') as f:
        for line in fp:
            count += 1
            url = line
            try:
                writer.add_document(title=unicode(url, "utf-8"), path=unicode(url, "utf-8"),
                                    content=unicode(url))
            except Exception as e:
                print "Caught exception e at " + '' + str(e)
            print str(count) + " in " + " URL:" + url

    writer.commit()
    print "Indexing Completed !"


indexing()
