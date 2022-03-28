from hashlib import sha256

def xor(fichier1, fichier2, key):
    try:
        with open(fichier1, 'rb') as fichier1:
            with open(fichier2, 'ab') as fichier2:
                i = 0
                while fichier1.peek():
                    cara = ord(fichier1.read(1))
                    j = i % len(key)
                    resultat = bytes([cara ^ key[j]])
                    i += 1
                    fichier2.write(resultat)

    except:
        print("\n----------------------------\n")
        print("ERREUR: vous avez dû entrer un chemin d'accès incorrecte.\n")

def encoder():
    print("\n----------------------------\n")
    fichier = input("Veuillez entrer le chemin d'accès du fichier que vous souhaitez encoder: \n")
    print("\n----------------------------\n")
    fichier2 = input("Veuillez entrer le chemin d'accès du fichier où vous souhaitez enregistrer le texte encodé: \n")
    print("\n----------------------------\n")
    key = input("Veuillez entrer un mot de passe (vous en aurez besoin pour décoder le fichier): \n")
    key = sha256(key.encode("utf-8")).digest()
    xor(fichier, fichier2, key)
    
def décoder():
    print("\n----------------------------\n")
    fichier = input("Veuillez entrer le chemin d'accès du fichier que vous souhaitez décoder: \n")
    print("\n----------------------------\n")
    fichier2 = input("Veuillez entrer le chemin d'accès du fichier où vous souhaitez enregistrer le texte décodé: \n")
    print("\n----------------------------\n")
    key = input('''Veuillez entrer le mot de passe (si celui que vous entrez ne correspond pas à celui utilisé pour encoder le fichier, le texte sera incompréhensible): \n''')
    key = sha256(key.encode("utf-8")).digest()
    xor(fichier, fichier2, key)
    
while True:
    print("----------------------------\n")
    print("Voulez-vous:")
    print("1 - Encoder; ")
    print("2 - Décoder;")
    print("q - Quitter.")
    print("\n----------------------------\n")
    rep = input("")
    if rep == "1":
        encoder()
    elif rep == "2":
        décoder()
    elif rep in ["q", "Q"]:
        break