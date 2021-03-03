#Node implemenation
class Node:
    def __init__(self,number,name): 
        self.left = None
        self.right = None
        self.val = number
        self.val2 = name

def insert(root,node):
    #Monarch
    if root == None:
        root = node
    #For Male Ancestors (Even Numbers) (2,4,6,8)
    elif (node.val % 2 == 0):

        root.left = insert(root.left, node)
    #For Female Ancestors (Odd Numbers)
    else:
        root.right = insert(root.right, node)
    return root

   
#def print_Ancenstraltree(tree):




        



