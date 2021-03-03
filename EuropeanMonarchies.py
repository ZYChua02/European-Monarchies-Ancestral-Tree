import AncestralTree as at
monarchies_list = ['Kingdom of Belgium','Kingdom of Denmark','Principality of Liechtenstein','Grand Duchy of Luxembourg','Principality of Monaco','Kingdom of the Netherlands','Kingdom of Norway','Kingdom of Spain', 'Kingdom of Sweden', 'United Kingdom of Great Britain and Northern Ireland']


#Print menu
def print_menu(monarchies_list):
    print('European Hereditary Monarchies\n=========')
    for i in range(1,len(monarchies_list)+1):
        print("[{}]".format(i),monarchies_list[i-1])
    print()
    print('[0] Exit the program')


def test_insertion():
    #Elizabeth II
    root = at.Node(1, "Elizabeth II")
    at.insert(root, at.Node(2, "Geroge VI"))
    at.insert(root, at.Node(3, "Elizabeth Bowes-Lyon"))
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
    
