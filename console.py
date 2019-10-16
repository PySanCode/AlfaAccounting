activo = {
"1.01": """BANCO "X" Cuenta Corriente""",
"1.02": "Caja",
"1.03": "Deudores por ventas",
"1.04": "Documentos a cobrar",
"1.05": "Equipos de computacion",
"1.06": "Inmuebles",
"1.07": "Instalaciones",
"1.08": "Maquinarias",
"1.09": "Materias primas",
"1.10": "Mercaderias",
"1.11": "Muebles y utiles",
"1.12": "Rodados",
"1.13": """Tarjetas de credito "XX" """,
"1.14": "Valores a depositar"
}

pasivo = {
    "2.01": "Acreedores varios",
    "2.02": "Documentos a pagar",
    "2.03": "Proovedores",
    "2.04": "Valores diferidos a pagar"
}

patrimonio_neto = {
    "3.01": "Capital"
}

resultado_negativo = {
    "4.01": "Alquileres perdidos",
    "4.02": "Comisiones perdidas",
    "4.03": "Costo de mercaderias vendidas",
    "4.04": "Descuentos cedidos",
    "4.05": "Fletes y acarreos",
    "4.06": "Gastos generales",
    "4.07": "Impuestos",
    "4.08": "Intereses perdidos",
    "4.09": "Publicidad perdida",
    "4.10": "Seguros",
    "4.11": "Sueldos y jornales"
}

resultado_positivo = {
    "5.01": "Alquileres ganados",
    "5.02": "Comisiones ganadas",
    "5.03": "Descuentos obtenidos",
    "5.04": "Intereses ganados",
    "5.05": "Ventas"
}

valid = ["1.01","1.02","1.03","1.04","1.05","1.06","1.07","1.08","1.09","1.10","1.11","1.12","1.13","1.14",
         "2.01","2.02","2.03","2.04"
         "3.01",
         "4.01","4.02","4.03","4.04","4.05","4.06","4.07","4.08","4.09","4.10","4.11","5.01","5.02","5.03","5.04","5.05"]

segun_dict = {
    "1": "Factura Original",
    "2": "Factura Duplicado",
    "3": "Recibo Original",
    "4": "Recibo Duplicado",
    "5": "Boleta de Deposito",
    "6": "Ficha de Stock"
}

class Asiento():

    def __init__(self):

        self.cuentas = []
        self.segun = ""
        self.segun_display = ""

    def add_cuenta(self, cuenta, debe_o_haber, valor):

        if cuenta in activo:
            cuenta_nombre = activo.get(cuenta)

            if debe_o_haber == "1": sufijo = "(A+)"
            else: sufijo = "(A-)"

            self.cuentas.append({
                "cuenta": cuenta,
                "cuenta_nombre": cuenta_nombre,
                "tipo": "activo",
                "sufijo": sufijo,
                "display": cuenta_nombre + sufijo,
                "debe_o_haber": debe_o_haber,
                "valor": valor
            })

        elif cuenta in pasivo:
            cuenta_nombre = pasivo.get(cuenta)

            if debe_o_haber == "1": sufijo = "(P+)"
            else: sufijo = "(P-)"

            self.cuentas.append({
                "cuenta": cuenta,
                "cuenta_nombre": cuenta_nombre,
                "tipo": "pasivo",
                "sufijo": sufijo,
                "display": cuenta_nombre + sufijo,
                "debe_o_haber": debe_o_haber,
                "valor": valor
            })

        elif cuenta in patrimonio_neto:
            cuenta_nombre = patrimonio_neto.get(cuenta)

            if debe_o_haber == "1": sufijo = "(P.N+)"
            else: sufijo = "(P.N-)"

            self.cuentas.append({
                "cuenta": cuenta,
                "cuenta_nombre": cuenta_nombre,
                "tipo": "patrimonio_neto",
                "sufijo": sufijo,
                "display": cuenta_nombre + sufijo,
                "debe_o_haber": debe_o_haber,
                "valor": valor
            })

        elif cuenta in resultado_negativo:
            cuenta_nombre = resultado_negativo.get(cuenta)

            sufijo = "(R.N.)"

            self.cuentas.append({
                "cuenta": cuenta,
                "cuenta_nombre": cuenta_nombre,
                "tipo": "resultado_negativo",
                "sufijo": sufijo,
                "display": cuenta_nombre + sufijo,
                "debe_o_haber": debe_o_haber,
                "valor": valor
            })

        elif cuenta in resultado_positivo:
            cuenta_nombre = resultado_positivo.get(cuenta)

            sufijo = "(R.P.)"

            self.cuentas.append({
                "cuenta": cuenta,
                "cuenta_nombre": cuenta_nombre,
                "tipo": "resultado_positivo",
                "sufijo": sufijo,
                "display": cuenta_nombre + sufijo,
                "debe_o_haber": debe_o_haber,
                "valor": valor
            })

    def set_fecha(self, fecha):

        self.fecha = fecha

    def set_segun(self, segun):

        self.segun = segun
        self.segun_display = segun_dict.get(segun)

