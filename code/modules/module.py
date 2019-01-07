import abc
from abc import ABC, abstractmethod
# abstract class
class Module(ABC):
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
class Proof(Module):
    def run_module(self):
        print(str(self.params))

prueba = Proof("123")
prueba.run_module()
#print(str(globals()))
