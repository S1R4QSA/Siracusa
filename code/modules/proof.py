from modules.module import Module
class Proof (Module):
    """
        properties:
        params (parent) : contain module params as a dict.
    """
    def run_module(self):
        print(str(self.params))
