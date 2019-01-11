import nmap
from modules.module import Module
class Nmap_module (Module):
    """
        properties:
        params (parent) : contain module params as a dict.
        nmap_handler : contain the portmapper.
    """
    def __init__(self, params):
        super().__init__(params)
        self.namp_handler = nmap.PortScanner()
        
    def run_module(self):
        print(str(self.params))
