import sys

if __name__=="__main__":
        reponse= input("voulez vous multiplier?(oui/non) ")
        print(reponse)
        if(reponse == "oui"):
                if(len(sys.argv)==3):
                        print(sys.argv)
                        x = int(sys.argv[1])
                        y =int(sys.argv[2])
                        print(mul(x,y))
                elif(len(sys.argv)==2):
                        x = int(sys.argv[1])
                        y=int(input("veuillez entree la troixieme valeur:  "))
                        print(mul(x,y))

                elif(len(sys.argv)==1):
                        x=int(input("veuillez entree la deuxieme valeur: "))
                        y=int(input("veuillez entree la troixieme valeur: "))
                        print(x*y)
                else:
                        print("erreur")
