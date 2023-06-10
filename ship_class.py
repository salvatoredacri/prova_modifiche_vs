from griglia import *
class Navi:
    def __init__(self, nome, lunghezza, coordinate=None, quantita=None): 
        """
        Inizializza un oggetto Navi con il nome, la lunghezza e le coordinate specificate.

        Argomenti:
        - nome: Il nome della nave.
        - lunghezza: La lunghezza della nave.
        - coordinate: Le coordinate occupate dalla nave. (Default: None)

        Attributi:
        - nome: Il nome della nave.
        - lunghezza: La lunghezza della nave.
        - coordinate: Le coordinate occupate dalla nave.
        - colpi: Il numero di volte che la nave è stata colpita.

        """
        self.nome = nome
        self.lunghezza = lunghezza
        self.quantita = quantita
          # Lista delle posizioni occupate dalla nave
        
        self.colpi = 0  # Numero di volte che la nave è stata colpita
        # self.affondata = False  # Indica se la nave è stata affondata 
        if coordinate is None:
         self.coordinate = []
        else:
            self.coordinate = coordinate
    
    def controlla_colpo(self, riga, colonna, griglia): 
        """
        Verifica se la nave è stata colpita in una specifica posizione.

        Argomenti:
        - riga: La riga in cui si vuole verificare il colpo.
        - colonna: La colonna in cui si vuole verificare il colpo.
        - griglia: La griglia del giocatore in cui si trova la nave.

        Valore di ritorno:
        - True se la nave è stata colpita nella posizione specificata, False altrimenti.

        """
        posizione_colpita = griglia[riga][colonna]
      
        
        if posizione_colpita == 1 and (riga, colonna) in self.coordinate:
             return True
        return False
    
    def colpita(self, riga, colonna, griglia):    
        """
        Registra un colpo sulla nave nella posizione specificata.

        Argomenti:
        - riga: La riga in cui si è verificato il colpo.
        - colonna: La colonna in cui si è verificato il colpo.
        - griglia: La griglia del giocatore in cui si trova la nave.

        Valore di ritorno:
        - True se la nave è stata colpita nella posizione specificata, False altrimenti.

        """
        
        if self.controlla_colpo(riga,colonna,griglia):
            self.coordinate.remove((riga,colonna))
            self.colpi += 1
            return True
        return False
    
    def affondata(self):  
        """
        Verifica se la nave è affondata.

        Valore di ritorno:
        - True se la nave è affondata (è stata colpita tutte le volte necessarie), False altrimenti.

        """
        
        if self.colpi == self.lunghezza:
            return True
        else:
            return False
    
    
                     




                     


