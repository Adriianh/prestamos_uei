"""Funciones factory de widgets reutilizables."""

import tkinter as tk

from constantes import FUENTE, BLANCO, ROJO, ROJO_OSCURO, GRIS, NEGRO


def crear_boton_principal(parent, texto, comando):
    """Botón rojo con texto blanco (Ingresar, Registrar, Devolver)."""
    return tk.Button(
        parent,
        text=texto,
        command=comando,
        font=(FUENTE, 12, "bold"),
        fg=BLANCO,
        bg=ROJO,
        activebackground=ROJO_OSCURO,
        activeforeground=BLANCO,
        relief="flat",
        bd=0,
        padx=20,
        pady=8,
        cursor="hand2",
    )


def crear_boton_contorno(parent, texto, comando):
    """Botón con borde rojo; al pasar el mouse los colores se invierten."""
    marco = tk.Frame(parent, bg=ROJO, padx=2, pady=2)
    boton = tk.Button(
        marco,
        text=texto,
        command=comando,
        font=(FUENTE, 16, "bold"),
        fg=ROJO,
        bg=BLANCO,
        activeforeground=BLANCO,
        activebackground=ROJO,
        relief="flat",
        bd=0,
        width=14,
        pady=10,
        cursor="hand2",
    )
    boton.pack()
    boton.bind("<Enter>", lambda e: boton.config(bg=ROJO, fg=BLANCO))
    boton.bind("<Leave>", lambda e: boton.config(bg=BLANCO, fg=ROJO))
    return marco


def crear_entry(parent, **opciones):
    """Campo de texto con borde que se torna rojo al recibir foco."""
    return tk.Entry(
        parent,
        font=(FUENTE, 11),
        fg=NEGRO,
        bg=BLANCO,
        relief="flat",
        highlightthickness=1,
        highlightbackground=GRIS,
        highlightcolor=ROJO,
        **opciones,
    )
