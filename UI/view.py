import flet as ft
from UI.alert import AlertManager



'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK
        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        self._dropdown_musei = None
        self._dropdown_epoca = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        self._dropdown_musei = ft.Dropdown(label="Museo", hint_text="seleziona un museo per iniziare", width=400)
        self._dropdown_epoca = ft.Dropdown(label = "Epoca", hint_text="seleziona un'epoca", width=200)
        self.controller.popola_dropdown_musei()
        self.controller.popola_dropdown_epoca()


        # Sezione 3: Artefatti
        bottone_ricerca_artefatti = ft.ElevatedButton(text = "Cerca Artefatti", on_click= lambda e: self.controller.mostra_artefatti(self._dropdown_musei.value, self._dropdown_epoca.value))
        # TODO


        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),
            ft.Row(controls=[self._dropdown_musei, self._dropdown_epoca],
                   alignment = "CENTER"),
            ft.Divider(),
            bottone_ricerca_artefatti,

            # Sezione 2: Filtraggio
            # TODO

            # Sezione 3: Artefatti
            # TODO
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()



