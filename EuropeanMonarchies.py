import AncestralTree as at
monarchies_list = ['Kingdom of Belgium','Kingdom of Denmark','Principality of Liechtenstein','Grand Duchy of Luxembourg','Principality of Monaco','Kingdom of the Netherlands','Kingdom of Norway','Kingdom of Spain', 'Kingdom of Sweden', 'United Kingdom of Great Britain and Northern Ireland']


#Print menu
def print_menu(monarchies_list):
    print()
    print('European Hereditary Monarchies\n=========')
    for i in range(1,len(monarchies_list)+1):
        print("[{}]".format(i),monarchies_list[i-1])
    print('[0] Exit the program\n')

#Insertion of current monarch (Queen Elizabeth II) Ancestors
def insertionofAncestors10():
    #Elizabeth II
    root = at.Node(1, "Queen Elizabeth II")
    at.insert(root, at.Node(2, "King George VI"))
    at.insert(root, at.Node(3, "Queen Elizabeth Bowes-Lyon"))
    at.insert(root, at.Node(4, "King George V"))
    at.insert(root, at.Node(5, "Queen Mary"))
    at.insert(root, at.Node(6, "Claude Bowes-Lyon"))
    at.insert(root, at.Node(7, "Cecilia Bowes-Lyon"))
    at.print_Ancenstraltree(root)
# Loop for the program to function
while True:
    print_menu(monarchies_list)
    option = int(input("Enter the number of the monarchy that you will like to see the ancestral tree of: "))
    if option == 0:
        break
    elif option == 10:
        test_insertion()
    else:
        print("Invalid option! Please Try again")
    
