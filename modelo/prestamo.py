"""Clase Prestamo: registro de un préstamo activo o cerrado."""


class Prestamo:
    """Vincula a un responsable con un equipo durante un período de tiempo."""

    def __init__(self, responsable, carne, fecha_prestamo, fecha_devolucion, equipo):
        self.responsable = responsable
        self.carne = carne
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.equipo = equipo
        self.activo = True
