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
    #King Philippe of Belgium
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
    #Queen Margrethe II
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



#Insertion of current monarch (Prince Hans-Adam II) Ancestors
def insertionofAncestors3():
    #Prince Hans-Adam II
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


#Insertion of current monarch (Grand Duke Henri) Ancestors
def insertionofAncestors4():
    #Grand Duke Henri
    root = at.Node(1, "Henri, Grand Duke of Luxembourg")
    at.insert(root, at.Node(2, "Jean, Grand Duke of Luxembourg"))
    at.insert(root, at.Node(3, "Princess Joséphine Charlotte of Belgium"))
    at.insert(root, at.Node(4, "Prince Felix of Bourbon-Parma"))
    at.insert(root, at.Node(5, "Charlotte, Grand Duchess of Luxembourg"))
    at.insert(root, at.Node(6, "Leopold III of Belgium"))
    at.insert(root, at.Node(7, "Astrid of Sweden"))
    at.insert(root, at.Node(8, "Robert I, Duke of Parma"))
    at.insert(root, at.Node(9, "Infanta Maria Antonia of Portugal"))
    at.insert(root, at.Node(10, "William IV, Grand Duke of Luxembourg"))
    at.insert(root, at.Node(11, "Infanta Marie Anne of Portugal"))
    at.insert(root, at.Node(12, "Albert I of Belgium"))
    at.insert(root, at.Node(13, "Elisabeth of Bavaria, Queen of Belgium"))
    at.insert(root, at.Node(14, "Prince Carl, Duke of Västergötland"))
    at.insert(root, at.Node(15, "Princess Ingeborg of Denmark"))
    at.print_Ancenstraltree(root)


#Insertion of current monarch (Prince Albert II) Ancestors
def insertionofAncestors5():
    #Prince Albert II
    root = at.Node(1, "Albert II, Prince of Monaco")
    at.insert(root, at.Node(2, "Rainier III, Prince of Monaco"))
    at.insert(root, at.Node(3, "Grace Kelly"))
    at.insert(root, at.Node(4, "Prince Pierre of Monaco, Count of Polignac"))
    at.insert(root, at.Node(5, "Princess Charlotte, Duchess of Valentinois"))
    at.insert(root, at.Node(6, "John B. Kelly Sr."))
    at.insert(root, at.Node(7, "Margaret Katherine Majer"))
    at.insert(root, at.Node(8, "Count Maxence of Polignac"))
    at.insert(root, at.Node(9, "Susana Mariana de la Torre y Mier"))
    at.insert(root, at.Node(10, "Louis II, Prince of Monaco"))
    at.insert(root, at.Node(11, "Marie Juliette Louvet"))
    at.insert(root, at.Node(12, "John Henry Kelly"))
    at.insert(root, at.Node(13, "Mary Anne Costello"))
    at.insert(root, at.Node(14, "Carl Majer"))
    at.insert(root, at.Node(15, "Margaretha Berg"))
    at.print_Ancenstraltree(root)

#Insertion of current monarch (King Willem-Alexander) Ancestors
def insertionofAncestors6():
    #King Willem-Alexander
    root = at.Node(1, "Willem-Alexander of the Netherlands")
    at.insert(root, at.Node(2, "Jonkheer Claus von Amsberg"))
    at.insert(root, at.Node(3, "Beatrix of the Netherlands"))
    at.insert(root, at.Node(4, "Claus Felix von Amsberg"))
    at.insert(root, at.Node(5, "Baroness Gösta von dem Bussche-Haddenhausen"))
    at.insert(root, at.Node(6, "Prince Bernhard of Lippe-Biesterfeld"))
    at.insert(root, at.Node(7, "Juliana of the Netherlands"))
    at.insert(root, at.Node(8, "Wilhelm von Amsberg"))
    at.insert(root, at.Node(9, "Elise von Vieregge"))
    at.insert(root, at.Node(10, "Baron Georg von dem Bussche-Haddenhausen"))
    at.insert(root, at.Node(11, "Baroness Gabriele von dem Bussche-Ippenburg"))
    at.insert(root, at.Node(12, "Prince Bernhard of Lippe"))
    at.insert(root, at.Node(13, "Baroness Armgard von Cramm"))
    at.insert(root, at.Node(14, "Duke Henry of Mecklenburg-Schwerin"))
    at.insert(root, at.Node(15, "Wilhelmina of the Netherlands"))
    at.print_Ancenstraltree(root)