class Libro_Diario():

    def __init__(self):

        self.asientos = []

    def add_asiento(self, asiento):

        self.asientos.append(asiento)

def new():
    libro = Libro_Diario()

    while True:
        asiento = Asiento()

        fecha = input("\nFecha:\n> ")
        asiento.set_fecha(fecha)

        cuenta = input("\nCuenta:\n> ")

        while cuenta not in valid:
            cuenta = input("\nCuenta:\n> ")

        debe_o_haber = input(
            "\n¿Debe o haber?"
            "\n1 = Debe"
            "\n2 = Haber"
            "\n> "
        )

        while debe_o_haber != "1" and debe_o_haber != "2":

            debe_o_haber = input(
                "\n¿Debe o haber?"
                "\n1 = Debe"
                "\n2 = Haber"
                "\n> "
            )

        if debe_o_haber == "1":
            valor = input("\nValor: \n> ")

        elif debe_o_haber == "2":
            valor = input("\nValor: \n> ")

        segun = input(
            "\n¿Segun?"
            "\n1 = Factura Original"
            "\n2 = Factura Duplicado"
            "\n3 = Recibo Original"
            "\n4 = Recibo Duplicado"
            "\n5 = Boleta de Deposito"
            "\n6 = Ficha de Stock"
            "\n> "
        )

        while segun != "1" and segun != "2" and segun != "3" and segun != "4" and segun != "5" and segun != "6":

            segun = input(
                "\n¿Segun?"
                "\n1 = Factura Original"
                "\n2 = Factura Duplicado"
                "\n3 = Recibo Original"
                "\n4 = Recibo Duplicado"
                "\n5 = Boleta de Deposito"
                "\n6 = Ficha de Stock"
                "\n> "
            )

        asiento.set_segun(segun)

        asiento.add_cuenta(cuenta,debe_o_haber,valor)

        continuar = input(
            "\n¿Que desea hacer?"
            "\n1 = Continuar otra cuenta"
            "\n2 = Continuar con el libro"
            "\n3 = Volver a editar" #FALTA EDITAR SOLO UNA CUENTA
            "\n4 = Editar solo un elemento"
            "\n5 = Parar"
            "\n> "
        )

        while continuar != "1" and continuar != "2" and continuar != "3" and continuar != "4" and continuar != "5":

            continuar = input(
                "\n¿Que desea hacer?"
                "\n1 = Continuar otra cuenta"
                "\n2 = Continuar con el libro"
                "\n3 = Volver a editar"  # FALTA EDITAR SOLO UNA CUENTA
                "\n4 = Editar solo un elemento"
                "\n5 = Parar"
                "\n> "
            )

        if continuar == "3": continue

        if continuar == "1":
            while True:
                cuenta = input("\nCuenta:\n> ")

                debe_o_haber = input(
                    "\n¿Debe o haber?"
                    "\n1 = Debe"
                    "\n2 = Haber"
                    "\n> "
                )

                valor = input("\nValor: \n> ")

                continuar = input(
                    "\n¿Que desea hacer?"
                    "\n1 = Continuar otra cuenta"
                    "\n2 = Continuar con el libro"
                    "\n3 = Volver a editar cuenta"
                    "\n4 = Editar solo un elemento"
                    "\n5 = Parar"
                    "\n> "
                )

                if continuar == "4":

                    editar = input(
                    "\n¿Que desea editar?"
                    "\n1 = Cuenta"
                    "\n2 = Debe o haber"
                    "\n3 = Valor"
                    "\n4 = Editar solo un elemento"
                    "\n5 = Nada"
                    "\n> "
                    )

                    if editar == "1":

                        while True:
                            while cuenta not in valid:
                                cuenta = input("\nCuenta:\n> ")
                                if cuenta in valid and input("\n¿Seguro? S/N\n> ").lower == "S": break

                    if editar == "2":

                        while True:

                            while debe_o_haber != "1" and debe_o_haber != "2":

                                debe_o_haber = input(
                                    "\n¿Debe o haber?"
                                    "\n1 = Debe"
                                    "\n2 = Haber"
                                    "\n> "
                                )
                                if debe_o_haber == "1" or debe_o_haber == "2" and input("\n¿Seguro? S/N\n> ").lower == "S": break

                if continuar == "3": continue

                asiento.add_cuenta(cuenta,debe_o_haber,valor)
                if continuar == "2": break

        libro.add_asiento(asiento)
        if continuar == "5": break

    display(libro)

