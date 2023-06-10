from griglia import  *
from ship_class import Navi
from gioco import turno, vittoria
from standards import *
import os
import time
import platform

#os.system('cls')
clear_console()

# from standards import lista_navi
print('Benvenuto')


# Assegna i valori degli argomenti alle variabili
args=initialize_parser(navi_disponibili)
lista_navi_1 = crea_lista_navi(args, navi_disponibili)
lista_navi_2 = crea_lista_navi(args, navi_disponibili)


giocatore_1 = args.giocatore_1
giocatore_2 = args.giocatore_2
dimensione = args.dimensione
modalita =args.modalita
check_parser(args)

stampa_messaggio_iniziale(lista_navi_1)
time.sleep(5)
clear_console()
#os.system('cls')




# #Creo le griglie dei due giocatori
# dimensione = int(input("Inserisci la dimensione della griglia: "))   

griglia_colpi_1= crea_griglia(dimensione)
griglia_colpi_2= crea_griglia(dimensione)
griglia_giocatore_1 = crea_griglia(dimensione)
griglia_giocatore_2 = crea_griglia(dimensione)

player=[giocatore_1, giocatore_2]



# Giocatore 1 posiziona le tue navi!
print(player[0],", è il tuo turno!" "\n Posiziona le tue navi!")
stampa_griglia(griglia_giocatore_1,dimensione)
griglia1 = posiziona_navi(griglia_giocatore_1, player[0], lista_navi_1)
print(griglia1)

clear_console()
#os.system('cls')
# Giocatore 1 ha finito di posizionare le navi. Passa al turno del Giocatore 2.
input(f"Premi INVIO e passa il computer per passare al turno di {player[1]}")
stampa_griglia(griglia_giocatore_2, dimensione)



# # Giocatore 2 posiziona le tue navi!
print(player[1],", è il tuo turno!" "\n Posiziona le tue navi!")

griglia2 = posiziona_navi(griglia_giocatore_2, player[1], lista_navi_2)
print(griglia2)

clear_console()
#os.system('cls')
# Inizia il gioco
print("""Giocatori, inizia la fase di attacco! Preparate la vostra offensiva!
         \nBuona fortuna!""")

time.sleep(7)
clear_console()
#os.system('cls')

fine_gioco = False
turno_giocatore = 0  # Indice del giocatore di turno

while not fine_gioco:
    print(f"{player[turno_giocatore]}, è il tuo turno! Attacca!")

    if turno_giocatore == 0:
        griglia_combattimento = griglia_giocatore_2
        griglia_colpi = griglia_colpi_1
        avversario = player[1]
        lista_navi_avversario = lista_navi_2

        
        
    else:
        griglia_combattimento = griglia_giocatore_1
        griglia_colpi = griglia_colpi_2
        avversario = player[0]
        lista_navi_avversario = lista_navi_1
        
        
        

    # Esegui il turno di attacco
    fine_gioco, griglia_colpi, griglia_combattimento= turno(griglia_combattimento, player[turno_giocatore], griglia_colpi, fine_gioco, lista_navi_avversario, modalita)
    

    
    # # Controlla la vittoria del giocatore
    # fine_gioco = vittoria(lista_navi_avversario)
     
    if not fine_gioco:
        input(f"Premi INVIO e passa il computer per passare al turno di {player[1-turno_giocatore]}")
        turno_giocatore = 1 - turno_giocatore
          

# # Fine del gioco, un giocatore ha vinto
#os.system('cls')
clear_console()
vincitore = player[turno_giocatore]
print(f"{vincitore} ha vinto il gioco! Complimenti!")
print("\n Grazie per aver giocato")
