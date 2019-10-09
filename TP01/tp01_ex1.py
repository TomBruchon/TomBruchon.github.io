"""
Programme testant si une année, saisie par l'utilisateur,est bissextile ou non
  Données : Une année saisie par l'utilisateur
  Indications:
        - Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
        - Si elle est multiple de 4, on regarde si elle est multiple de 100.
          - Si c'est le cas, on regarde si elle est multiple de 400.
            - Si c'est le cas, l'année est bissextile.
            - Sinon, elle n'est pas bissextile.
          - Sinon, elle est bissextile.
  Résultats : Un message spécifiant si l'année entrée est bissextile ou non
"""

### Déclaration des variables

annee : int

### Initialisation des variables

annee : int = 0

### Séquence d'opération

annee = int(input("saisir une annee :"))

if annee % 4 == 0:
    print("l'année est bissextile")
elif annee % 100 == 0:
    print("l'année est bissextile")
elif annee % 400 == 0:
    print("l'année est bissextile")
else:
    print("l'année n'est pas bissextile")


