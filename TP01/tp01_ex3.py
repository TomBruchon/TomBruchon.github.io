"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1,
              le niveau de risque est faible. Sinon il est élevé.
"""
### Déclaration des variables
age : int
sexe : str
fumeur : str
sport : str

### Initialisation des variables

age : int = 0
score : int = 0

### Séquence d'opération

age = int(input("quel age avez-vous ? :"))
sexe = str(input("êtes vous un homme ? :"))
fumeur = str(input("êtes vous fumeurs ? : "))
sport = str(input("êtes vous sportif ? :"))


if fumeur == "oui":
    print("votre niveau de risque augmente de 2 point")
    score = score + 2
if sport == "oui":
    print("votre niveau de risque diminue de 1 point")
    score = score -1
if sexe == "oui" and age > 50:
    print("votre niveau de risque augmente de 1 point")
    score = score +1
if sexe == "non" and age > 60:
    print("votre niveau de risque augmente de 1 point")
    score = score + 1

print("niveau de risque :",score)

if score <= 1:
    print("votre niveau de risque est faible")
else:
    print("votre niveau de risque est élevé")
