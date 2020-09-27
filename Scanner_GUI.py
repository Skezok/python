#!/usr/bin/python3

from tkinter import *

#---------------Création de la fenêtre-------------------------

fenetre = Tk()
ip_saisi=0

#---------------Création des Fonctions-------------------------

# Définition de la fonction de récupération de l'ip
def recupere():
    ip_saisi = entree.get()
    resultat.set(ip_saisi)

#---------------Création des Frames-------------------------

# Frame du titre
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=TOP, pady=1)

# Frame pour l'ip
Frame2 = Frame(fenetre, relief=GROOVE)
Frame2.pack()

# Frame qui demande de saisir l'ip dans Frame2
Frame3 = Frame(Frame2, relief=GROOVE)
Frame3.pack(side=LEFT,)

# Frame de saisi d'ip dans Frame2
Frame4 = Frame(Frame2, borderwidth=2, relief=GROOVE)
Frame4.pack(side=RIGHT,)

# Frame de saisi du type de scan
Frame5 = Frame(fenetre, relief=GROOVE)
Frame5.pack(side=LEFT)

# Frame de confirmation
Frame6 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame6.pack(side=BOTTOM, padx=30)

# Frame d'affichage du résultat du scan
Frame7 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame7.pack(side=RIGHT, padx=2)

#---------------Ajout de contenu dans les Frames-------------------------

# Ajout de label pour Frame1/3
Label(Frame1, text="Bienvenue dans un simple scanner de port nmap").pack(padx=10, pady=10)
Label(Frame3, text="Entrez l'IP que vous voulez scanner: ").pack(padx=10, pady=10)

# Ajout du champ de saisi dans Frame4
value = StringVar() 
value.set("")
entree = Entry(Frame4, textvariable=value, width=30)
entree.pack()

# Ajout des boutons radio pour saisir le type de scan a éffectué dans Frame5
value = StringVar() 
bouton1 = Radiobutton(Frame5, text="SYN ACK Scan", variable=value, value=1)
bouton2 = Radiobutton(Frame5, text="UDP Scan", variable=value, value=2)
bouton3 = Radiobutton(Frame5, text="Complete Scan", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()

# Ajout du boutton de confirmation dans Frame6
bouton = Button(Frame6, text="Validez", command=recupere)
bouton.pack()

# Ajout du résultat du scan dans Frame7
resultat = StringVar()
label_result = Label(Frame7, textvariable=resultat)
label_result.pack()

#---------------Apparition de la fenêtre-------------------------

fenetre.mainloop()