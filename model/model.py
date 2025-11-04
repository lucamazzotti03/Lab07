import mysql

from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        artefatti = self._artefatto_dao.get_artefatti()
        artefatti_filtrati = []
        for artefatto in artefatti:
            if artefatto.id_museo == museo and artefatto.epoca == epoca:
                artefatti_filtrati.append(artefatto)

        return artefatti_filtrati


        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO

    def get_epoche(self):
        epoche = self._museo_dao.get_epoche()
        return epoche
        """Restituisce la lista di tutte le epoche."""
        # TODO

    # --- MUSEI ---
    def get_musei(self):
        musei = self._museo_dao.get_musei()
        return musei
        """ Restituisce la lista di tutti i musei."""
        # TODO

