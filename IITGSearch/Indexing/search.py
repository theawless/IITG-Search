# import whoosh
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.query import *
from bs4 import BeautifulSoup
import string
import sys, urllib2, urllib, os
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
        result = searcher.search(query, limit=None)
        for i in result:
            result1[j] = i['path'][1:]
            # print i
            # print i.highlights('content')
            j += 1
    return result1


def show_all_content():
    ix = open_dir("test")
    result1 = {}
    with ix.searcher() as searcher:
        j = 0
        result = searcher.search(Every('content'))
        for i in result:
            result1[j] = i['path'][1:]
            # print i.highlights('content')
            print i["path"]
            # print i["content"]
            j += 1
    return result1


def check_spelling_error(mistyped_words):
    ix = open_dir("data")
    result1 = {}
    query = QueryParser("content", ix.schema).parse(mistyped_words)
    with ix.searcher() as s:
        corrector = s.corrector("title")
        corrected = s.correct_query(query, mistyped_words)
        if corrected.query != query:
            print("Did you mean:", corrected.string)

# search1 = search("cse")
# print search1

check_spelling_error("saswota")

# show_all_content()

