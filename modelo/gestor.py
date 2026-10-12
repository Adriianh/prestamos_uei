"""GestorPrestamos: lógica de negocio. No usa Tkinter."""

from datetime import datetime

from constantes import DISPONIBLE, PRESTADO, FORMATO_FECHA
from excepciones import EquipoNoDisponible, FechaInvalida, SinPrestamoActivo
from modelo.equipo import Equipo
from modelo.prestamo import Prestamo


def _normalizar_codigo(codigo):
    """lp-01 y LP-01 se tratan como el mismo código."""
    return codigo.strip().upper()


def _parsear_fecha(texto, campo):
    """Convierte texto dd/mm/aaaa a datetime.date. Lanza FechaInvalida si falla."""
    try:
        return datetime.strptime(texto.strip(), FORMATO_FECHA).date()
    except ValueError:
        raise FechaInvalida(
            "La fecha debe tener el formato dd/mm/aaaa (por ejemplo 25/10/2026).",
            campo,
        )


class GestorPrestamos:
    """Guarda los equipos y préstamos y aplica las reglas de negocio."""

    def __init__(self):
        self.equipos = {}
        self.prestamos = []

    def registrar_prestamo(
        self, responsable, carne, fecha_prestamo, fecha_devolucion, nombre, tipo, codigo
    ):
        f_pres = _parsear_fecha(fecha_prestamo, "fecha_prestamo")
        f_dev = None
        if fecha_devolucion.strip():
            f_dev = _parsear_fecha(fecha_devolucion, "fecha_devolucion")
            if f_dev < f_pres:
                raise FechaInvalida(
                    "La fecha de devolución no puede ser anterior a la fecha de préstamo.",
                    "fecha_devolucion",
                )

        codigo = _normalizar_codigo(codigo)
        equipo = self.equipos.get(codigo)
        if equipo is not None and not equipo.disponible:
            raise EquipoNoDisponible(
                f"El equipo con código {codigo} ya está prestado.\n"
                "Cambia el código del equipo.",
                "codigo",
            )
        if equipo is None:
            equipo = Equipo(codigo, nombre.strip(), tipo)
            self.equipos[codigo] = equipo
        else:
            equipo.nombre = nombre.strip()
            equipo.tipo = tipo

        prestamo = Prestamo(responsable.strip(), carne.strip(), f_pres, f_dev, equipo)
        self.prestamos.append(prestamo)
        equipo.estado = PRESTADO
        return prestamo

    def registrar_devolucion(self, carne, codigo):
        codigo = _normalizar_codigo(codigo)
        prestamo = self.buscar_prestamo_activo(codigo, carne.strip())
        if prestamo is None:
            raise SinPrestamoActivo(
                "Ese equipo no tiene un préstamo activo con ese carné.\n"
                "Revisa los datos ingresados.",
                None,
            )
        prestamo.activo = False
        prestamo.equipo.estado = DISPONIBLE
        return prestamo

    def buscar_prestamo_activo(self, codigo, carne):
        """Devuelve el Prestamo activo que coincide con código + carné, o None."""
        for p in self.prestamos:
            if p.activo and p.equipo.codigo == codigo and p.carne == carne:
                return p
        return None
