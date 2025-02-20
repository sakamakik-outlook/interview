"""
This DB class is not thread safe. 
How can we make this thread safe? 
"""

import logging
import time

class FakeDatabase:

    def __init__(self):
        self.value = 0
    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(2)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)