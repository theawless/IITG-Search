import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import w3lib.url


class MixSpider(CrawlSpider):
    name = 'MixSpider'
    allowed_domains = ["iitg.ernet.in"]
    link_file = open(r'NewLogs/mix_links.txt', 'a+')
    all_link_file = open(r'NewLogs/all_links.txt', 'a+')
    all_link_file2 = open(r'NewLogs/something.txt', 'a+')
    start_urls = [
        "http://intranet.iitg.ernet.in",
        "http://local.iitg.ernet.in"
    ]
    rules = (Rule(LinkExtractor(allow="iitg.ernet\.in",
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
                                ),
                  follow=True,
                  # process_request='lets_see',
                  process_links='print_before_requesting',
                  callback='parse_item'
                  ),
             )

    def print_before_requesting(self, links):
        for i in range(len(links)):
            links[i].url = w3lib.url.url_query_cleaner(links[i].url)
            MixSpider.all_link_file.write(links[i].url + '\n')
        return links

    def lets_see(self, request):
        MixSpider.all_link_file2.write(request.url + '\n')
        return request

    def parse_item(self, response):
        # self.all_link_file2.write(response.request.headers.get('Referer', None) + '\n')
        MixSpider.link_file.write(response.url + '\n')
        return None
