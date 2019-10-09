"""
Programme de calcul du prix d'un billet de cinéma selon plusieurs rabais possible.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais membre : 3chf
    Forfait famille : 1chf
    Carte mensuelle : L'entrée est gratuite

Indications :
    - Il est possible de bénéficier d'un rabais membre et étudiant en même temps
    - Il n'est pas possible de bénéficier d'un rabais famille et étudiant
    - Il est possible de bénéficier d'un rabais membre et famille
    - Il est possible d'avoir une carte mensuelle permettant
      l'accès gratuitement à ce film
    - Si une personne possède la carte membre et étudiante ainsi que le rabais famille,
      le rabais membre et étudiant s'applique (car le rabais étudiant est plus grand)

Contrainte : Si la personne possède la carte mensuelle,
             il ne faut pas lui demander d'autres informations."
"""
### Déclaration des variables
prix : int
etu : int
membre : int
famille : int
carte : int

### Initialisation des variables
prix : int = 0
etu : int = 0
membre : int = 0
famille : int = 0
carte : int = 0

### Séquence d'opération
prix = str(input("voulez vous un billet ? (prix 10 chf) :"))
etu = str(input("êtes-vous étudiant ? : (rabais 2 chf :"))
membre = str(input("êtes-vous membre ? : (rabais 3 chf) :"))
famille = str(input("souhaitez-vous un rabais famille ? (rabais 1 chf) :"))
carte = str(input("avez vous la carte mensuel ? :"))

PRIX = 10
ETU = 2
MEMBRE = 3
FAMILLE = 1
CARTE = 10

if ((prix == "oui") and (membre == "oui")) and (etu == "oui") :
    print("prix du billet :", PRIX - ETU - MEMBRE)
elif (((prix == "oui") and (etu == "oui"))and (famille == "oui")) :
    print("il n'est pas possible d'avoir un rabais famille et étudiant en même temps")
elif print
