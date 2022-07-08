from itertools import permutations
def split(word):
    return [char for char in word]
def Phrases_all_combination_func(text):
    #First, we separate the given text into a list of letters (string variables)
    text_separated=split(text)
    #Now, everytime we find a ".", we create reunite the strings in between the points
    i=0
    text_separated_by_periods=[]
    while (i<len(text_separated)):
        text_separated_by_periods_aux=""
        while (text_separated[i]!="."):
            text_separated_by_periods_aux=text_separated_by_periods_aux+text_separated[i]
            i=i+1
            if i==len(text_separated):
                break
        i=i+1
        text_separated_by_periods.append(text_separated_by_periods_aux)
    text_separated_by_periods_all_permutations=permutations(text_separated_by_periods)    
    return text_separated_by_periods_all_permutations
def print_all_permutations(list_permutations):
    for i in list(list_permutations):
        print (i)
text_all_permutations=Phrases_all_combination_func("España se sitúa en el suroeste de Europa y el norte de África. En Europa, ocupa la mayor parte de la península ibérica, conocida como España peninsular, y las islas Baleares (en el mar Mediterráneo); en África se hallan las ciudades de Ceuta y Melilla, las islas Canarias (en el océano Atlántico) y varias posesiones mediterráneas denominadas «plazas de soberanía». El municipio de Llivia, en los Pirineos, constituye un exclave rodeado totalmente por territorio francés. Completa el conjunto de territorios una serie de islas e islotes frente a las propias costas peninsulares. Tiene una extensión de 505 370 km²,11​ por lo que es el cuarto país más extenso del continente,nota 2​ y con una altitud media de 650 m s. n. m. (metros sobre el nivel del mar), uno de los países más montañosos de Europa.")
print_all_permutations(text_all_permutations)
