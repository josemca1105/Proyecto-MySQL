import notas.nota as modelo

class Acciones:

    def crear(self, usuario):

        print(f"\nOk {usuario[1]}, vamos a crear una nueva nota...")

        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Agrega contenido a la nota creada: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto! Se ha guardado la nota: {nota.titulo}")
        
        else:
            print(f"\nNo se ha guardado la nota, lo lamento {usuario[1]}.")
    
    def mostrar(self, usuario):

        print(f"\nOk {usuario[1]}, aquí tienes tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n**************************")
            print(nota[2])
            print(nota[3])
            print("\n**************************")
    
    def borrar(self, usuario):

        print(f"\nOk {usuario[1]}, vamos a borrar algunas notas!")

        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Se ha borrado la nota {nota.titulo}.")
        
        else:
            print("No se ha borrado la nota, intenta más tarde.")