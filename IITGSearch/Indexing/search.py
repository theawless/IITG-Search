# import whoosh
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.query import *
from bs4 import BeautifulSoup
import string
import sys, urllib2, urllib, os
from HTMLParser import HTMLParser
import urllib
import time
from whoosh.qparser import QueryParser
from whoosh.index import open_dir


def search(search_keyword, radio):
    start_time = time.time()
    sel = "content"
    if radio == "pdf":
        sel = "pdf"
    if radio == "image":
        sel = "image"
    if radio == "repo":
        sel = "repo"
    ix = open_dir("data/" + sel + "_data")

    final_result = dict()
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(search_keyword)
        j = 0
        result = searcher.search(query, limit=None)
        print result
        for i in result:
            final_result[j] = i['path']
            # print i
            # print i.highlights('content')
            j += 1

    suggestion = check_spelling_error(search_keyword, ix)
    end_time = time.time()

    final_result['time'] = str(end_time - start_time)
    final_result['suggestion'] = suggestion
    return final_result


def check_spelling_error(mistyped_words, ix):
    query = QueryParser("content", ix.schema).parse(mistyped_words)
    with ix.searcher() as s:
        corrector = s.corrector("title")
        corrected = s.correct_query(query, mistyped_words)
        if corrected.query != query:
            return corrected.string


def show_all_content():
    start_time = time.time()

    ix = open_dir("data/pdf_data")
    final_result = {}
    with ix.searcher() as searcher:
        j = 0
        result = searcher.search(Every('content'))
        for i in result:
            final_result[j] = i['path']
            # print i.highlights('content')
            # print i["path"]
            # print i["content"]
            j += 1
    suggestion = check_spelling_error("", ix)
    end_time = time.time()

    final_result['time'] = str(end_time - start_time)
    final_result['suggestion'] = suggestion

    return final_result


search1 = search("Institute", "pdf")
print search1
search2 = show_all_content()
print search2
# check_spelling_error("alcher")
