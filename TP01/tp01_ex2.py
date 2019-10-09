"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Sandwich au poulet à 4.90
           - Chips paprika à 2.50
           - Barre chocolat à 2.00
           - Bonbons à 3.30
           - Ice Tea à 2.20
           - Limonade à 1.90
 Résultats : - Un message confirmant ou annulant la transaction
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant un bon appétit/santé
"""

### Déclaration des variables
sandwich_poulet = float
chips_paprika = float
barre_chocolat = float
bonbons = float
ice_tea = float
limonade = float

###Initialisation des variables
sandwich_poulet : float = 4.90
chips_paprika : float = 2.50
barre_chocolat : float = 2.00
bonbons : float = 3.30
ice_tea : float = 2.20
limonade : float = 1.90

### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")

num_art = int(input("entrez numéro d'article :"))
montant = float(input("entrez votre montant :"))

# article 1
if num_art == 1:
    print("sandwich au poulet = 4.90")
    if montant < sandwich_poulet:
        print("montant incorrect")
    else:
        print("reçu", round(montant - sandwich_poulet,2))
        print("bon apettit")

# article 2
if num_art == 2:
    print("chips paprika = 2.50")
    if montant < chips_paprika:
        print("montant incorrect")
    else:
        print("reçu", round(montant - chips_paprika,2))
        print("bon apettit")

# article 3
if num_art == 3:
    print("Barre chocolatée = 2.00")
    if montant < barre_chocolat:
        print("montant incorrect")
    else:
        print("reçu", round(montant - barre_chocolat,2))
        print("bon apettit")

# article 4
if num_art == 4:
    print("bonbons = 3.30")
    if montant < bonbons:
        print("montant incorrect")
    else:
        print("reçu", round(montant - bonbons,2))
        print("bon apettit")

# article 5
if num_art == 5:
    print("ice tea = 2.20 ")
    if montant < ice_tea:
        print("montant incorrect")
    else:
        print("reçu", round(montant - ice_tea,2))
        print("bon apettit")

# article 6
if num_art == 6:
    print("limonade = 1.90 ")
    if montant < limonade:
        print("montant incorrect")
    else:
        print("reçu", round(montant - limonade,2))
        print("bon apettit")





