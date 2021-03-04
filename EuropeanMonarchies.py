import AncestralTree as at
monarchies_list = ['Kingdom of Belgium','Kingdom of Denmark','Principality of Liechtenstein','Grand Duchy of Luxembourg','Principality of Monaco','Kingdom of the Netherlands','Kingdom of Norway','Kingdom of Spain', 'Kingdom of Sweden', 'United Kingdom of Great Britain and Northern Ireland']


#Print menu
def print_menu(monarchies_list):
    print()
    print('European Hereditary Monarchies\n=========')
    for i in range(1,len(monarchies_list)+1):
        print("[{}]".format(i),monarchies_list[i-1])
    print('[0] Exit the program\n')



#Insertion of current monarch (King Philippe) Ancestors
def insertionofAncestors1():
    #Philippe of Belgium
    root = at.Node(1, "Philippe of Belgium")
    at.insert(root, at.Node(2, "Albert II of Belgium"))
    at.insert(root, at.Node(3, "Paola Ruffo di Calabria"))
    at.insert(root, at.Node(4, "Leopald III of Belgium"))
    at.insert(root, at.Node(5, "Astrid of Sweden"))
    at.insert(root, at.Node(6, "Fulco VIII, Prince Ruffo di Calabria"))
    at.insert(root, at.Node(7, "Luisa Gazelli dei Conti di Rossana e di Sebastiano"))
    at.insert(root, at.Node(8, "Albert I of Belgium"))
    at.insert(root, at.Node(9, "Elisabeth of Bavaria, Queen of Belgium"))
    at.insert(root, at.Node(10, "Prince Carl, Duke of Västergötland"))
    at.insert(root, at.Node(11, "Princess Ingeborg of Denmark"))
    at.insert(root, at.Node(12, "Fulco VII, Prince Ruffo di Calabria"))
    at.insert(root, at.Node(13, "Laura Mosselman du Chenoy"))
    at.insert(root, at.Node(14, "Augusto Gazelli dei Conti di Rossana"))
    at.insert(root, at.Node(15, "Maria dei Conti Rignon"))
    at.print_Ancenstraltree(root)


#Insertion of current monarch (Queen Margrethe II) Ancestors
def insertionofAncestors2():
    #Margrethe II
    root = at.Node(1, "Margrethe II of Denmark")
    at.insert(root, at.Node(2, "Frederik IX of Denmark"))
    at.insert(root, at.Node(3, "Ingrid of Sweden"))
    at.insert(root, at.Node(4, "Christian X of Denmark"))
    at.insert(root, at.Node(5, "Alexandrine of Mecklenburg-Schwerin"))
    at.insert(root, at.Node(6, "Gustaf VI Adolf of Sweden"))
    at.insert(root, at.Node(7, "Princess Margaret of Connaught"))
    at.insert(root, at.Node(8, "Frederik VIII of Denmark"))
    at.insert(root, at.Node(9, "Princess Louise of Sweden"))
    at.insert(root, at.Node(10, "Frederick Francis III, Grand Duke of Mecklenburg-Schwerin"))
    at.insert(root, at.Node(11, "Grand Duchess Anastasia Mikhailovna of Russia"))
    at.insert(root, at.Node(12, "Gustav V of Sweden"))
    at.insert(root, at.Node(13, "Victoria of Baden"))
    at.insert(root, at.Node(14, "Prince Arthur, Duke of Connaught and Strathearn"))
    at.insert(root, at.Node(15, "Princess Louise Margaret of Prussia"))
    at.print_Ancenstraltree(root)



#Insertion of current monarch (Hans-Adam II) Ancestors
def insertionofAncestors3():
    #Margrethe II
    root = at.Node(1, "Hans-Adam II, Prince of Liechtenstein")
    at.insert(root, at.Node(2, "Franz Joseph II, Prince of Liechtenstein"))
    at.insert(root, at.Node(3, "Countess Georgina von Wilczek"))
    at.insert(root, at.Node(4, "Prince Aloys of Liechtenstein"))
    at.insert(root, at.Node(5, "Archduchess Elisabeth Amalie of Austria"))
    at.insert(root, at.Node(6, "Count Ferdinand Maria von Wilczek"))
    at.insert(root, at.Node(7, "Countess Norbertine Kinsky von Wchinitz und Tettau"))
    at.insert(root, at.Node(8, "Prince Alfred of Liechtenstein"))
    at.insert(root, at.Node(9, "Princess Henriette Maria of Liechtenstein"))
    at.insert(root, at.Node(10, "Archduke Karl Ludwig of Austria"))
    at.insert(root, at.Node(11, "Infanta Maria Theresa of Portugal"))
    at.insert(root, at.Node(12, "Count Johann Nepomuk von Wilczek"))
    at.insert(root, at.Node(13, "Countess Elisabeth Wilhelmine Kinsky von Wchinitz und Tettau"))
    at.insert(root, at.Node(14, "Count Oktavian Zdenko Kinsky von Wchinitz und Tettau"))
    at.insert(root, at.Node(15, "Countess Georgine Ernestine Festétics de Tólna"))
    at.print_Ancenstraltree(root)


#Insertion of current monarch (Queen Elizabeth II) Ancestors
def insertionofAncestors10():
    #Elizabeth II
    root = at.Node(1, "Elizabeth II of the United Kingdom")
    at.insert(root, at.Node(2, "George VI of the United Kingdom"))
    at.insert(root, at.Node(3, "Lady Elizabeth Bowes-Lyon"))
    at.insert(root, at.Node(4, "George V of the United Kingdom"))
    at.insert(root, at.Node(5, "Princess Mary of Teck"))
    at.insert(root, at.Node(6, "Claude Bowes-Lyon, 14th Earl of Strathmore and Kinghorne"))
    at.insert(root, at.Node(7, "Cecilia Nina Cavendish-Bentick"))
    at.insert(root, at.Node(8, "Edward VII of the United Kingdom"))
    at.insert(root, at.Node(9, "Princess Alexandra of Denmark"))
    at.insert(root, at.Node(10, "Francis, Duke of Teck"))
    at.insert(root, at.Node(11, "Princess Mary Adelaide of Cambridge"))
    at.insert(root, at.Node(12, "Claude Bowes-Lyon, 13th Earl of Strathmore and Kinghorne"))
    at.insert(root, at.Node(13, "Frances Dora Smith"))
    at.insert(root, at.Node(14, "Charles Cavendish-Bentick"))
    at.insert(root, at.Node(15, "Caroline Louisa Burnaby"))
    at.print_Ancenstraltree(root)
# Loop for the program to function
while True:
    print_menu(monarchies_list)
    option = int(input("Enter the number of the monarchy that you will like to see the ancestral tree of: "))
    if option == 0:
        break
    elif option == 1:
        insertionofAncestors1()
    elif option == 2:
        insertionofAncestors2()
    elif option == 3:
        insertionofAncestors3()
    elif option == 10:
        insertionofAncestors10()
    else:
        print("Invalid option! Please Try again")
    
