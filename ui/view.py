import flet as ft
from flet.core.alert_dialog import AlertDialog

# Classe che implementa la View del pattern MVC

class View:
    def __init__(self, page : ft.Page):
        self._page = page
        self._controller = None # All'atto della inizializzazione non lo so ancora

        self._page.title = "Yelp"
        self._page.horizontal_alignment = 'CENTER' #ft.CrossAxisAlignment.CENTER

    def set_controller(self, controller):
        self._controller = controller

    def update_page(self):
        self._page.update()

    def show_alert(self, message):
        dlg = AlertDialog(title = ft.Text(message), modal = False)
        self._page.open(dlg)
        self._page.update()

    def load_interface(self):
        # Qui scriverò il codice che crea la GUI
        label  = ft.Text("Business reviews", color = "blue", size = 24)
        self._page.controls.append(label)

        self._dd_stars = ft.Dropdown(label = "Stars",
                            options = [ft.dropdown.Option("1", "*"),
                                       ft.dropdown.Option("2", "**"),
                                       ft.dropdown.Option("3", "***"),
                                       ft.dropdown.Option("4", "****"),
                                       ft.dropdown.Option("5", "*****")],
                            width = 200,
                            hint_text = "Select the number of stars",
                            on_change = self._controller.handler_dropdown_change
                            )

        btn_businesses_with_stars = ft.ElevatedButton(text = "Show businesses",
                                                      width = 200,
                                                      tooltip = "Businesses with stars higher than chosen one",
                                                      on_click = self._controller.handler_btn_businesses_with_stars
                                                      )

        btn_reviews_with_stars = ft.ElevatedButton(text = "Show reviews",
                                                      width = 200,
                                                      tooltip = "Reviews for businesses with stars higher than chosen one",
                                                      on_click= self._controller.handler_btn_reviews_with_stars
                                                      )

        row = ft.Row(controls = [self._dd_stars, btn_businesses_with_stars, btn_reviews_with_stars],
                     alignment = ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row)

        # Questa è la ListView in cui verranno aggiunti i risultati (business, review)
        self._lst_results = ft.ListView(expand = True, spacing = 10, padding = 20)

        #for i in range(1, 100):
        #    lst_results.controls.append(ft.Text(f"Business {i}"))

        self._page.controls.append(self._lst_results)

        self._page.update()