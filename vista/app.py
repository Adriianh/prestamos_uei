"""App: ventana principal — crea las pantallas y gestiona la navegación."""

import tkinter as tk
from tkinter import messagebox

from constantes import NOMBRE_PROGRAMA, FUENTE, BLANCO, GRIS_FONDO, NEGRO
from modelo.gestor import GestorPrestamos
from vista.formulario_base import FormularioBase
from vista.pantalla_login import PantallaLogin
from vista.pantalla_menu import PantallaMenu
from vista.pantalla_prestamo import PantallaPrestamo
from vista.pantalla_devolucion import PantallaDevolucion


class App(tk.Tk):
    """Ventana principal: apila todas las pantallas y cambia entre ellas con tkraise()."""

    def __init__(self):
        super().__init__()
        self.title(NOMBRE_PROGRAMA)
        self.geometry("460x640")
        self.resizable(False, False)
        self.configure(bg=BLANCO)
        self.gestor = GestorPrestamos()

        barra = tk.Menu(self, bg=GRIS_FONDO, fg=NEGRO, font=(FUENTE, 10))
        ayuda = tk.Menu(barra, tearoff=0)
        ayuda.add_command(
            label="Acerca de",
            command=lambda: messagebox.showinfo(
                "Acerca de",
                f"{NOMBRE_PROGRAMA}\nUniversidad del Éxito Instantáneo",
            ),
        )
        barra.add_cascade(label="Ayuda", menu=ayuda)
        self.config(menu=barra)

        contenedor = tk.Frame(self, bg=BLANCO)
        contenedor.pack(fill="both", expand=True)
        contenedor.grid_rowconfigure(0, weight=1)
        contenedor.grid_columnconfigure(0, weight=1)

        self.pantallas = {
            "login":      PantallaLogin(contenedor, self),
            "menu":       PantallaMenu(contenedor, self),
            "prestamo":   PantallaPrestamo(contenedor, self),
            "devolucion": PantallaDevolucion(contenedor, self),
        }
        for pantalla in self.pantallas.values():
            pantalla.grid(row=0, column=0, sticky="nsew")

        self.actual = None
        self.mostrar("login")
        self.protocol("WM_DELETE_WINDOW", self.cerrar)

    def mostrar(self, nombre):
        self.actual = self.pantallas[nombre]
        self.actual.tkraise()

    def cerrar(self):
        """Situación 6: pide confirmación si hay datos sin guardar antes de cerrar."""
        pantalla = self.actual
        if isinstance(pantalla, FormularioBase) and pantalla.hay_datos():
            if not messagebox.askyesno(
                "Cerrar aplicación",
                "Hay datos sin guardar. ¿Quieres salir de todos modos?",
            ):
                return
        self.destroy()
