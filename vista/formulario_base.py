"""FormularioBase: parte común de las pantallas C (préstamo) y D (devolución)."""

import tkinter as tk
from tkinter import ttk, messagebox

from constantes import FUENTE, BLANCO, ROJO, ROJO_OSCURO, GRIS, NEGRO, TIPOS_EQUIPO, TIPO_PLACEHOLDER
from excepciones import ErrorPrestamo, FechaInvalida
from vista.componentes import crear_entry, crear_boton_principal


class FormularioBase(tk.Frame):
    """Encabezado con flecha de regreso, campos, validación de vacíos y cancelar.
    Las subclases solo necesitan declarar CAMPOS y definir accion().
    """

    TITULO = ""
    TEXTO_BOTON = ""
    CAMPOS = []

    def __init__(self, parent, app):
        super().__init__(parent, bg=BLANCO)
        self.app = app
        self.entradas = {}

        encabezado = tk.Frame(self, bg=BLANCO)
        encabezado.pack(fill="x", padx=24, pady=(20, 10))
        tk.Button(
            encabezado,
            text="←",
            font=(FUENTE, 16, "bold"),
            fg=ROJO,
            bg=BLANCO,
            activeforeground=ROJO_OSCURO,
            relief="solid",
            bd=1,
            width=3,
            cursor="hand2",
            command=self.cancelar,
        ).pack(side="left")
        tk.Label(
            encabezado,
            text=self.TITULO,
            font=(FUENTE, 19, "bold"),
            fg=NEGRO,
            bg=BLANCO,
        ).pack(side="left", padx=14)

        cuerpo = tk.Frame(self, bg=BLANCO, padx=30)
        cuerpo.pack(fill="x")
        for clave, etiqueta, obligatorio, es_combo in self.CAMPOS:
            fila = tk.Frame(cuerpo, bg=BLANCO)
            fila.pack(fill="x", pady=(8, 0))
            tk.Label(fila, text=etiqueta, font=(FUENTE, 11), fg=NEGRO, bg=BLANCO).pack(side="left")
            if obligatorio:
                tk.Label(fila, text=" *", font=(FUENTE, 11), fg=ROJO, bg=BLANCO).pack(side="left")
            if es_combo:
                widget = ttk.Combobox(cuerpo, values=TIPOS_EQUIPO, state="readonly", font=(FUENTE, 11))
                widget.set(TIPO_PLACEHOLDER)
                widget.pack(fill="x", pady=(2, 0), ipady=2)
            else:
                widget = crear_entry(cuerpo)
                widget.pack(fill="x", ipady=4, pady=(2, 0))
            self.entradas[clave] = widget

        tk.Label(self, text="* Campo obligatorio", font=(FUENTE, 10), fg=GRIS, bg=BLANCO).pack(
            anchor="w", padx=30, pady=(12, 8)
        )
        crear_boton_principal(self, self.TEXTO_BOTON, self.accion).pack(padx=30, anchor="w")

    def valor(self, clave):
        """Devuelve el texto del campo limpio, o '' si es el placeholder del combo."""
        texto = self.entradas[clave].get().strip()
        return "" if texto == TIPO_PLACEHOLDER else texto

    def hay_datos(self):
        """True si al menos un campo tiene contenido."""
        return any(self.valor(c) != "" for c in self.entradas)

    def limpiar(self):
        for widget in self.entradas.values():
            if isinstance(widget, ttk.Combobox):
                widget.set(TIPO_PLACEHOLDER)
            else:
                widget.delete(0, "end")

    def faltan_campos(self):
        """Situación 2: avisa y enfoca el primer campo obligatorio vacío."""
        for clave, etiqueta, obligatorio, _ in self.CAMPOS:
            if obligatorio and self.valor(clave) == "":
                messagebox.showwarning(
                    "Faltan datos",
                    f"Faltan campos por llenar.\nCompleta: {etiqueta}.",
                )
                self.entradas[clave].focus_set()
                return True
        return False

    def mostrar_error(self, error):
        """Convierte un ErrorPrestamo en messagebox y ajusta el foco."""
        if error.nivel == "warning":
            messagebox.showwarning(error.titulo, str(error))
        else:
            messagebox.showerror(error.titulo, str(error))
        widget = self.entradas.get(error.campo)
        if widget is None:
            return
        widget.focus_set()
        if isinstance(error, FechaInvalida):
            widget.delete(0, "end")
        elif isinstance(widget, tk.Entry):
            widget.select_range(0, "end")

    def cancelar(self):
        """Situación 5: pide confirmación si hay datos escritos antes de volver al menú."""
        if self.hay_datos():
            if not messagebox.askyesno(
                "Cancelar operación", "Hay datos escritos. ¿Quieres salir sin guardar?"
            ):
                return
            self.limpiar()
        self.app.mostrar("menu")

    def accion(self):
        raise NotImplementedError
