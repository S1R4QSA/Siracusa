import abc
from node import Node
from abc import ABC, abstractmethod
# abstract class
class Module(ABC):
    """
    properties:

    params : contain module params as a dict.

    """
    def __init__(self, params):

        self.params={}
        for param in params:
            key,value = param.split("=")
            self.params[key]=value
        super().__init__()

    @abstractmethod
    def run_module(self):
        pass
    #@abstractmethod
    #def getresults(self):
    #    pass
    
    @abstractmethod
    def return_nodes(self):
        pass
# PoC for developers
