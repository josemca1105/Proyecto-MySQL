from logging import exception
import usuarios.usuario as user
import notas.acciones

class Acciones:

    def registro(self):

        print("\nHola. Procede a registrarte en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu e-mail: ")
        password = input("Introduce tu contraseña: ")

        usuario = user.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado correctamente con el e-mail {registro[1].email}")

        else:
            print("No te has registrado correctamente.")

    def login(self):

        print("\nBienvenido. Identificate en el sistema...")

        try:

            email = input("Introduce tu e-mail: ")
            password = input("Introduce tu contraseña: ")

            usuario = user.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has identificado el {login[5]}")
                self.proximasAcciones(login)
            
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print("Login incorrecto! Intenta más tarde.")

    def proximasAcciones(self, usuario):

        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Qué quieres hacer?: ")
        haz = notas.acciones.Acciones()

        if accion == "crear":
            haz.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            haz.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            haz.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Hasta luego {usuario[1]}!!")
            exit()