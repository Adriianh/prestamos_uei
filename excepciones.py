"""Excepciones de la lógica de negocio. No usan Tkinter.
La vista las captura y las convierte en messagebox.
"""


class ErrorPrestamo(Exception):
    """Error de reglas del negocio. La vista lo convierte en messagebox."""

    titulo = "Error"
    nivel = "error"  # "warning" o "error"

    def __init__(self, mensaje, campo=None):
        super().__init__(mensaje)
        self.campo = campo  # clave del campo que la vista debe enfocar


class EquipoNoDisponible(ErrorPrestamo):
    """Situación 1: el equipo ya está prestado."""

    titulo = "Equipo no disponible"
    nivel = "warning"


class FechaInvalida(ErrorPrestamo):
    """Situación 3: formato o lógica de fechas incorrecta."""

    titulo = "Fecha incorrecta"
    nivel = "error"


class SinPrestamoActivo(ErrorPrestamo):
    """Situación 4: no existe un préstamo activo para ese código + carné."""

    titulo = "Sin préstamo activo"
    nivel = "error"
