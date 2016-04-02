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
    schema = Schema(title=TEXT(analyzer=ana, spelling=True), path=ID(stored=True), content=TEXT)
    ix = create_in("data_main_thread", schema)
    writer = ix.writer()
    count = 0

    with open('mix_links.txt') as fp, open('data_main_thread/text_files/content.txt', 'w+') as f:
        for line in fp:
            count += 1
            url = line
            if ".pdf" not in url and ".jpg" not in url and ".doc" not in url and ".c" not in url and ".cpp" not in url \
                    and ".tar" not in url and "zip" not in url and ".exe" not in url and ".asm" not in url and ".JPG" \
                    not in url and ".bin" not in url and ".PDF" not in url:
                try:
                    # http = urllib3.PoolManager()
                    # r = http.request('GET', url)
                    # html_content = r.data.decode('utf-8')
                    response = urllib.urlopen(url)
                    html_content = response.read()
                    soup = BeautifulSoup(html_content)
                    content_text = soup.get_text()
                    print content_text

                    f.write(html_content)

                    writer.add_document(title=unicode(url, "utf-8"), path=unicode("/" + url, "utf-8"),
                                        content=unicode(content_text))
                    writer.add_document(title=unicode(url, "utf-8"), path=unicode("/" + url, "utf-8"),
                                        content=unicode(url))
                except Exception as e:
                    print "Caught exception e at " + url
            print str(count) + " in " + " URL:" + url
            if count == 100:
                f.close()
                break

    writer.commit()
    print "Indexing Completed.........................................Exiting Main Thread"


indexing()
