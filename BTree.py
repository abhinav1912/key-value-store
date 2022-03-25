from KeyValueStore import KeyValueStoreInterface

class BTreeNode:
    def __init__(self, value = None, keys = None, children = None) -> None:
        self.value = value
        self.keys = keys or []
        self.children = children or []

class BTree(KeyValueStoreInterface):
    def put(self, key, value):
        return super().put(key, value)
    
    def get(self, key):
        return super().get(key)

    def delete(self, key):
        return super().delete(key)