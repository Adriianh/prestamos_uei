"""PantallaMenu: pantalla B — menú principal."""

import tkinter as tk

from constantes import FUENTE, BLANCO, ROJO, NEGRO
from vista.componentes import crear_boton_contorno


class PantallaMenu(tk.Frame):
    """Pantalla B: menú principal con dos opciones."""

    def __init__(self, parent, app):
        super().__init__(parent, bg=BLANCO)
        tk.Label(
            self,
            text="Sistema de Préstamo de\nEquipos – UEI",
            font=(FUENTE, 18, "bold"),
            fg=ROJO,
            bg=BLANCO,
        ).pack(pady=(60, 20))
        tk.Label(
            self,
            text="Selecciona una opción",
            font=(FUENTE, 14),
            fg=NEGRO,
            bg=BLANCO,
        ).pack(pady=(0, 30))
        crear_boton_contorno(self, "Préstamo", lambda: app.mostrar("prestamo")).pack(pady=8)
        crear_boton_contorno(self, "Devolución", lambda: app.mostrar("devolucion")).pack(pady=8)
