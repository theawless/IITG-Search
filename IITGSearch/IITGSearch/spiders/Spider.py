import scrapy
from scrapy.http import Request
import re
import w3lib.url
import mimetypes
from urlparse import urlparse
from IITGSearch.items import IITGSearchItem
from scrapy.linkextractors import LinkExtractor


class IITGSpider_Spider(scrapy.Spider):
    name = "IITG_Spider"
    allowed_domains = ["iitg.ernet.in"]
    start_urls = [
        "http://intranet.iitg.ernet.in",
        "http://local.iitg.ernet.in"
    ]
    crawledLinks = set()
    link_file = open(r'Spi/links.txt', 'a+')
    url_file1 = open(r'Spi/all_links.txt', 'a+')
    link_extractor = LinkExtractor(allow="iitg.ernet\.in",
                                   deny=("intranet\.iitg\.ernet\.in/cclrs/",
                                         "csea\.iitg\.ernet\.in/csea/Public/web_new/index\.php/activities/",
                                         "intranet\.iitg\.ernet\.in/eventcal/",
                                         "shilloi\.iitg\.ernet\.in/~hss/reservation/",
                                         "intranet\.iitg\.ernet\.in/news/user/login\?",
                                         "local\.iitg\.ernet\.in/node/46/",
                                         "jatinga\.iitg\.ernet\.in/~dppc/",
                                         ),
                                   canonicalize=True,
                                   deny_extensions=(),
                                   )

    def parse(self, response):
        if response.status == 200:
            IITGSpider_Spider.link_file.write(response.url + "\n")

            ''' + " type: " +
                str(mimetypes.guess_extension(response.headers['content-type'])) + "\n")
            '''
            links_extracted = IITGSpider_Spider.link_extractor.extract_links(response)

            for link in links_extracted:
                link_clean = w3lib.url.url_query_cleaner(link.url)
                IITGSpider_Spider.url_file1.write(str(link_clean) + '\n')

                # If it is a proper link and is not checked yet, yield it to the Spider
                if link_clean not in IITGSpider_Spider.crawledLinks:
                    IITGSpider_Spider.crawledLinks.add(link_clean)
                    yield Request(link_clean, self.parse)
