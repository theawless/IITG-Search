# import whoosh
from whoosh.index import create_in
from whoosh.fields import *
from bs4 import BeautifulSoup
from mechanize import Browser
import string
import sys, urllib2, urllib, os
import nltk
from HTMLParser import HTMLParser
import urllib
from whoosh.qparser import QueryParser
from whoosh.index import open_dir


def search(search_keyword):
    ix = open_dir("data")
    result1 = {}
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(search_keyword)
        j = 0
        result = searcher.search(query)
        for i in result:
            result1[j] = i['path'][1:]
            j += 1
    return result1


#search1 = search("saswata")

#print search1
