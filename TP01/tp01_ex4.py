"""
Une compagnie d'assurance automobile propose à ses clients quatre familles
de tarifs identifiables par une couleur, du moins au plus onéreux :
    tarifs bleu, vert, orange et rouge.
Le tarif dépend de la situation du conducteur :
    - un conducteur de moins de 25 ans et titulaire du permis depuis moins
      de deux ans, se voit attribuer le tarif rouge, si toutefois
      il n'a jamais été responsable d'accident.
      Sinon, la compagnie refuse de l'assurer.
    - un conducteur de moins de 25 ans et titulaire du permis depuis
      plus de deux ans, ou de plus de 25 ans mais titulaire du permis
      depuis moins de deux ans a le droit au tarif orange s'il
      n'a jamais provoqué d'accident, au tarif rouge pour un accident,
      sinon il est refusé.
    - un conducteur de plus de 25 ans titulaire du permis depuis plus de
      deux ans bénéficie du tarif vert s'il n'est à l'origine d'aucun
      accident et du tarif orange pour un accident, du tarif rouge pour
      deux accidents, et refusé au-delà
    - De plus, pour encourager la fidélité des clients acceptés,
      la compagnie propose un contrat de la couleur immédiatement la plus
      avantageuse s'il est entré dans la maison depuis plus de cinq ans.
      Ainsi, s'il satisfait à cette exigence, un client normalement "vert"
      devient "bleu", un client normalement "orange" devient "vert",
      et le "rouge" devient "orange".

Ecrire l'algorithme permettant de saisir les données nécessaires
(sans contrôle de saisie) et de traiter ce problème.

  Données : - L'Age du conducteur
            - Le nombre d'année de permis
            - Le nombre d'accidents
            - Le nombre d'années d'assurance
  Résultats : Un message spécifiant la situation du client
"""

### Déclaration des variables

age : int
nb_annee_permis : int
nb_accident : int
nb_annee_assu : int
tarif : str
### Initialisation des variables

age : int = 0
nb_annee_permis : int = 0
nb_accident : int = 0
nb_annee_assu : int = 0

### Séquence d'opération

age = int(input("quel age avez-vous ? :"))
nb_annee_permis = int(input("depuis combien d'année avez-vous votre permis ? :"))
nb_accident = int(input("combien d'accident avez-vous eu ? :"))
nb_annee_assu = int(input("depuis combien d'année êtes-vous assuré chez nous ? :"))

if age < 25 and nb_annee_permis < 2 and nb_accident == 0 :
    tarif = "tarif rouge"
elif (age < 25 and nb_annee_permis > 2) or (age > 25 and nb_annee_permis < 2 and nb_accident == 0) :
    tarif = "tarif organge"
elif nb_accident == 1 :
    tarif = "tarif rouge"
elif age > 25 and nb_annee_permis > 2 :
    if nb_accident == 0 :
        tarif = "tarif vert"
    if nb_accident == 1 :
      tarif = "tarif orange"
    if nb_accident == 2 :
        tarif = "tarif rouge"
else:
     tarif = "refus de vous assurer"


if nb_annee_assu > 5 and tarif != "refus de vous assurer":
    if tarif == "tarif rouge" :
        tarif = "tarif orange"
    elif tarif == "tarif orange":
        tarif = "tarif vert"
    elif tarif == "tarif vert":
        tarif = "tarif bleu"

print(tarif)
