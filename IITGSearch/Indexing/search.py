#import whoosh
from whoosh.index import create_in
from whoosh.fields import *
from bs4 import BeautifulSoup
from mechanize import Browser
import string
import sys,urllib2,urllib,os
import nltk
from HTMLParser import HTMLParser
import urllib
from whoosh.qparser import QueryParser
from whoosh.index import open_dir


ix = open_dir("test")

with ix.searcher() as searcher:
	query = QueryParser("content", ix.schema).parse("inkulu")
	results = searcher.search(query)
	for i in results:
		print i['path']


