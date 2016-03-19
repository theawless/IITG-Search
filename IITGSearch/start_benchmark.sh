#!/bin/bash
timeout 600s scrapy crawl IITG_Spider &
timeout 600s scrapy crawl MixSpider &
timeout 600s scrapy crawl IITG &