def display(libro):
    print("| ", "Fecha", " " * (6 - len("fecha")), "| ", "Detalle", " " * (40 - len("detalle")), "| ", "Debe",
    " " * (10 - len(("debe"))), "| ", "Haber", " " * (10 - len("haber")), "|")

    for asiento in libro.asientos:

        print("| ", "", " " * (6),
              "| ", "-------------------{}--------------------".format(libro.asientos.index(asiento)+1), " " * (40 - 40),
              "| ", "", " " * (10),
              "| ", "", " " * (10), "|")

        print("| ", asiento.fecha, " " * (6 - len(asiento.fecha)),
              "| ", asiento.cuentas[0].get("display"), " " * (40 - len(asiento.cuentas[0].get("display"))),
              "| ", asiento.cuentas[0].get("valor"), " " * (10 - len((asiento.cuentas[0].get("valor")))),
              "| ", "", " " * (10), "|")

        for cuenta in asiento.cuentas:

            if cuenta == asiento.cuentas[0]: continue

            if cuenta.get("debe_o_haber") == "1":
                print("| ", "", " " * (6),
                      "| ", cuenta.get("display"), " " * (40 - len(cuenta.get("display"))),
                      "| ", cuenta.get("valor"), " " * (10 - len((cuenta.get("valor")))),
                      "| ", "", " " * (10), "|")

        for cuenta in asiento.cuentas:

            if cuenta == asiento.cuentas[0]: continue

            if cuenta.get("debe_o_haber") == "2":
                print("| ", "", " " * (6),
                      "| ", "    " + cuenta.get("display"), " " * (40 - (len((cuenta.get("display"))) + len("    "))),
                      "| ", "", " " * (10),
                      "| ", cuenta.get("valor"), " " * (10 - len((cuenta.get("valor")))), "|")

        if asiento == libro.asientos[0]:
            print("| ", "", " " * (6),
                  "| ", "Segun Inventario Inicial", " " * (40 - (len("Segun Inventario Inicial"))),
                  "| ", "", " " * (10),
                  "| ", "", " " * (10), "|")

        else:

            print("| ", "", " " * (6),
                  "| ", asiento.segun_display, " " * (40 - (len(asiento.segun_display))),
                  "| ", "", " " * (10),
                  "| ", "", " " * (10), "|")

print("AlfaBOOK Edicion Consola\n"
      "Version 1.0")
print("Escribe 0 para volver si te equivocas")

while True:

    start = input(
    "Que desea hacer? \n"
    "1 = Nuevo archivo \n"
    "2 = Cargar archivo\n"
    "> "
    )
    if start == "1" or start == "2": break

if start == "1":
    new()

if start == "2":
    load_previous()

# libro = Libro_Diario()
# asiento1 = Asiento()
# asiento2 = Asiento()
# asiento3 = Asiento()
#
# asiento1.add_cuenta("1.03","1","5050")
# asiento1.add_cuenta("1.11","1","1000")
# asiento1.add_cuenta("1.01","1","1500")
# asiento1.add_cuenta("4.01","2","2000")
# asiento1.set_fecha("05/05")
#
# asiento2.add_cuenta("1.04","1","1500")
# asiento2.add_cuenta("1.05","1","3000")
# asiento2.add_cuenta("1.06","1","2500")
# asiento2.add_cuenta("1.01","2","5000")
# asiento2.set_fecha("08/05")
# asiento2.set_segun("3")
#
# asiento3.add_cuenta("1.07","1","50")
# asiento3.add_cuenta("1.08","1","1200")
# asiento3.add_cuenta("1.09","1","5050")
# asiento3.add_cuenta("1.10","2","2010")
# asiento3.set_fecha("10/05")
# asiento3.set_segun("4")
#
# libro.add_asiento(asiento1)
# libro.add_asiento(asiento2)
# libro.add_asiento(asiento3)
#
# display(libro)

"""

|  Fecha   |  Detalle                                   |  Debe        |  Haber       |
|          |  -------------------1--------------------  |              |              |
|  05/05   |  BANCO "X" Cuenta Corriente(A+)            |  500         |              |
|          |  Caja(A+)                                  |  1000        |              |
|          |  Deudores por ventas(A+)                   |  500         |              |
|          |      Capital(P.N-)                         |              |  2000        |
|          |  -------------------2--------------------  |              |              |
|  08/05   |  Documentos a cobrar(A+)                   |  1500        |              |
|          |  Equipos de computacion(A+)                |  3000        |              |
|          |  Inmuebles(A+)                             |  2500        |              |
|          |      BANCO "X" Cuenta Corriente(A-)        |              |  5000        |
|          |  -------------------3--------------------  |              |              |
|  10/05   |  Instalaciones(A+)                         |  50          |              |
|          |  Maquinarias(A+)                           |  1200        |              |
|          |  Materias primas(A+)                       |  5050        |              |
|          |      Mercaderias(A-)                       |              |  2010        |


"""