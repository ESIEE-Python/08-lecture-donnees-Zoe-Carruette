"""08- Lecture de donées Zoé CARRUETTE"""
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        for line in f:
            l.append([int(x) for x in line.strip().split(';') ])
    return l

def get_list_k(data, k):
    """ prend en argument: la liste de listes retournée par read_data() 
                           et un indice k
        retourne la kième liste.
    """
    return data[k]

def get_first(l):
    """prend en argument une liste
       retourne le premier élément de cette liste
    """
    return l[0]

def get_last(l):
    """prend en argument une liste
       retourne le dernier élément de cette liste ;
    """
    n=len(l)
    return l[n-1]

def get_max(l):
    """prend en argument une liste
       retourne le maximum de cette liste ;
    """
    maxval=l[0]
    for i in l:
        maxval = max(maxval, i)
    return maxval

def get_min(l):
    """prend en argument une liste 
       retourne le minimum de cette liste ;
    """
    minval=l[0]
    for i in l:
        minval = min(minval, i)
    return minval

def get_sum(l):
    """ prend en argument une liste
        retourne la somme de cette liste.
    """
    tot=0
    for i in l:
        tot+=i
    return tot


#### Fonction principale


def main():
    """ fait appel aux fonctions pour vérifier leur bon fonctionnement.
    """
    data = read_data(FILENAME)
    print("Contenue du fichier", data)
    k_list = get_list_k(data,2)
    print("La list k:",k_list)
    print("Le premier element:", get_first(k_list))
    print("Le dernier element:", get_last(k_list))
    print("Le max:", get_max(k_list))
    print("LE min:", get_min(k_list))
    print("la somme", get_sum(k_list))
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
