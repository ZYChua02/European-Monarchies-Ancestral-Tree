monarchies_list = ['Kingdom of Belgium','Kingdom of Denmark','Principality of Liechtenstein','Grand Duchy of Luxembourg','Principality of Monaco','Kingdom of the Netherlands','Kingdom of Norway','Kingdom of Spain', 'Kingdom of Sweden', 'United Kingdom of Great Britain and Northern Ireland']


#Print menu
def print_menu(monarchies_list):
    print('MAIN MENU\n=========')
    for i in range(1,len(monarchies_list)+1):
        print("[{}]".format(i),monarchies_list[i-1])
    print()
    print('[0] Exit the program')


# Loop for the program to function
while True:
    print_menu(monarchies_list)
    input = int(input("Enter the number of the monarchy that you will like to see the ancestral tree of: "))
    if input == 0:
        break
    
