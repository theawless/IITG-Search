#!/usr/bin/python3

import setlog
import threading
import time

logger = setlog.logger()


class BackgroundThread(threading.Thread):
    def __init__(self, instance):
        threading.Thread.__init__(self)
        self.pluginClass = instance

    def run(self):
        logger.debug(self.name + " run thread")
        self.pluginClass.bgCallHandler()

    def stop(self):
        logger.debug(self.name + " stop thread")


'''def _callrecog(self):
    # Calls recognizer and gets the text output
    textout = recogSpeech.recog(1)
    _state = statesMod.decide_state(textout)
    return textout, _state
'''


def bgcallhandler(self):
    # Based on output by the callRecog we proceed further
    logger.debug("Inside bgcallhandler")
    if not self.thread_is_running:
        logger.debug("Thread not running")
        return
    # run async
    else:
        logger.debug("End Background Call Handler")
        return
