import csv

def libCSV0():
    '''
    readCVS(fileName : str) -> list :
        lit le fichier CSV fileName et renvoie une listes de dictionnaires contenant les enregistrements
    
    setColType(lstDict : list , cle : str , typeOf:type) -> None :
        changer le type d'une colonne
    
    setColsTypes(lstDict : list , lstCle : list) -> None :
        changer le type de plusieurs colonnes
    
    printDictCles(dico:dict,l:int) -> None :
        Affiche les clefs du dictionnaire avec une largeur fixe égale à l
        exemple :
        >>> dict= { 'nom':'GELINET' , 'prenom':'louis')
        >>> printDictClef(dict,20)
        nom                 Prénom
        ----------------------------------------
    
    printDict(dico:dict,l:int) -> None :
       Affiche les valeurs du dictionnaire avec une largeur fixe égale à l
        exemple :
        >>> dict= { 'nom':'GELINET' , 'prenom':'louis')
        >>> printDictClef(dict,20)
        GELINET          Louis
        
    printLstDict(lstDict:dict,l:int) -> None :
        Affiche toutes les valeurs de tous les dictionnaires de la liste avec une largeur fixe égale à l
        ATTENTION : affiche TOUT le ficher, éviter avec de grandes listes de dictionnaires !
    '''

def readCSV( filename:str ) -> list :
    '''
    Entrée : le nom d'un fichier CSV (str)
    Sortie :  une listes de dictionnaires contenant les enregistrements
    '''
    with open(filename, mode = "r" , newline = '') as csvFile :
        reader = csv.DictReader(csvFile)
        lu = [dict(ligne) for ligne in reader]
    print( 'nombre d\'enregistrement lus :',len(lu) )
    return lu

def setColType(lstDict : list , cle : str , typeOf:type) -> None :
    '''
    Entrée : lstDict (liste de dictionnaire)
    cle : nom d'une clef des dictionnaires (str)
    typeOf : int, float, ou str : type dans lequel on souhaite encoder la colonne
    La fonction modifie par effet de bord la liste lstDict
    Le type d'une seule colonne est modifiée

    
    exemple :
    >>> neveux = [ {"nom" : "Riri" , "age" : "12" , "argent":"41.3"} ,
                {"nom" : "Fifi" , "age" : "15" , "argent":"21.0"} ,
                {"nom" : "Loulou" , "age" : "13" , "argent":"11.5"}]
    >>> lstTypes = { 'age' : int , 'argent' : float }
    >>> setColsTypes(neveux , 'age' , int )
    [ {"nom" : "Riri" , "age" : 12 , "argent":"41.3"} ,
                {"nom" : "Fifi" , "age" : 15 , "argent":"21.0"} ,
                {"nom" : "Loulou" , "age" : 13 , "argent":"11.5"}]
                
    # les éléments de la colonne age sont maintenant de types int.
    '''
    # précondition :
    assert typeOf in [int,float,str]
    for dico in lstDict :
        dico[cle] = typeOf(dico[cle])
     
     
def setColsTypes(lstDict : list , lstCle : list) -> None :
    '''
    Entrée : lstDict (liste de dictionnaire)
    dictCle : dictionnaire { noms de clefs:type } 
    typeOf : int, float, ou str : type dans lequel on souhaite encoder la colonne
    La fonction modifie par effet de bord la liste lstDict
    Le type des colonnes dont les noms sont des cles de lstCles sont modifiées
    
    exemple :
    >>> neveux = [ {"nom" : "Riri" , "age" : "12" , "argent":"41.3"} ,
                {"nom" : "Fifi" , "age" : "15" , "argent":"21.0"} ,
                {"nom" : "Loulou" , "age" : "13" , "argent":"11.5"}]
    >>> lstTypes = { 'age' : int , 'argent' : float }
    >>> setColsTypes(neveux , lstTypes )
    [ {"nom" : "Riri" , "age" : 12 , "argent":41.3} ,
                {"nom" : "Fifi" , "age" : 15 , "argent":21.0} ,
                {"nom" : "Loulou" , "age" : 13 , "argent":11.5}]
                
    # les éléments des colonnes age et argent sont maintenant de types int et float.
    
    '''
    # précondition :
    ok = True
    for cle in lstCle : 
        if lstCle[cle] not in [int,float,str] : ok = False
    assert ok == True

    for dico in lstDict :
        for cle in lstCle :
            dico[cle] = lstCle[cle](dico[cle])
            
def printDictCles(dico:dict,l:int) -> None :
    '''
    Procédure qui prend en paramètre un dictionnaire et un entier l
    Affiche les clefs du dictionnaire avec une largeur fixe égale à l
    affiche une ligne ---- en dessous (de la bonne largeur)

    exemple :
    >>> dict= { 'nom':'GELINET' , 'prenom':'louis')
    >>> printDictClef(dict,20)
    nom                 Prénom
    ----------------------------------------
    '''
    cles = dico.keys()
    for k in cles :
        print(format(k,str(l)),end="")
    print()
    print('-'*l*len(cles))

def printDict(dico:dict,l:int) -> None :
    '''
    Procédure qui prend en paramètre un dictionnaire et un entier l
    Affiche les valeurs du dictionnaire avec une largeur fixe égale à l
    Les valeurs sont tronquée à longueur l-1 si elle dépasse la largeur l
    
    Exemple :
    >>> dict= { 'nom':'GELINET' , 'prenom':'louis'}
    >>> printDict(dict,20)
    GELINET          Louis
    
    '''
    for e in dico :
        s = str(dico[e])
        if len(s) >= l : s=s[:l-1]
        print(format(s,str(l)),end="")
    print()

def printLstDict(lstDict:dict,l:int) -> None :
    '''
    Procédure qui prend en paramètre une liste de dictionnaires
    et 1 paramètres entier optionnel l
    Affiche toutes les valeurs de tous les dictionnaires de la liste avec une largeur fixe égale à l
    Les valeurs sont tronquée à longueur l-1 si elle dépasse la largeur l
    si la liste est vide : retourne sans rien faire
    
    ATTENTION : affiche TOUT le ficher, éviter avec de grandes listes de dictionnaires !
    '''
    if len(lstDict) == 0 : return
    printDictCles(lstDict[0],l)
    for d in lstDict :
        printDict (d,l)
    print()