#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        boucle= True
        values=[]
        while boucle:
            nb=input("LES VALEURS?!!!!!(n to stop)")
            if nb=="n":
                boucle=False
            else:
                values.append(float(nb))
    return values.sort()


def anagrams(words: list = None) -> bool:
    anagram=False
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if words is None:
        # TODO: demander les mots ici
        words1=input("La phrase1?!!!!!")
        words2=input("La phrase2??")
        rep=True
        if False not in [True if words1.count(lettres)==words2.count(lettres) else False for lettres in alphabet ]:
            anagram=True
    return anagram


def contains_doubles(items: list) -> bool:
    pas_doublons=False
    for i in range(len(items)):
        for j in range(len(items)):
            if i==j:
                pass
            elif items[i]==items[j]:
                pas_doublons= True
    return pas_doublons


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    élèves=list(student_grades.keys())
    moyenne_la_plus_grande=0
    nom=""
    for i in range(len(élèves)):
        if moyenne_la_plus_grande<(sum(student_grades[élèves[i]])%len(student_grades[élèves[i]])):
            moyenne_la_plus_grande=sum(student_grades[élèves[i]])%len(student_grades[élèves[i]])
            nom=élèves[i]
    rep={}
    rep[moyenne_la_plus_grande]=nom
    return rep


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lettres={}
    rep={}
    for i in range(26):
        if sentence.count(alphabet[i])>5:
            lettres[alphabet[i]]=sentence.count(alphabet[i])

    return sorted(lettres.items(), key=lambda x:-x[-1])

recipes={}
global recipe
def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    boucle=True
    while boucle:
        ingredients=[]
        nb=input("ingrédients (n to stop)")
        if nb=="n":
            boucle=False
        else:
            ingredients.append(nb)
        num=len(recipes)
        recipes[num]=ingredients
        
    return num
    


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    if ingredients in recipes.keys():
        return print(recipes[ingredients])
    else:
        return print("Connai pas la recette frere")


def main() -> None:
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
