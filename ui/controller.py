from model.model import Model
from ui.view import View
import flet as ft

# Classe che implementa il Controller del pattern MVC

class Controller:
    def __init__(self, model : Model, view : View):
        self._model = model
        self._view = view
        self._num_stars = None

    # Event handler della casella dropdown
    def  handler_dropdown_change(self, e):
        print("handler_dropdown_change()")
        # Tengo traccia del numero di star impostato dall'utente

        # Se già impostato, aggiorno il contento della ListView,
        # anche senza che sia premuto il pulsante dedicato

        if self._num_stars is None:
            self._num_stars = self._view._dd_stars.value
        else:
            self.handler_btn_businesses_with_stars(None)

    # Event handler del primo pulsante
    def  handler_btn_businesses_with_stars(self, e):
        print("handler_btn_businesses_with_stars()")
        if self._view._dd_stars.value is None:
            self._view.show_alert("You need to select stars first!")
        else:
            # Leggo i business dal Model e li aggiungo alla ListView

            # Posso leggere solo quelli il cul numero di star è maggiore o uguale al valore impostato
            # dall'utente con la casella dropdown (il filtraggio avviene nel DAO con SELECT ... WHERE

            #businesses = self._model.get_businesses_with_stars(self._view._dd_stars.value)

            # Oppure posso leggere tutte le righe del database, una volta sola, quando non
            # ancora fatto, e di li in avanti usare la struttura dati costruita, es. filtrandola con if

            businesses = self._model.get_all_businesses()
            self._view._lst_results.clean()
            for business in businesses:
                if business.stars>=int(self._view._dd_stars.value): # Solo i business con numero di star maggiore o uguale ...
                    self._view._lst_results.controls.append(ft.Text(business))
            self._view.update_page()

    # Event handler del secondo pulsante
    def handler_btn_reviews_with_stars(self, e):
        print("handler_btn_reviews_with_stars()")