"""Sistema de Préstamo de Equipos – UEI
Punto de entrada principal. Ejecutar con: python prestamos.py

Arquitectura:
  constantes.py   — colores, fuentes y valores de dominio
  excepciones.py  — ErrorPrestamo y sus subclases (sin Tkinter)
  modelo/         — Equipo, Prestamo, GestorPrestamos (lógica pura)
  vista/          — App, pantallas A–D y widgets reutilizables (Tkinter)

Manejo de errores (7 situaciones):
  1. Equipo ya prestado             → showwarning, foco en código
  2. Campos obligatorios vacíos     → showwarning, foco en el campo vacío
  3. Fecha de devolución inválida   → showerror, borra solo la fecha mala
  4. Devolución sin préstamo activo → showerror, sin foco específico
  5. Cancelar con datos escritos    → askyesno antes de volver al menú
  6. Cerrar con datos sin guardar   → askyesno antes de destruir la ventana
  7. Credenciales incorrectas       → showerror, borra contraseña
"""

from vista.app import App

if __name__ == "__main__":
    App().mainloop()
