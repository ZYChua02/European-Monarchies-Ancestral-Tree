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
        if (node.val/2 % 2 != 0): # -1 is not needed as wives are always +1 of their husbands
            child = search(root, (node.val/(2)))
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
    if (root == None): 
        return None

    else:
        maleline = search(root.left, number)  #Search male line
        femaleline = search(root.right, number) #Search female line
        return root
        
 


#Print tree in level order using queue (from geeksforgeeks.com)
def print_Ancenstraltree(root):
    #Base case (Tree is empty)
    if root == None:
        return
    queue = [] #Empty list for level order traversal
    queue.append(root) #Add in root of tree and intialise height
    
    while(len(queue) > 0):
        #Print front of queue
        if queue[0].val == 1:
            print("\nThe Current Monarch: {0}\n".format(queue[0].val2))
            print("His/Her Ancestors:")
        elif queue[0].val == 2:
            print("Father: {0}".format(queue[0].val2)) #Print Father
        elif queue[0].val == 3:
            print("Mother: {0}".format(queue[0].val2)) # Print Mother
            print("\nGrandparents: ")
        elif (queue[0].val >= 4) and (queue[0].val <= 6): #Print the first three grandparents
            print(queue[0].val2)
        elif queue[0].val == 7: #Print the last grandparent
            print(queue[0].val2)
            print("\nGreat-Grandparents:")
        else: # Print the great grandparents
            print(queue[0].val2)
        node = queue.pop(0) #Removing it from the queue
 
        #Enqueue node left child if any
        if node.left != None:
            queue.append(node.left)
 
        #Enqueue node right child if any
        if node.right != None:
            queue.append(node.right)
    





        