#Insertion of current monarch (King Harald V) Ancestors
def insertionofAncestors7():
    #King Harald V
    root = at.Node(1, "Harald V of Norway")
    at.insert(root, at.Node(2, "Olav V of Norway"))
    at.insert(root, at.Node(3, "Princess Märtha of Sweden"))
    at.insert(root, at.Node(4, "Haakon VII of Norway"))
    at.insert(root, at.Node(5, "Princess Maud of Wales"))
    at.insert(root, at.Node(6, "Prince Carl, Duke of Västergötland"))
    at.insert(root, at.Node(7, "Princess Ingeborg of Denmark"))
    at.insert(root, at.Node(8, "Frederick VIII of Denmark"))
    at.insert(root, at.Node(9, "Elise von Vieregge"))
    at.insert(root, at.Node(10, "Edward VII of the United Kingdom"))
    at.insert(root, at.Node(11, "Princess Alexandra of Denmark"))
    at.insert(root, at.Node(12, "Princess Sophia of Nassau"))
    at.insert(root, at.Node(13, "Baroness Armgard von Cramm"))
    at.insert(root, at.Node(14, "Frederick VIII of Denmark"))
    at.insert(root, at.Node(15, "Princess Louise of Sweden and Norway"))
    at.print_Ancenstraltree(root)



#Insertion of current monarch (King Felipe VI) Ancestors
def insertionofAncestors8():
    #King Felipe VI
    root = at.Node(1, "Felipe VI of Spain")
    at.insert(root, at.Node(2, "Juan Carlos I of Spain"))
    at.insert(root, at.Node(3, "Princess Sophia of Greece and Denmark"))
    at.insert(root, at.Node(4, "Infante Juan, Count of Barcelona"))
    at.insert(root, at.Node(5, "Princess María de las Mercedes of Bourbon-Two Sicilies"))
    at.insert(root, at.Node(6, "Paul of Greece"))
    at.insert(root, at.Node(7, "Princess Frederica of Hanover"))
    at.insert(root, at.Node(8, "Alfonso XIII of Spain"))
    at.insert(root, at.Node(9, "Princess Victoria Eugenie of Battenberg"))
    at.insert(root, at.Node(10, "Prince Carlos of Bourbon-Two Sicilies"))
    at.insert(root, at.Node(11, "Princess Louise of Orléans"))
    at.insert(root, at.Node(12, "Constantine I of Greece"))
    at.insert(root, at.Node(13, "Princess Sophia of Prussia"))
    at.insert(root, at.Node(14, "Ernest Augustus, Duke of Brunswick"))
    at.insert(root, at.Node(15, "Princess Victoria Louise of Prussia"))
    at.print_Ancenstraltree(root)

#Insertion of current monarch (King Carl XVI Gustaf) Ancestors
def insertionofAncestors9():
    #King Carl XVI Gustaf
    root = at.Node(1, "Carl XVI Gustaf of Sweden")
    at.insert(root, at.Node(2, "Prince Gustaf Adolf, Duke of Västerbotten"))
    at.insert(root, at.Node(3, "Princess Sibylla of Saxe-Coburg and Gotha"))
    at.insert(root, at.Node(4, "Gustaf VI Adolf of Sweden"))
    at.insert(root, at.Node(5, "Princess Margaret of Connaught"))
    at.insert(root, at.Node(6, "Charles Edward, Duke of Saxe-Coburg and Gotha"))
    at.insert(root, at.Node(7, "Princess Victoria Adelaide of Schleswig-Holstein-Sonderburg-Glücksburg"))
    at.insert(root, at.Node(8, "Gustaf V of Sweden"))
    at.insert(root, at.Node(9, "Princess Victoria of Baden"))
    at.insert(root, at.Node(10, "Prince Arthur, Duke of Connaught and Strathearn"))
    at.insert(root, at.Node(11, "Princess Louise Margaret of Prussia"))
    at.insert(root, at.Node(12, "Prince Leopold, Duke of Albany"))
    at.insert(root, at.Node(13, "Princess Helena of Waldeck and Pyrmont"))
    at.insert(root, at.Node(14, "Friedrich Ferdinand, Duke of Schleswig-Holstein"))
    at.insert(root, at.Node(15, "Princess Karoline Mathilde of Schleswig-Holstein-Sonderburg-Augustenburg"))
    at.print_Ancenstraltree(root)

#Insertion of current monarch (Queen Elizabeth II) Ancestors
def insertionofAncestors10():
    #Queen Elizabeth II
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
    elif option == 4:
        insertionofAncestors4()
    elif option == 5:
        insertionofAncestors5()
    elif option == 6:
        insertionofAncestors6()
    elif option == 7:
        insertionofAncestors7()
    elif option == 8:
        insertionofAncestors8()
    elif option == 9:
        insertionofAncestors9()
    elif option == 10:
        insertionofAncestors10()
    else:
        print("Invalid option! Please Try again")
    
