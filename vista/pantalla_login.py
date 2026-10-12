"""PantallaLogin: pantalla A — inicio de sesión."""

import tkinter as tk
from tkinter import messagebox

from constantes import (
    FUENTE, BLANCO, ROJO, GRIS, GRIS_CLARO, NEGRO,
    USUARIO_PRUEBA, CONTRASENA_PRUEBA,
)
from vista.componentes import crear_entry, crear_boton_principal


def _etiqueta_obligatoria(parent, texto):
    """Fila de etiqueta con asterisco rojo indicando campo obligatorio."""
    fila = tk.Frame(parent, bg=BLANCO)
    fila.pack(fill="x")
    tk.Label(fila, text=texto, font=(FUENTE, 11), fg=NEGRO, bg=BLANCO).pack(side="left")
    tk.Label(fila, text=" *", font=(FUENTE, 11), fg=ROJO, bg=BLANCO).pack(side="left")


class PantallaLogin(tk.Frame):
    """Pantalla A: inicio de sesión."""

    def __init__(self, parent, app):
        super().__init__(parent, bg=BLANCO)
        self.app = app

        tk.Label(
            self,
            text="Sistema de Préstamo de\nEquipos – UEI",
            font=(FUENTE, 18, "bold"),
            fg=ROJO,
            bg=BLANCO,
        ).pack(pady=(40, 4))
        tk.Label(
            self,
            text="Universidad del Éxito Instantáneo",
            font=(FUENTE, 11),
            fg=GRIS,
            bg=BLANCO,
        ).pack(pady=(0, 24))

        caja = tk.Frame(self, bg=BLANCO, highlightthickness=1, highlightbackground=GRIS_CLARO)
        caja.pack(padx=40, fill="x")
        tk.Frame(caja, bg=ROJO, height=4).pack(fill="x")
        interior = tk.Frame(caja, bg=BLANCO, padx=24, pady=20)
        interior.pack(fill="x")

        _etiqueta_obligatoria(interior, "Usuario")
        self.entry_usuario = crear_entry(interior)
        self.entry_usuario.pack(fill="x", ipady=4, pady=(2, 12))

        _etiqueta_obligatoria(interior, "Contraseña")
        fila = tk.Frame(interior, bg=BLANCO)
        fila.pack(fill="x", pady=(2, 18))
        self.entry_contrasena = crear_entry(fila, show="*")
        self.entry_contrasena.pack(side="left", fill="x", expand=True, ipady=4)
        self.boton_ojo = tk.Button(
            fila,
            text="Ver",
            font=(FUENTE, 10),
            fg=GRIS,
            bg=BLANCO,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.alternar_ver,
        )
        self.boton_ojo.pack(side="left", padx=(6, 0))

        crear_boton_principal(interior, "Ingresar", self.ingresar).pack(fill="x")

        self.entry_usuario.bind("<Return>", lambda e: self.ingresar())
        self.entry_contrasena.bind("<Return>", lambda e: self.ingresar())

    def alternar_ver(self):
        """Muestra u oculta la contraseña."""
        if self.entry_contrasena.cget("show") == "*":
            self.entry_contrasena.config(show="")
            self.boton_ojo.config(text="Ocultar")
        else:
            self.entry_contrasena.config(show="*")
            self.boton_ojo.config(text="Ver")

    def limpiar(self):
        self.entry_usuario.delete(0, "end")
        self.entry_contrasena.delete(0, "end")
        self.entry_contrasena.config(show="*")
        self.boton_ojo.config(text="Ver")

    def ingresar(self):
        usuario = self.entry_usuario.get().strip()
        contrasena = self.entry_contrasena.get()
        if not usuario or not contrasena:
            messagebox.showwarning("Faltan datos", "Escribe tu usuario y tu contraseña.")
            (self.entry_usuario if not usuario else self.entry_contrasena).focus_set()
            return
        if usuario != USUARIO_PRUEBA or contrasena != CONTRASENA_PRUEBA:
            messagebox.showerror("No se pudo ingresar", "Usuario o contraseña incorrectos.")
            self.entry_contrasena.delete(0, "end")
            self.entry_contrasena.focus_set()
            return
        self.limpiar()
        self.app.mostrar("menu")
