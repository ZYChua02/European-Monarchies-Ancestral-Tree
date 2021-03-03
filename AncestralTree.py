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
    #For Male Ancestors (Even Numbers) 
    elif (node.val % 2 == 0):
        #Edge case for male ancestors in the female line 
        if (((node.val)/(2)) % 2 != 0): # -1 is not needed as wives are always +1 of their husbands
            child = search(root, ((node.val)/(2)))
            child.left = insert(child.left, node)
        else:
            root.left = insert(root.left, node)
    #For Female Ancestors (Odd Numbers)
    else:
        #Edge case for female ancestors in the male line 
        if (((node.val - 1)/(2)) % 2 == 0): # -1 is needed as wives are always +1 of the husbands 
            child = search(root, ((node.val - 1)/(2)))
            child.right = insert(child.right, node)
        else:
            root.right = insert(root.right, node)
    return root

def search(root,number):
    if root == None:
        return None;
    else:
        if (root.val == number):
            return root
        elif (number % 2 == 0):
            return search(root.left, number)
        else:
            return search(root.right, number)
#def print_Ancenstraltree(tree):




        



