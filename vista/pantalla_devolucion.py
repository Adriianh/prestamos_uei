"""PantallaDevolucion: pantalla D — registrar la devolución de un equipo.

Solo requiere carné y código para localizar el préstamo activo.
El campo responsable se conserva por fidelidad al wireframe del boceto.
"""

from tkinter import messagebox

from excepciones import ErrorPrestamo
from vista.formulario_base import FormularioBase


class PantallaDevolucion(FormularioBase):
    """Pantalla D: formulario para registrar una devolución."""

    TITULO = "Devolución"
    TEXTO_BOTON = "Devolver"
    CAMPOS = [
        ("responsable", "Nombre del responsable", True,  False),
        ("carne",       "Carné",                  True,  False),
        ("codigo",      "Código del equipo",       True,  False),
    ]

    def accion(self):
        if self.faltan_campos():
            return
        try:
            self.app.gestor.registrar_devolucion(
                self.valor("carne"),
                self.valor("codigo"),
            )
        except ErrorPrestamo as error:
            self.mostrar_error(error)
            return
        messagebox.showinfo("Devolución registrada", "La devolución se registró correctamente.")
        self.limpiar()
        self.app.mostrar("menu")
