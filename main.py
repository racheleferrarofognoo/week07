import flet as ft

from database.db_connect import DBConnect
from database.yelp_dao import YelpDao
from model.model import Model
from ui.view import View
from ui.controller import Controller

def main(page : ft.Page):
    model = Model()
    view = View(page)
    controller = Controller(model, view)
    # Posso impostare il Controller solo dopo averlo creato
    view.set_controller(controller)

    # Ritardo la costruzione della GUI in modo che tutto sia pronto
    view.load_interface()

ft.app(target=main)
