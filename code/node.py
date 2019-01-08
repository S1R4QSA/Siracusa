from funtionsUtils import checkIP

class Node:
    data_node: dict = {'hello': 0, 'world': 1}

    def __init__(self):
        pass

    def get(self, getters: [str]) -> dict: 
        return {k: v for k, v in self.data_node.items() if k in getters}
        
    def set(self, setters: dict) -> bool:
        self.data_node = {k: v for k, v in self.data_node.items() }
        return True

    def to_dict(self) -> dict:
        return self.data_node

nodea = Node()
print (nodea.to_dict())

print (nodea.get(['world']))