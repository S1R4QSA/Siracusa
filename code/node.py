class Node:
    # {'ip':['192.168.1.108','10.16.48.1'], 'dn':['example.com', 'example2.com']}
    data_node: dict = {}
    # children: [Node]
    # parent: Node

    def __init__(self):
        pass

    def get(self, getters: [str]) -> dict: 
        return {k: v for k, v in self.data_node.items() if k in getters}
        
    def set(self, setters: dict) -> bool:
        for key, value in setters.items():
            if key in self.data_node:
                valToIntru = list(filter(lambda x : not x in self.data_node[key], value))
                self.data_node[key] = self.data_node[key] + valToIntru
            else:
                self.data_node[key] = value
        return True

    def to_dict(self) -> dict:
        return self.data_node

# nodea = Node()
# print (nodea.to_dict())

# nodea.set({'ip':['BLABLABLA','10.16.48.1']})

# print (nodea.to_dict())