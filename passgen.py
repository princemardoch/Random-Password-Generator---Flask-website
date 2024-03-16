import string
import random

lettres_minuscule = string.ascii_lowercase
lettres_majuscules = string.ascii_uppercase
chiffres = string.digits
crt_speciaux = "!@#$%^&"

liste = []

def passgen(a,b,c,d,e):
    a = a
    b = b
    c = c
    d = d

    if a == 'True' :
        liste.append(lettres_majuscules)
    if b == 'True' :
        liste.append(lettres_minuscule)
    if c == 'True' :
        liste.append(chiffres)
    if d == 'True' :
        liste.append(crt_speciaux)

    password = ''.join(random.choice(''.join(liste)) for _ in range(e))
    liste.clear()
    
    return password
    

