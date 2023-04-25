import math

def max_index(matrice):
    max_element = matrice[1][0]
    max_index = 0
    for i in range(1, len(matrice[1])):
        if matrice[1][i] > max_element:
            max_element = matrice[1][i]
            max_index = i
    return max_index

def trier_tableau(tableau):
    n = len(tableau)
    for i in range(n):
        for j in range(i+1, n):
            if tableau[j] < tableau[i]:
                tableau[i], tableau[j] = tableau[j], tableau[i]
    return tableau

# Demande à l'utilisateur d'entrer les valeurs de la variable X et les effectifs associés
x_values = input("Entrez les valeurs de la variable X séparées par des espaces : ").split()
effectif_values = input("Entrez les effectifs associés séparés par des espaces : ").split()

# Vérifie que le nombre de valeurs x correspond au nombre d'effectifs
if len(x_values) != len(effectif_values):
    print("Le nombre de valeurs X ne correspond pas au nombre d'effectifs.")
    exit(1)

# Convertit les valeurs en entiers
x_values = list(map(int, x_values))
effectif_values = list(map(int, effectif_values))

# Crée une liste de listes pour stocker les valeurs de X et les effectifs associés sous forme de matrice
M = []
M.append(x_values)
M.append(effectif_values)

# Affiche la matrice M
print("Matrice M:")
for i in range(len(M)):
    for j in range(len(M[0])):
        print(M[i][j], end="\t")
    print()

# Calcule les ECC (Effectifs Cumulés Croissants)
ecc = [0] * len(M[0])
for i in range(len(M[0])):
    ecc[i] = sum(M[1][:i+1])

# Affiche le tableau T1 des ECC
print("Tableau T1 des ECC:")
for i in range(len(M[0])):
    print(ecc[i],end="\t")
print()

# Calcule les FCC (Fréquences Cumulées Croissantes)
total_effectifs = sum(M[1])
fcc = [ecc[i] / total_effectifs for i in range(len(ecc))]

# Affiche le tableau T2 des FCC
print("Tableau T2 des FCC:")
for i in range(len(M[0])):
    print(fcc[i],end="\t")
print()

# Calcul du Mode
indice= max_index(M)
mode = M[0][indice]

# Calcul de la Moyenne
som = 0
taille=0
for element in M[1]:
    som = som + element
    taille =taille+1
moyenne = som/taille

# Tri des données pour calculer la Médiane, Q1 et Q3
Tab_Trie = trier_tableau(M[1])

# Calcul de la Médiane
if taille % 2 == 0:
    mediane = (Tab_Trie[taille//2 - 1] + Tab_Trie[taille//2]) / 2
else:
    mediane = Tab_Trie[taille//2]


# Calcul de Q1 et Q3
q1 = Tab_Trie[taille//4]
q3 = Tab_Trie[3 * taille//4]
 
# Calcul de la variance
somme_carres_ecart = sum([(x - moyenne)**2 for x in M[1]])
variance = somme_carres_ecart/taille

# Calcul de l'écart-type
ecart_type = math.sqrt(variance)

# Calcul de l'intervalle interquartile
interquartile = q3 - q1

# Calcul de l'étendue
etendue = max(M[1]) - min(M[1])

# Calcul du coefficient de variation
cv = (ecart_type / moyenne) * 100



# Affichage des résultats
print("Mode =", mode)
print("Moyenne =", moyenne)
print("Médiane =", mediane)
print("Q1 =", q1)
print("Q2 =", mediane)
print("Q3 =", q3)
print("Variance :", variance)
print("Écart-type :", ecart_type)
print("Intervalle interquartile :", interquartile)
print("Étendue :", etendue)
print("Coefficient de variation :", cv, "%")