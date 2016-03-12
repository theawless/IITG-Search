import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import re
import urlparse
from IITGSearch.items import IITGSearchItem
import IITGSearch.setlog

logger = IITGSearch.setlog.logger


class IITGSpider(scrapy.Spider):
    name = "IITG2"
    allowed_domains = ["iitg.ernet.in"]
    start_urls = [
        "http://intranet.iitg.ernet.in",
        "http://local.iitg.ernet.in"
    ]
    crawledLinks = set()

    def parse(self, response):
        if response.status == 200:
            IITGSpider.crawledLinks.add(response.url)
            logger.debug(response.url)

        hxs = HtmlXPathSelector(response)
        links = hxs.select("//a/@href").extract()

        # Pattern to check proper link
        linkPattern = re.compile(
            "^(?:ftp|http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")

        for link in links:
            # If it is a proper link and is not checked yet, yield it to the Spider
            if linkPattern.match(link) and link not in IITGSpider.crawledLinks:
                yield Request(link, self.parse)
