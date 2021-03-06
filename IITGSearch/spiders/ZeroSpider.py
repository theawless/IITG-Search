import os
import scrapy
import w3lib.url
from scrapy.http import Request
import re
import urlparse
import mimetypes
from IITGSearch.items import IITGSearchItem


class ZeroSpider(scrapy.Spider):
    name = "ZeroSpider"
    allowed_domains = ["iitg.ernet.in"]
    start_urls = [
        "http://intranet.iitg.ernet.in",
        "http://local.iitg.ernet.in"
    ]

    if not os.path.exists("Links/Zero"):
        os.makedirs("Links/Zero")

    crawledLinks = set()
    link_file = open(r'Links/Zero/links.txt', 'a+')
    unaccepted_url_file = open(r'Links/Zero/unaccepted_links.txt', 'a+')
    all_url_file = open(r'Links/Zero/all_links.txt', 'a+')

    def parse(self, response):
        if response.status == 200:
            ZeroSpider.link_file.write(response.url + '\n')
            # IITGSpider.link_file.write(
            #     response.url + " type: " +
            #     str(mimetypes.guess_extension(response.headers['content-type'])) + "\n")
            links = response.xpath("//a/@href").extract()
            for link in links:
                _link = self.abs_url(link, response)
                link_clean = w3lib.url.url_query_cleaner(_link)
                ZeroSpider.all_url_file.write(str(link_clean) + '\n')

                # If it is a proper link and is not checked yet, yield it to the Spider
                if link_clean not in ZeroSpider.crawledLinks and self.desired_link(link_clean):
                    ZeroSpider.crawledLinks.add(link_clean)
                    yield Request(link_clean, self.parse)

    def abs_url(self, url, response):
        base = response.xpath('//head/base/@href').extract()
        if base:
            base = base[0]
        else:
            base = response.url
        return urlparse.urljoin(base, url)

    def desired_link(self, url):
        events = re.compile(
            ".*intranet\.iitg\.ernet\.in/cclrs/.*|.*csea\.iitg\.ernet\.in/csea/Public/web_new/index\.php/activities/.*|.*intranet\.iitg\.ernet\.in/eventcal/.*|.*shilloi\.iitg\.ernet\.in/~hss/reservation/.*|.*intranet\.iitg\.ernet\.in/news/user/login\?.*|.*local\.iitg\.ernet\.in/node/46/.*|.*jatinga\.iitg\.ernet\.in/~dppc/.*")
        if events.match(url):
            ZeroSpider.unaccepted_url_file.write("Returning False: " + url + '\n')
            return False
        return True
