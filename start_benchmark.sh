#!/bin/bash
timeout 600s scrapy crawl FullSpider &
timeout 600s scrapy crawl ZeroSpider &
timeout 600s scrapy crawl SemiSpider &
