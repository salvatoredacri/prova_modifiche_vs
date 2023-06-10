from ship_class import Navi
from griglia import *
import copy
import argparse
import sys
import platform
import os

def check_parser(args):
    try:
        check_arguments(args)
    except ValueError:
        sys.exit()


def check_arguments(args):
    if not 7 <= args.dimensione <= 20:
        print('\u001b[31mDimensione errata\033[0m')
        raise ValueError
    if not 0 <= args.portaerei <= 3:
        print('\u001b[31mNumero invalido di portaerei\033[0m')
        raise ValueError
    if not 0<= args.corazzata <= 3:
        print('\u001b[31mNumero invalido di corazzata\033[0m')
        raise ValueError
    if not 0<= args.incrociatore <=4:
        print('\u001b[31mNumero invalido di incrociatore\033[0m')
        raise ValueError
    if not 0<= args.sottomarino<= 5:
        print('\u001b[31mNumero invalido di sottomarino\033[0m')
        raise ValueError
    if not 0<= args.cacciatorpediniere <=5:
        print('\u001b[31mNumero invalido di cacciatorpediniere\033[0m')
        raise ValueError
    if not (args.modalita==0 or args.modalita==1):
        print('\u001b[31mInput invalido per "modalita". Deve essere 0 o 1\033[0m')
        raise ValueError
    
    

navi_disponibili = {
    "portaerei": Navi("portaerei", 5),
    "corazzata": Navi("corazzata", 4),
    "incrociatore": Navi("incrociatore", 3),
    "sottomarino": Navi("sottomarino", 2),
    "cacciatorpediniere": Navi("cacciatorpediniere", 1)
}

def crea_lista_navi(args, navi_disponibili):
    # Crea una copia dell'oggetto args
    args_copy = argparse.Namespace(**vars(args))
    
    lista_navi = []
    for nave in navi_disponibili.values():
        num_navi = getattr(args_copy, nave.nome)  # Ottiene il valore dell'attributo corrispondente al nome della nave
        if num_navi > 0:
            for _ in range(num_navi):
                nuova_nave = Navi(nave.nome, nave.lunghezza, quantita=1)  # Crea una nuova nave con quantita=1
                lista_navi.append(nuova_nave)  # Aggiunge la nuova nave alla lista delle navi
                num_navi -= 1  # Decrementa il valore di num_navi di 1
                setattr(args_copy, nave.nome, num_navi)  # Aggiorna il valore di num_navi nella copia di args
    
    return lista_navi


def initialize_parser(navi_disponibili):
    parser = argparse.ArgumentParser()
    for nave in navi_disponibili.values():
     parser.add_argument(f"--{nave.nome}", type=int, default=1, help=f"Numero di {nave.nome} da inserire")
    
    parser.add_argument("-g1","--giocatore_1", type=str,default='giocatore_1', help='Nome del giocatore 1')
    parser.add_argument("-g2", "--giocatore_2", type=str,default='giocatore_2', help='Nome del giocatore 2')
    parser.add_argument("-d","--dimensione", type=int, default=9, help='Dimensione della griglia')
    parser.add_argument('-m','--modalita', type=int, default=0, help='Modalità di gioco: 0 il turno di attacco si conclude solo in caso di mancato bersaglio; 1 si procede un turno alla volta ')
   
    return parser.parse_args()


def stampa_messaggio_iniziale(lista_navi):
    print("Quantità di navi selezionate:")
    navi_selezionate = set(nave.nome for nave in lista_navi)
    for nome_nave in navi_selezionate:
     quantita_nave = sum(nave.quantita for nave in lista_navi if nave.nome == nome_nave)
     print(f"{nome_nave}: {quantita_nave}")

def clear_console():
    # Controllo del sistema operativo
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:
      os.system('clear') # Unix/Linux/Mac