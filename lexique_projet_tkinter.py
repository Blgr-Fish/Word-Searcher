from tkinter import * 
from tkinter import ttk
import csv

fichier = open("lexique140000mots.csv", encoding='ISO-8859-1')  # Banque de 65k mots de 'a' à 'h'
table_mots = list(csv.DictReader(fichier, delimiter=","))
fichier.close()

liste_lexique=[] # Creation du liste, facilitant la manipulation d'index

for i in range(len(table_mots)):
    liste_lexique.append(table_mots[i]["Word"])




def dictionnaire_startwith():
    global entree
    mot = entree.get().lower()
    liste=[]
    liste = [i for i in liste_lexique if i.startswith(mot)] # startwith() cherche toutes les valeurs commencant par celle choisie
    


    liste2 = Listbox(jeu, yscrollcommand = scrollbar.set )
    for i in range(len(liste)):
        liste2.insert(END, str(i)+'-'+str(liste[i]))
        liste2.pack(side = LEFT, fill = BOTH )
        scrollbar.config(command = liste2.yview )
    
    var_label.set(str(len(liste))+(' mot(s) commencant par ' + mot))
    

def dictionnaire_endwith():
    global entree
    mot = entree.get().lower()
    liste=[]
    liste = [i for i in liste_lexique if i.endswith(mot)] # endwith() cherche toutes les valeurs finissant par celle choisie

    liste2 = Listbox(jeu, yscrollcommand = scrollbar.set )
    for i in range(len(liste)):
        liste2.insert(END, str(i)+'-'+str(liste[i]))
        liste2.pack(side = LEFT, fill = BOTH )
        scrollbar.config(command = liste2.yview )
    
    var_label.set(str(len(liste))+(' mot(s) terminant par ' + mot))

####################################################
# Partie Tkinter    
####################################################

jeu = Tk()

cadre = Frame(jeu) # Création de l'interface
cadre.pack(padx=10, pady=10)

etiquette = Label(cadre, text='Entrez une lettre/mot :') # label d'écriture
etiquette.pack(padx=5, pady=5, side=LEFT)

entree = Entry(cadre, width=50) # ici qu'on ecrit notre lettre
entree.pack(padx=5, pady=5, side=LEFT)
entree.focus_force()

btnAffiche_startwith = Button(jeu, text='Commence par',cursor = 'hand2',relief = RAISED, command=dictionnaire_startwith) # bouton qui effectue une commande
btnAffiche_startwith.pack(fill = BOTH,padx = 5, pady=5)

btnAffiche_endwith = Button(jeu, text='Fini par',cursor = 'hand2',relief = RAISED, command=dictionnaire_endwith) # bouton qui effectue une commande
btnAffiche_endwith.pack(fill = BOTH,padx=5, pady=5)

scrollbar = Scrollbar(jeu)
scrollbar.pack( side = LEFT, fill = Y )


var_label = StringVar()     #Zone de communication avec objet TkInter/Label
label=Label(jeu,textvariable=var_label).pack() # Association Label et StringVar
var_label.set("")       #Initialisation via méthode "set" (optionnel)


jeu.mainloop() # le programme tourne non-stop

