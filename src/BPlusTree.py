# BPlusTree.py
# IMPLEMENT ONLY THE STRUCTURE OF B+ TREE,
# AS THIS FILE WILL BE CALLED FROM main.py  

class TreeNode:
    def __init__(self, isLeaf = False):
        self.isLeaf = isLeaf
        self.keys = []

        # INTERNAL NODE, POINTS TO CHILDREN NODES
        self.childrenNodes = []

        # LEAD NODE, POINTS TO NEXT LEAF
        self.nextLeaf = None 

    def getIfFull(self, maxKeys: int):
        if len(self.keys) >= maxKeys:
            return True
        else:
            return False
        
    def getKeyCount(self):
        return len(self.keys)

    def getIsInternal(self):
        if self.isLeaf == True:
            return False
        else:
            return True

    def addIndexKey(self, key, value):
        pass




    def setOrder(self, nodeOrder):
        self.nodeOrder = nodeOrder

    def setIsLeafTrue(self):
        self.isLeaf = True
    def setIsLeafFalse(self):
        self.isLeaf = False


    def setParentNode(self, parentNode):
        self.parent = parentNode

