import abc
from abc import ABC, abstractmethod
# abstract class
class Module(ABC):
    """
    properties:

    params : contain module params as a dict.
    """
    def __init__(self, params):
        self.params=params
        super().__init__()
    @abstractmethod
    def run_module(self):
        pass
    #@abstractmethod
    #def getresults(self):
    #    pass

# PoC for developers
