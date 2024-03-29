from tkiteasy import *
import random

LONGEUR = 600
HAUTEUR = 600
CASE = 20
AGEPROIE = 40
NBR_NAIS = 5
NBR_TOUR = 5000
CPT_TOUR = 0
ID_PROIE = 0
NBR_PROIE = {}
CASE_VIDE = []
DEPLACEMENT_LISTEX = []
DEPLACEMENT_LISTEY = []


g = ouvrirFenetre(LONGEUR,HAUTEUR)

for x in range(0,LONGEUR,CASE):
    g.dessinerLigne(x,0,x,HAUTEUR,"Gray")
for y in range (0,HAUTEUR,CASE):
    g.dessinerLigne(0,y,LONGEUR,y,"Gray")


########################## FONCTION ##########################

def POS_PROIE(CASE_VIDE):
    indice_case = random.randrange(len(CASE_VIDE))
    case = CASE_VIDE.pop(indice_case)
    return case



def DEPLACEMENT_POSSIBLE(x,y):

    if x == 0:
        DEPLACEMENT_LISTEX = [0, CASE]
    elif x == LONGEUR - CASE:
        DEPLACEMENT_LISTEX = [-CASE, 0]
    else:
        DEPLACEMENT_LISTEX = [-CASE, 0, CASE]

    if y == 0:
        DEPLACEMENT_LISTEY = [0, CASE]
    elif y == HAUTEUR - CASE:
        DEPLACEMENT_LISTEY = [-CASE, 0]
    else:
        DEPLACEMENT_LISTEY = [-CASE, 0, CASE]

    return DEPLACEMENT_LISTEX, DEPLACEMENT_LISTEY

########################## CODE ##########################

for x in range (0, LONGEUR, CASE):
    for y in range (0, HAUTEUR, CASE):
        CASE_VIDE.append([x,y])

while(CPT_TOUR < NBR_TOUR):
    CPT_TOUR += 1


    if CASE_VIDE:
        for nais_proie in range(NBR_NAIS):
            list_case_vide = POS_PROIE(CASE_VIDE)
            proieX = list_case_vide[0]
            proieY = list_case_vide[1]
            ID_PROIE = g.dessinerDisque(proieX+CASE/2,proieY+CASE/2,CASE/2,"Silver")
            NBR_PROIE[ID_PROIE] = [proieX, proieY, AGEPROIE]


    for mort_proie,info in dict(NBR_PROIE).items():
        proieX = info[0]
        proieY = info[1]
        age = info[2]

        if age == 0:
            element = NBR_PROIE.pop(mort_proie)
            element_x = element[0]
            element_y = element[1]
            CASE_VIDE.append((element_x, element_y))
            g.supprimer(mort_proie)

        elif age >= 1:
            age -= 1
            NBR_PROIE.update({mort_proie: [proieX, proieY, age]})


    for deplacement_proie,info in dict(NBR_PROIE).items():
        proieX = info[0]
        proieY = info[1]
        age = info[2]

        DEPLACEMENT_LISTEX, DEPLACEMENT_LISTEY = DEPLACEMENT_POSSIBLE(proieX,proieY)

        nouvelle_indiceX = random.randrange(len(DEPLACEMENT_LISTEX))
        nouveauX = DEPLACEMENT_LISTEX[nouvelle_indiceX]

        nouvelle_indiceY = random.randrange(len(DEPLACEMENT_LISTEY))
        nouveauY = DEPLACEMENT_LISTEY[nouvelle_indiceY]

        g.deplacer(deplacement_proie, nouveauX, nouveauY)

        NBR_PROIE.update({deplacement_proie: [proieX + nouveauX, proieY + nouveauY,age]})

########################## UTILE ##########################

    g.pause(0.2)

    touche = g.recupererTouche()

    if touche == "Return":
        for mort_proie in list(NBR_PROIE):
            info = NBR_PROIE[mort_proie]
            proieX = info[0]
            proieY = info[1]
            age = info[2]

            print(proieX,proieY,age)