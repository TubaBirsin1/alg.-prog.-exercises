liste=[3,5,7,12]
def f (liste):
    if len(liste)==0:
        return 0
    return liste[0]+f(liste[1:])