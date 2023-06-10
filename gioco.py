from griglia import *
import os
import time

def turno(griglia_combattimento, giocatore, griglia_colpi, fine_gioco, lista_navi,modalita): 
    
    """
    Esegue un turno di gioco per il giocatore corrente.

    Argomenti:
    - griglia_combattimento: la griglia di gioco del giocatore avversario
    - giocatore: il nome del giocatore corrente
    - griglia_colpi: la griglia dei colpi effettuati dal giocatore corrente
    - fine_gioco: flag che indica se il gioco è terminato
    - lista_navi: la lista delle navi in gioco
    - modalita: la modalità di gioco (0 o 1)

    Ritorno:
    - fine_gioco: flag che indica se il gioco è terminato
    - griglia_colpi: la griglia dei colpi effettuati dal giocatore corrente
    - griglia_combattimento: la griglia di gioco del giocatore avversario
    

    """
    fine_turno = False
    

    while not fine_turno:
        os.system('cls')
        print(giocatore, "Ecco la tua griglia dei colpi effettuati")
        stampa_griglia(griglia_colpi, len(griglia_colpi))
        print(giocatore, "inserisci le coordinate dove vuoi sparare")

        try:
         colonna = input("Inserisci la lettera della colonna in cui vuoi sparare (es.A): ")
         colonna = colonna.upper()
         if colonna not in string.ascii_uppercase[:len(griglia_combattimento)]:
            print("Lettera non valida. Inserisci una lettera da A a", string.ascii_uppercase[:len(griglia_combattimento)])
            time.sleep(3)
            continue
        except ValueError:
         print("Inserisci una lettera valido")
         time.sleep(3) 
         continue

        try:
         riga = int(input("Inserisci il numero della riga in cui vuoi sparare (es.1): ")) - 1
         if riga < 0 or riga > len(griglia_combattimento):
            print(f"Numero non valido. Inserisci nemero valido, da 1 a {len(griglia_combattimento)}")
            time.sleep(3)
            continue
        except ValueError:
         print('Inserisci un numero valido') 
         time.spleep(3)
         continue
    
      
        colonna = string.ascii_uppercase.index(colonna)  # Converte la lettera in indice
   

        if griglia_colpi[riga][colonna] != 0:
            print("Hai già sparato in questa posizione. Riprova.")
            time.sleep(3)
            continue

        colpo = False
        
        for nave in lista_navi:
            if nave.controlla_colpo(riga, colonna,griglia_combattimento):
                print("Hai colpito una nave!")
                colpo = True
                griglia_colpi[riga][colonna] = "c"
                nave.colpita(riga,colonna,griglia_combattimento)
                if nave.affondata():
                    print("Hai affondato una nave!",nave.nome)
                    if all(n.affondata() for n in lista_navi):
                        fine_gioco = vittoria(lista_navi)  # Tutte le navi sono affondate, fine del gioco
                        break

       
        if colpo and modalita == 0:
             
              print("\nGriglia dei colpi:")
              stampa_griglia(griglia_colpi, len(griglia_colpi))
              print('Puoi sparare ancora!')
              time.sleep(4)

        elif not colpo and modalita == 0:
              print("Hai sparato in acqua.")
              griglia_colpi[riga][colonna] = "-"
              fine_turno = True
        else:
            if not colpo and modalita == 1:
             print("Hai sparato in acqua.")
             griglia_colpi[riga][colonna] = "-"
             fine_turno = True
            elif colpo and modalita == 1:
               fine_turno = True
      
        if fine_gioco:
            break
        
        
        print("\nGriglia dei colpi:")
        stampa_griglia(griglia_colpi, len(griglia_colpi))

    return fine_gioco, griglia_colpi, griglia_combattimento

def vittoria(lista_navi): 
    """
    Determina se tutte le navi nella lista sono state affondate.

    Argomenti:
    - lista_navi: Una lista delle navi nel gioco.

    Valore di ritorno:
    - True se tutte le navi sono state affondate, False altrimenti.
    """
    for nave in lista_navi:
        if not nave.affondata():
            return False
    return True








           
