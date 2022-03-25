from KeyValueStore import KeyValueStoreInterface

class BTreeNode:
    def __init__(self, value = None, keys = None, children = None) -> None:
        self.value = value
        self.keys = keys or []
        self.children = children or []
        self.isLeaf = False

class BTree(KeyValueStoreInterface):
    def __init__(self, value = None) -> None:
        super().__init__()
        self.root = BTreeNode(value = value)

    def put(self, key, value):
        return super().put(key, value)
    
    def get(self, key):
        curr = self.root
        while curr:
            if key in curr.keys:
                return True
            
            i = 0
            while i < len(curr.keys) and key < curr.keys[i]:
                i += 1
            if i < len(curr.keys) and key == curr.keys[i]:
                return True
            if not curr.children:
                return False
            
            curr = curr.children[i]
        return False

    def delete(self, key):
        return super().delete(key)