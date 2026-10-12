"""PantallaPrestamo: pantalla C — registrar un nuevo préstamo."""

from tkinter import messagebox

from excepciones import ErrorPrestamo
from vista.formulario_base import FormularioBase


class PantallaPrestamo(FormularioBase):
    """Pantalla C: formulario para registrar un préstamo."""

    TITULO = "Registrar préstamo"
    TEXTO_BOTON = "Registrar"
    CAMPOS = [
        ("responsable",      "Nombre del responsable",          True,  False),
        ("carne",            "Carné",                           True,  False),
        ("fecha_prestamo",   "Fecha de préstamo (dd/mm/aaaa)",  True,  False),
        ("fecha_devolucion", "Fecha de devolución (dd/mm/aaaa)", False, False),
        ("nombre",           "Nombre del equipo",               True,  False),
        ("tipo",             "Tipo de equipo",                  True,  True),
        ("codigo",           "Código del equipo",               True,  False),
    ]

    def accion(self):
        if self.faltan_campos():
            return
        try:
            self.app.gestor.registrar_prestamo(
                self.valor("responsable"),
                self.valor("carne"),
                self.valor("fecha_prestamo"),
                self.valor("fecha_devolucion"),
                self.valor("nombre"),
                self.valor("tipo"),
                self.valor("codigo"),
            )
        except ErrorPrestamo as error:
            self.mostrar_error(error)
            return
        messagebox.showinfo("Préstamo registrado", "El préstamo se guardó correctamente.")
        self.limpiar()
        self.app.mostrar("menu")
