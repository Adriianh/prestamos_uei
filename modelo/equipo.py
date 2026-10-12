"""Clase Equipo: datos de un equipo físico."""

from constantes import DISPONIBLE


class Equipo:
    """Representa un equipo físico con código único, nombre, tipo y estado."""

    def __init__(self, codigo, nombre, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.estado = DISPONIBLE

    @property
    def disponible(self):
        return self.estado == DISPONIBLE
