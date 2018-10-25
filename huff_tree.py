

class Node():
    def __init__(self, val=None):
        self.l= None
        self.r = None
        self.val = val

class Tree():
    def __init__(self):
        self.root = Node()

    #get node located at path
    def get_node(self, path, return_val=True):
        #start with root
        node = self.root

        try:
            #work through path
            for bit in path:
                if bit == '1':
                    node = node.r
                else:
                    node = node.l 

            if return_val:
                #return value of node at end of path
                return node.val
            else:
                #return node at end of path
                return node


        #if any node is None
        except AttributeError:
            print('node not yet available')
            return -1



    #add node to tree at location specifyed by path
    def add_node(self, path, new_node):
        #start with root node
        node = self.root
        
        #work forward along path
        for bit in path[:-1]:
            if bit == 1:
                if node.r == None:
                    node.r = Node()
                node = node.r
            else:
                if node.l == None:
                    node.l = Node()
                node = node.l

        #insert new node based on last bit of the path
        if path[-1] == 1:
            node.r = new_node
        else:
            node.l = new_node

