def division_deux_nombres(nombre1, nombre2):
    if nombre2 == 0:
        raise ValueError("Division par zéro n'est pas autorisée.")
    resultat = nombre1 / nombre2
    return resultat

# Exemple d'utilisation de la fonction
try:
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))

    resultat = division_deux_nombres(nombre1, nombre2)
    print(f"Le résultat de la division est : {resultat}")
except ValueError as e:
    print("Erreur :", e)
except Exception as e:
    print("Une erreur est survenue :", e)
