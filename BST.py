class Node:
    def __init__(self,key,value):
        self.__key = key
        self.__value = value
        self.__left = None
        self.__right = None

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def getKey(self):
        return self.__keys
    def getValue(self):
        return self.__value
    
    def  setLeft(self,left):
        self.__left = left
    
    def  setRight(self,right):
        self.__right
    
    def setValue(self,value):
        self.__value = value
    
    def toString(self):
        return str(self.__value)


class BST:
    def __init__(self):
        self.__root : Node =  None

    def add(self,key,value):
        temp : Node = Node(key,value) 
        if self.__root is None:
            self.__root = temp

    def search():
        pass
    def delete():
        pass
    def printInorder():
        pass   