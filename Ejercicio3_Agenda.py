import sys


class Agenda:
    def __init__(self):
        self.__contactos = []

    def menu(self):
        num1 = int(
            input(
                "Introduzca un número según la función a realizar:\nAñadir contacto: 1\nMostrar Lista de Contactos: 2\nBuscar Contacto: 3\nEditar Contacto: 4\nCualquier otro número cerrara la agenda\n"
            )
        )

        if num1 == 1:
            self.add()
        elif num1 == 2:
            self.lista()
        elif num1 == 3:
            self.buscar()
        elif num1 == 4:
            self.edit()
        else:
            sys.exit("Programa finalizado")

    def add(self):
        nom = str(input("Introduzca el nombre: "))
        tel = int(input("Introduzca el telefono: "))
        email = str(input("Introduzca el email: "))
        contacto = [nom, tel, email]

        num2 = int(
            input(
                "¿Es "
                + str(contacto)
                + " correcto?\nNo, modificar: 1\nCualquier otro número seguirá el programa.\n",
            )
        )
        if num2 == 1:
            self.add()

        self.__contactos.append(contacto)
        print("Contacto añadido correctamente\n")
        self.menu()

    def lista(self):
        contador = 1
        for i in self.__contactos:
            print("Contacto", contador, ":", i, "\n")
            contador += 1
        self.menu()

    def buscar(self):

        nombre = input("Introduzca el nombre del contacto que desea buscar:\n")
        for i in self.__contactos:
            for j in i:
                if nombre == j:
                    print("El contacto es:", i, "\n")
        self.menu()

    def edit(self):
        contador = 1
        for i in self.__contactos:
            print("Contacto", contador, ":", i, "\n")
            contador += 1

        num3 = int(input("Introduzca el número del contacto que quiera modificar.\n"))

        item = int(input("¿Que desea modificar?\nNombre: 1\nTelefono: 2\nEmail: 3\n"))

        (self.__contactos[num3 - 1])[item - 1] = input(
            "Se modificará "
            + str((self.__contactos[num3 - 1])[item - 1])
            + ". Introduzca a lo que se modificará "
        )
        print("El contacto ahora es", i)

        self.menu()


agenda1 = Agenda()
agenda1.menu()
