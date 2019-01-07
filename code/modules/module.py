import abc
from abc import ABC, abstractmethod
# abstract class
class Module(ABC):
    def __init__(self, params):
        self.params=params
        super().__init__()
    @abstractmethod
    def act(self):
        pass

class Proof(Module):
    def act(self):
        print(str(self.params))

prueba = Proof("123")
prueba.act()
