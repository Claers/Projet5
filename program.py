from DataBaseOperations import DataBase

class App():

    def __init__(self):
        self.running = False
        self.db = DataBase("OpenFoodUser", "OpenPass",
                           "OpenFoodDB", "localhost")

        self.choice = 0

        self.categorylistmem = ""
        self.productlistmem = ""
        self.categorychoice = 0
        self.productchoice = 0
        self.categoryfound = False
        self.productfound = False

        self.productsubstitute = ""

        self.favoritechoice = 0
        self.favoritemem = ''
        self.favoritefound = False

    def LaunchApp(self):
        self.running = True
        self.AppLoop()

    def AppLoop(self):
        # Main loop of the app
        while(self.running):
            # Main menu
            if(self.choice == 0):
                self.choice = int(input(
                    "\n1 - Quel aliment souhaitez vous remplacer ? \n2 - Retrouver mes aliments substitués\n3 - Quitter le programme \n\nVotre Choix (1,2 ou 3):"))
                print("\n")
            # Replace a product by finding a substitute
            elif(self.choice == 1):
                if(self.categorychoice == 0):
                    if(self.categorylistmem == ""):  # If the category list registred in memory is empty use the categorylist command
                        self.categorylistmem = self.db.categorylist()
                    if(self.categorylistmem == "Error"):
                        print("Une Erreur dans le programme a été rencontrée")
                        self.choice = 3
                    else:
                        self.categorychoice = int(input(
                            "\nVeuillez choisir une catégorie dans la liste précédente et entrez ici le chiffre correspondant (Entrez -1 pour affiner votre recherche) : "))
                elif(self.categorychoice != -1):
                    if(self.productchoice == 0):
                        for category in self.categorylistmem:
                            if(self.categorychoice == category['categoryid']): # If the category id enter by the user is in the list and exist
                                self.productlistmem = self.db.product_category(self.categorychoice)
                                self.categoryfound = True
                                self.productchoice = int(input("\nVeillez choisir un produit dans la liste précédente et entrez ici le chiffre correspondant : "))
                        if(self.categoryfound == False): # If the category id enter by the user is not the list
                            print("\nLe chiffre entré ne correspond à aucune des catégories. Merci d'entrer un nouveau chiffre.")
                            self.categorychoice = int(input(
                            "\nVeuillez choisir une catégorie dans la liste précédente et entrez ici le chiffre correspondant : "))
                    else:
                        if(self.productfound == False):
                            for product in self.productlistmem:
                                if(self.productchoice == product['productid']): # If the product id enter by the user is in the list and exist
                                    self.productfound = True
                            if(self.productfound == False): # If the product id enter by the user is not the list
                                print("\nLe chiffre entré ne correspond à aucun des produits. Merci d'entrer un nouveau chiffre.")
                                self.productchoice = int(input("\nVeillez choisir un produit dans la liste précédente et entrez ici le chiffre correspondant : "))
                        else:
                            self.productsubstitute = self.db.substitute(self.categorychoice, self.productchoice)
                            if(self.productsubstitute == "Best"): # If the substitute found is already the product selected
                                print("Ce produit est déja le meilleur de sa catégorie. Souhaitez vous enregistrer ce produit dans vos favoris ?")
                                self.productsubstitute = self.productchoice
                                register = int(input("1 - Oui / 2 - Non : "))
                                if(register == 1):
                                    self.db.add_favorite(self.productchoice,self.productchoice)
                                    print("Produit enregistré, retour au menu")
                                    self.AppReset()
                                elif(register ==2):
                                    print("Produit non enregistré, retour au menu")
                                    self.AppReset()
                                else:
                                    print("Choix Incorrect")
                                    register = 0
                            else: # If the substitute found is not the same product
                                print("\nVoulez vous enregistrer ce substitut dans vos favoris ?\n")
                                register = int(input("1 - Oui / 2 - Non : "))
                                if(register == 1):
                                    self.db.add_favorite(self.productsubstitute['productid'],self.productchoice)
                                    print("Produit enregistré, retour au menu")
                                    self.AppReset()
                                elif(register ==2):
                                    print("Produit non enregistré, retour au menu")
                                    self.AppReset()
                                else:
                                    print("Choix Incorrect")
                                    register = 0
                else: # If the user type -1 in the category choice, he can make a search by word 
                    categorysearch =  str(input("\nEntrez le nom d'une catégorie ou entourez un mot-clé avec \%\"mot-clé\"\% : "))
                    self.db.category(categorysearch)
                    self.categorychoice = 0 


            # Show the list of favorites
            elif(self.choice == 2):
                if(self.favoritemem == ""):  # If the favorite list registred in memory is empty use the show_favorite command
                    self.favoritemem = self.db.show_favorites()
                if (self.favoritechoice == 0):
                    self.favoritechoice = int(input("Veuillez choisir un favori dans la liste précédente et entrez ici le chiffre correspondant (-1 pour passer en mode supprimer) : "))
                elif (self.favoritechoice != -1):
                    if(self.favoritefound == False):
                        for favorite in self.favoritemem:
                            if (self.favoritechoice == favorite['favoriteid']):
                                self.favoritefound = True
                        if (self.favoritefound == False):
                            print("\n Le chiffre entré ne correspond à aucun des favoris. Merci d'entrer un nouveau chiffre")
                            self.favoritechoice = 0
                    else:
                        print("\n Substitut : \n")
                        self.db.product(self.favoritemem[self.favoritechoice-1]['favorite']) 
                        print("\n Produit substitué : \n")
                        self.db.product(self.favoritemem[self.favoritechoice-1]['productsubid']) 
                else: # If the user type -1 in the favorite choice, the program enter in the delete mode 
                    delfav = int(input("\n ATTENTION MODE SUPPRIMER ACTIVÉ. Veuillez choisir un favori dans la liste precedente pour le supprimer des favoris. Attention cette action est irréversible : "))
                    delfound = False
                    for favorite in self.favoritemem:
                            if (delfav == favorite['favoriteid']):
                                delfound = True
                    if (delfound == False):
                        print("\n Le chiffre entré ne correspond à aucun des favoris. Merci d'entrer un nouveau chiffre")
                    else:
                        self.db.remove_favorite(delfav)
                        print("\nFavori n°" + str(delfav)+ " supprimé. Retour en mode normal")
                        self.favoritechoice = 0
                        self.favoritemem = ""


            # Quit the programm
            elif(self.choice == 3):
                print("\nAu revoir")
                self.CloseApp()

            elif(self.choice > 3):
                print("Choix incorrect\n")
                self.choice = 0



    # A class to reset the app variable
    def AppReset(self):
        self.choice = 0
        self.categorychoice = 0
        self.productchoice = 0
        self.categorylistmem = ""
        self.favoritemem = ""
        self.favoritechoice = 0
        self.categoryfound = False
        self.productfound = False
        self.favoritefound = False


    def CloseApp(self):
        self.running = False
        self.db.close()


if __name__ == '__main__':
    Application = App()
    Application.LaunchApp()
