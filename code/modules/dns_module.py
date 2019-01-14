import dns
from modules.module import Module
class Dns_module (Module):
    """
        properties:
        params (parent) : contain module params as a dict.
        nmap_handler : contain the portmapper.
    """
    def __init__(self, params):
        super().__init__(params)
        
        
    def run_module(self):
        def A(search: str):
            dns.resolver.query(search, 'A')
            pass
        def MX(search: str):
            dns.resolver.query(search, 'MX')
            pass
        def NS(search: str):
            dns.resolver.query(search, 'NS')
            pass
        def AAAA(search: str):
            dns.resolver.query(search, 'AAAA')
            pass
        methods = {
            'A': A,
            'MX': MX,
            'NS': NS,
            'AAAA': AAAA
        }
        dataSearch = methods.get(self.params['type'], lambda: "Invalid type Searching")(self.params['dn'])
        
        #print(str(self.params))

