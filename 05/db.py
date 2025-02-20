
# DB abstract class 

# methods
# 1. connect
# 2. execute_query

from abc import abstractmethod


class db_connect():
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def connect(self):
        pass




