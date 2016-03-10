#!/usr/bin/python3

import setlog
import threading
import time

logger = setlog.logger


class BackgroundThread(threading.Thread):
    def __init__(self, instance):

        threading.Thread.__init__(self)
        self.crawler_instance = instance

    def run(self):
        logger.debug(self.name + " run thread")
        self.callhandler()

    def callhandler(self):
        logger.debug("Inside bgcallhandler")
        for i in range(1, 100):
            self.crawler_instance.list_of_links_to_crawl.put(self.name+" "+str(i))
            print(self.name+" "+str(i))

'''
    def callhandler(self):
        logger.debug("Inside bgcallhandler")
        for i in range(1, 100):
            self.crawler_instance.list_of_links_to_crawl.put(self.name+" "+str(i))
            print(self.name+" "+str(i))
'''