#Importation de Tkinter, logiciel graphique
from tkinter import *
import tkinter.messagebox

#Création de la fenêtre de départ et de variables
click = True
tk = None

def start():
    global tk
    tk = Tk()
    tk.title("Morpion")

    #Attribution du click de souris pour jouer à 2 joueurs
    def play(button):
        global click, tk

        if button["text"] == " " and click:
            button["text"] = "X"
            click = False
        elif button["text"] == " ":
            button["text"] = "O"
            click = True
        #Nouvelles variables et conditions de victoire
        X_win = None
        O_win = None
        if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
            X_win = True

        if button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
            O_win = True
        
        #En cas de victoire         
        if X_win == True:
            answer = tkinter.messagebox.askquestion('Le joueur X a gagné', 'Veux-tu jouer a nouveau ? ')
            tk.destroy()
            if answer == 'yes': start()
        elif O_win == True:
            answer = tkinter.messagebox.askquestion('Le joueur O a gagné', 'Veux-tu jouer a nouveau ? ')
            tk.destroy()
            if answer == 'yes': start()
        #En cas d'égalité     
        elif X_win == False and O_Win == False:                                      
            answer = tkinter.messagebox.askquestion('Egalité ', 'Veux-tu joeur a nouveau ? ') 
            tk.destroy()
            if answer == 'yes': start()


    #Création et paramètre de la grille 
    button1 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button1))
    button1.grid(row=1, column=0, sticky=S+N+E+W)

    button2 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button2))
    button2.grid(row=1, column=1, sticky=S+N+E+W)

    button3 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button3))
    button3.grid(row=1, column=2, sticky=S+N+E+W)

    button4 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button4))
    button4.grid(row=2, column=0, sticky=S+N+E+W)

    button5 = Button(tk, text=" ", font=("Times 26 bold"), height=4, width=8, command=lambda:play(button5))
    button5.grid(row=2, column=1, sticky=S+N+E+W)

    button6 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button6))
    button6.grid(row=2, column=2, sticky=S+N+E+W)

    button7 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button7))
    button7.grid(row=3, column=0, sticky=S+N+E+W)

    button8 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button8))
    button8.grid(row=3, column=1, sticky=S+N+E+W)

    button9 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button9))
    button9.grid(row=3, column=2, sticky=S+N+E+W)

    tk.mainloop()
start()


#Anticipation des coups gagnants 
def position_gagnante(button):
    if (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == " " ):
        return button3
    if (button1["text"] == "O" and button2["text"] == " " and button3["text"] == "O" ):
        return button2
    if (button1["text"] == " " and button2["text"] == "O" and button3["text"] == "O"):
        return button1
    if (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == " " ):
        return button6
    if (button4["text"] == "O" and button5["text"] == " " and button6["text"] == "O"):
        return button5
    if (button4["text"] == " " and button5["text"] == "O" and button6["text"] == "O" ):
        return button4
    if (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == " "):
        return button9
    if (button7["text"] == "O" and button8["text"] == " " and button9["text"] == "O"):
        return button8
    if (button7["text"] == " " and button8["text"] == "O" and button9["text"] == "O" ):
        return button7
    if (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == " " ):
        return button7
    if (button1["text"] == "O" and button4["text"] == " " and button7["text"] == "O"  ):
        return button4
    if (button1["text"] == " " and button4["text"] == "O" and button7["text"] == "O" ):
        return button1
    if (button2["text"] == "O" and button5["text"] == "O" and button8["text"] == " " ):
        return button8
    if (button2["text"] == "O" and button5["text"] == " " and button8["text"] == "O"  ):
        return button5
    if (button2["text"] == " " and button5["text"] == "O" and button8["text"] == "O"  ):
        return button2
    if (button3["text"] == "O" and button6["text"] == "O" and button9["text"] == " " ):
        return button9
    if (button3["text"] == "O" and button6["text"] == " " and button9["text"] == "O"):
        return button6
    if (button3["text"] == " " and button6["text"] == "O" and button9["text"] == "O" ):
        return button3
    if (button3["text"] == "O" and button5["text"] == "O" and button7["text"] == " " ):
        return button7
    if (button3["text"] == "O" and button5["text"] == " " and button7["text"] == "O"  ):
        return button5
    if (button3["text"] == " " and button5["text"] == "O" and button7["text"] == "O" ):
        return button3
    if (button1["text"] == "O" and button5["text"] == "O" and button9["text"] == " " ):
        return button9
    if (button1["text"] == "O" and button5["text"] == " " and button9["text"] == "O" ):
        return button5
    if (button1["text"] == " " and button5["text"] == "O" and button9["text"] == "O" ):
        return button1
    return

#IA
def jeu_ordi():
    #Elle vérifie qu'elle ne peut pas gagner au prochain coup
    coup_ordi = position_gagnante(button)
    if coup_ordi == 0:
        #Elle vérifie que le joueur n'est pas en position de gagner
        coup_ordi = position_gagnante(pion_joueur)
        if coup_ordi == 0:
            #Elle lui reste à voir si le centre est encore libre
            if button5["text"] == " ":
                coup_ordi = click
            #Sinon elle joue un coup aléatoire
            else :
                coup_ordi = click
    return


