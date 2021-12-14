"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la bbdd
- Si elegimos login, identificara al usuario y nos preguntara que queremos hacer:
- Crear nota, mostrar notas, borrarlas
"""
from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")

haz = acciones.Acciones()
accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
    haz.registro()

elif accion == "login":
    haz.login()