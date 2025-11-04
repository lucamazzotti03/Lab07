import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO

    def popola_dropdown_musei(self):
        musei = self._model.get_musei()

        for museo in musei:
            self._view._dropdown_musei.options.append(ft.dropdown.Option(museo.nome))
        self._view.page.update()

    def popola_dropdown_epoca(self):
        epoche = self._model.get_epoche()
        for epoca in epoche:
            self._view._dropdown_epoca.options.append(ft.dropdown.Option(epoca))
        self._view.page.update()

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI

    def mostra_artefatti(self, museo, epoca):
        artefatti_filtrati = self._model.get_artefatti_filtrati(museo, epoca)
        print(artefatti_filtrati)
    # TODO
