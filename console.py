__author__ = "Santiago Moreno"
__copyright__ = "Copyright (C) 2019 Santiago Moreno"
__license__ = "Todos los derechos reservados"
__version__ = "1.0"

import os

segun_dict = {
    "0": "Segun Inventario Inicial",
    "1": "Segun Factura Original",
    "2": "Segun Factura Duplicado",
    "3": "Segun Recibo Original",
    "4": "Segun Recibo Duplicado",
    "5": "Segun Boleta de Deposito",
    "6": "Segun Ficha de Stock"
}

class Libro_Diario():

    def __init__(self):

        self.asientos = []

    def add_asiento(self, asiento):

        self.asientos.append(asiento)

class Asiento():

    def __init__(self, number, first=False):

        self.cuentas = []
        self.first = first
        self.number = number
        self.total_debe = 0
        self.total_haber = 0

    def add_cuenta(self, cuenta, debe_o_haber, valor):

        cuentas_list.get(cuenta).add_use(self.number, debe_o_haber, valor)

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

            if debe_o_haber == "1": sufijo = "(P-)"
            else: sufijo = "(P+)"

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

            if debe_o_haber == "1": sufijo = "(P.N-)"
            else: sufijo = "(P.N+)"

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

    def set_totals(self, total_debe, total_haber):

        self.total_debe = total_debe
        self.total_haber = total_haber

class Cuenta():

    def __init__(self, number, name):

        self.number = number
        self.name = name
        self.used = []
        self.debe = 0
        self.haber = 0
        self.saldo_tipo = ""
        self.saldo_valor = 0

    def add_use(self, number, debe_o_haber, valor):

        self.used.append({
            "number": number,
            "debe_o_haber": debe_o_haber,
            "valor": int(valor)
        })

    def calc_totals(self):

        for use in self.used:

            if use.get("debe_o_haber") == "1":

                self.debe += use.get("valor")

            elif use.get("debe_o_haber") == "2":

                self.haber += use.get("valor")

        if self.debe > self.haber:

            self.saldo_tipo = "Saldo Deudor"
            self.saldo_valor = self.debe - self.haber

        elif self.haber > self.debe:

            self.saldo_tipo = "Saldo Acreedor"
            self.saldo_valor = self.haber - self.debe

        else:

            self.saldo_tipo = "Cuenta Saldada"

def load_plan():

    global activo
    global pasivo
    global patrimonio_neto
    global resultado_negativo
    global resultado_positivo
    global valid
    global cuentas_list

    activo = {}
    pasivo = {}
    patrimonio_neto = {}
    resultado_negativo = {}
    resultado_positivo = {}
    valid = {}
    cuentas_list = {}

    with open("plan_de_cuentas.txt", "r") as file:

        lines = file.read().splitlines()

        for line in lines:
            if line == "":
                modo_activo = False
                modo_pasivo = False
                modo_pn = False
                modo_rn = False
                modo_rp = False
                continue

            if line == "Activo":
                modo_activo = True
                continue

            elif line == "Pasivo":
                modo_pasivo = True
                continue

            elif line == "Patrimonio Neto":
                modo_pn = True
                continue

            elif line == "Resultado Negativo":
                modo_rn = True
                continue

            elif line == "Resultado Positivo":
                modo_rp = True
                continue

            line = line.split(":")

            if modo_activo:
                activo.update({line[0]: line[1]})
                valid.update({line[0]: line[1]})
                cuentas_list.update({line[0]: Cuenta(line[0], line[1])})

            elif modo_pasivo:
                pasivo.update({line[0]: line[1]})
                valid.update({line[0]: line[1]})
                cuentas_list.update({line[0]: Cuenta(line[0], line[1])})

            elif modo_pn:
                patrimonio_neto.update({line[0]: line[1]})
                valid.update({line[0]: line[1]})
                cuentas_list.update({line[0]: Cuenta(line[0], line[1])})

            elif modo_rn:
                resultado_negativo.update({line[0]: line[1]})
                valid.update({line[0]: line[1]})
                cuentas_list.update({line[0]: Cuenta(line[0], line[1])})

            elif modo_rp:
                resultado_positivo.update({line[0]: line[1]})
                valid.update({line[0]: line[1]})
                cuentas_list.update({line[0]: Cuenta(line[0], line[1])})

    pass

def new():

    libro = Libro_Diario()
    first = True
    modo_asiento = True
    skip = False

    while True:

        if modo_asiento:
            if first: asiento = Asiento(len(libro.asientos) + 1, first=True)
            else: asiento = Asiento(len(libro.asientos) + 1)

            fecha = input("\nFecha:\n> ")
            asiento.set_fecha(fecha)

        if not skip:

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

            valor = input("\nValor: \n> ")
            try:
                valor = int(valor)
            except:
                pass
            while type(valor) != int:
                valor = input("\nValor:\n> ")
                try:
                    valor = int(valor)
                except:
                    pass
            valor = str(valor)

            if modo_asiento:
                if asiento.first:
                    asiento.set_segun("0")
                    first = False

                else:

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

        skip = False

        continuar = input(
            "\n¿Que desea hacer?"
            "\n1 = Continuar otra cuenta"
            "\n2 = Continuar con el libro"
            "\n3 = Volver a editar" #FALTA EDITAR SOLO UNA CUENTA
            "\n4 = Editar solo un elemento"
            "\n5 = Parar y guardar"
            "\n> "
        )

        while continuar != "1" and continuar != "2" and continuar != "3" and continuar != "4" and continuar != "5":

            continuar = input(
                "\n¿Que desea hacer?"
                "\n1 = Continuar otra cuenta"
                "\n2 = Continuar con el libro"
                "\n3 = Volver a editar"
                "\n4 = Editar solo un elemento"
                "\n5 = Parar y guardar"
                "\n> "
            )

        if continuar == "1":
            modo_asiento = False
            asiento.add_cuenta(cuenta, debe_o_haber, valor)
            continue

        if continuar == "2":
            modo_asiento = True
            asiento.add_cuenta(cuenta, debe_o_haber, valor)
            libro.add_asiento(asiento)
            continue

        if continuar == "3": continue

        if continuar == "4":

            editar = input(
                "\n¿Que desea editar?"
                "\n1 = Cuenta"
                "\n2 = Debe o haber"
                "\n3 = Valor"
                "\n4 = Nada"
                "\n> "
            )

            while editar != "1" and editar != "2" and editar != "3" and editar != "4":
                editar = input(
                    "\n¿Que desea editar?"
                    "\n1 = Cuenta"
                    "\n2 = Debe o haber"
                    "\n3 = Valor"
                    "\n4 = Nada"
                    "\n> "
                )

            if editar == "1":

                cuenta = input("\nCuenta:\n> ")
                while cuenta not in valid:
                    cuenta = input("\nCuenta:\n> ")
                    if cuenta in valid and input("\n¿Seguro?\n1 = Si\n2 = No\n> ") == "1":
                        break
                    else:
                        continue

            if editar == "2":

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
                    if debe_o_haber == "1" or debe_o_haber == "2" and input("\n¿Seguro?\n1 = Si\n2 = No\n> ") == "1":
                        break
                    else:
                        continue

            if editar == "3":
                while type(valor) != int:
                    valor = input("\nValor:\n> ")
                    if input("\n¿Seguro?\n1 = Si\n2 = No\n> ") == "1":
                        break
                    else:
                        continue

            asiento.add_cuenta(cuenta, debe_o_haber, valor)

            if editar == "4": pass # NO EDITAR NADA

            skip = True

        if continuar == "5":
            libro.add_asiento(asiento)
            asiento.add_cuenta(cuenta, debe_o_haber, valor)
            save(libro)
            break

    display_libro_diario(libro)
    display_libro_mayor(libro)
    display_balance(libro)

def save(libro):

    while True:

        nombre = input("\nNombre del archivo: ")

        try:

            file = open("saved\{}.abk".format(str(nombre)), "x")

            for asiento in libro.asientos:

                file.write("Asiento{}\n".format(asiento.number))

                file.write("Fecha:{}\n".format(asiento.fecha))

                for cuenta in asiento.cuentas:

                    file.write("{},{},{}\n".format(cuenta.get("cuenta"), cuenta.get("debe_o_haber"), cuenta.get("valor")))

                file.write("Segun:{}\n".format(asiento.segun))

            file.close()

            break

        except FileExistsError:

            print("El archivo ya existe, elija otro nombre")

def load():

    load_plan()

    try:

        for carpeta, carpetas, files in os.walk("saved"):

            archivos = files

    except:

        pass

    print("¿Cual archivo desea cargar?")

    i = 1

    for file in archivos:

        print("{} = {}".format(i, file))
        i += 1

    while True:
        try:
            to_load = int(input("> "))
            break
        except: pass

    while to_load < 1 or to_load > len(archivos):

        print("¿Cual archivo desea cargar?")

        i = 1

        for file in archivos:
            print("{} = {}".format(i, file))
            i += 1

        to_load = int(input("> "))

    with open("saved/{}".format(archivos[to_load - 1]), "r") as archivo:

        libro = Libro_Diario()

        for linea in archivo.read().splitlines():

            if linea[:7] == "Asiento":

                asiento = Asiento(linea[7:])

            elif linea[:6] == "Fecha:":

                asiento.set_fecha(linea[6:])

            elif linea[:6] == "Segun:":

                asiento.set_segun(linea[6:])
                libro.add_asiento(asiento)

            else:

                cuenta, debe_o_haber, valor = linea.split(",")
                asiento.add_cuenta(cuenta, debe_o_haber, valor)

        libro.add_asiento(asiento)

    display_libro_diario(libro)
    display_libro_mayor(libro)
    display_balance(libro)

def display_libro_diario(libro):

    print("| ", "Fecha", " " * (10 - len("fecha")),
          "| ", "N°", " " * (5 - len("N°")),
          "| ", "Detalle", " " * (40 - len("detalle")),
          "| ", "Debe", " " * (10 - len(("debe"))),
          "| ", "Haber", " " * (10 - len("haber")), "|")

    for asiento in libro.asientos:

        print("| ", "", " " * (10),
              "| ", "", " " * (5),
              "| ", "-------------------{}--------------------".format(libro.asientos.index(asiento)+1), " " * (40 - 40),
              "| ", "", " " * (10),
              "| ", "", " " * (10), "|")

        print("| ", asiento.fecha, " " * (10 - len(asiento.fecha)),
              "| ", asiento.cuentas[0].get("cuenta"), " " * (5 - len(asiento.cuentas[0].get("cuenta"))),
              "| ", asiento.cuentas[0].get("display"), " " * (40 - len(asiento.cuentas[0].get("display"))),
              "| ", asiento.cuentas[0].get("valor"), " " * (10 - len((asiento.cuentas[0].get("valor")))),
              "| ", "", " " * (10), "|")

        for cuenta in asiento.cuentas:

            if cuenta == asiento.cuentas[0]: continue

            if cuenta.get("debe_o_haber") == "1":
                print("| ", "", " " * (10),
                      "| ", cuenta.get("cuenta"), " " * (5 - len(asiento.cuentas[0].get("cuenta"))),
                      "| ", cuenta.get("display"), " " * (40 - len(cuenta.get("display"))),
                      "| ", cuenta.get("valor"), " " * (10 - len((cuenta.get("valor")))),
                      "| ", "", " " * (10), "|")

        for cuenta in asiento.cuentas:

            if cuenta == asiento.cuentas[0]: continue

            if cuenta.get("debe_o_haber") == "2":
                print("| ", "", " " * (10),
                      "| ", cuenta.get("cuenta"), " " * (5 - len(asiento.cuentas[0].get("cuenta"))),
                      "| ", "    " + cuenta.get("display"), " " * (40 - (len((cuenta.get("display"))) + len("    "))),
                      "| ", "", " " * (10),
                      "| ", cuenta.get("valor"), " " * (10 - len((cuenta.get("valor")))), "|")

        print("| ", "", " " * (10),
              "| ", "", " " * (5),
              "| ", asiento.segun_display, " " * (40 - (len(asiento.segun_display))),
              "| ", "", " " * (10),
              "| ", "", " " * (10), "|")

    total_debe = 0
    total_haber = 0
    for cuenta in list(cuentas_list.values()):
        cuenta.calc_totals()
        total_debe += cuenta.debe
        total_haber += cuenta.haber

    print("|", "-" * 97, "|")

    print(
        "| ", "", " " * (10),
        "| ", "", " " * (5),
        "| ", "Total", " " * (40 - len("Total")),
        "| ", str(total_debe), " " * (10 - len(str(total_debe))),
        "| ", str(total_haber), " " * (10 - len(str(total_haber))), "|"
        )

    print("|", "-" * 97, "|")

def display_libro_mayor(libro):

    for cuenta in list(cuentas_list.values()):

        if cuenta.debe == 0 and cuenta.haber == 0: continue

        debe_used = []
        haber_used = []

        for use in cuenta.used:

            if use.get("debe_o_haber") == "1":

                debe_used.append(str(use.get("number")) + ": " + str(use.get("valor")))

            elif use.get("debe_o_haber") == "2":

                haber_used.append(str(use.get("number")) + ": " + str(use.get("valor")))

        while len(debe_used) < 6:

            debe_used.append("")

        while len(haber_used) < 6:

            haber_used.append("")

        if cuenta.saldo_tipo != "Cuenta Saldada":

            print(

                "\n\n\n| ", cuenta.name, "({})".format(cuenta.number),
                " " * (36 - len(cuenta.name) - len(cuenta.number) + 2), "|",

                "\n|", "-" * 41, "|",

                "\n| ", "Debe", " " * (19 - len("debe")), "| ", "Haber", " " * (19 - len("haber")), "|",

                "\n|", "-" * 41, "|",


                "\n| ", "{}".format(debe_used[0]), " " * (19 - len("{}".format(debe_used[0]))), "| ",
                "{}".format(haber_used[0]), " " * (19 - len("{}".format(haber_used[0]))), "|",

                "\n| ", "{}".format(debe_used[1]), " " * (19 - len("{}".format(debe_used[1]))), "| ",
                "{}".format(haber_used[1]), " " * (19 - len("{}".format(haber_used[1]))), "|",

                "\n| ", "{}".format(debe_used[2]), " " * (19 - len("{}".format(debe_used[2]))), "| ",
                "{}".format(haber_used[2]), " " * (19 - len("{}".format(haber_used[2]))), "|",

                "\n| ", "{}".format(debe_used[3]), " " * (19 - len("{}".format(debe_used[3]))), "| ",
                "{}".format(haber_used[3]), " " * (19 - len("{}".format(haber_used[3]))), "|",

                "\n| ", "{}".format(debe_used[4]), " " * (19 - len("{}".format(debe_used[4]))), "| ",
                "{}".format(haber_used[4]), " " * (19 - len("{}".format(haber_used[4]))), "|",

                "\n| ", "{}".format(debe_used[5]), " " * (19 - len("{}".format(debe_used[5]))), "| ",
                "{}".format(haber_used[5]), " " * (19 - len("{}".format(haber_used[5]))), "|",

                "\n|", "-" * 41, "|",

                "\n| ", "{}".format(cuenta.debe), " " * (19 - len("{}".format(cuenta.debe))), "| ",
                "{}".format(cuenta.haber), " " * (19 - len("{}".format(cuenta.haber))), "|",

                "\n|", "-" * 41, "|",

                "\n| ", cuenta.saldo_tipo, ": {}".format(cuenta.saldo_valor),
                " " * (38 - len(cuenta.saldo_tipo) - len(str(cuenta.saldo_valor))), "|",

                "\n|", "-" * 41, "|",

                sep=""
            )

        else:

            print(

                "\n\n\n| ", cuenta.name, "({})".format(cuenta.number),
                " " * (36 - len(cuenta.name) - len(cuenta.number) + 2), "|",

                "\n|", "-" * 41, "|",

                "\n| ", "Debe", " " * (19 - len("debe")), "| ", "Haber", " " * (19 - len("haber")), "|",

                "\n|", "-" * 41, "|",

                "\n| ", "{}".format(debe_used[0]), " " * (19 - len("{}".format(debe_used[0]))), "| ",
                "{}".format(haber_used[0]), " " * (19 - len("{}".format(haber_used[0]))), "|",

                "\n| ", "{}".format(debe_used[1]), " " * (19 - len("{}".format(debe_used[1]))), "| ",
                "{}".format(haber_used[1]), " " * (19 - len("{}".format(haber_used[1]))), "|",

                "\n| ", "{}".format(debe_used[2]), " " * (19 - len("{}".format(debe_used[2]))), "| ",
                "{}".format(haber_used[2]), " " * (19 - len("{}".format(haber_used[2]))), "|",

                "\n| ", "{}".format(debe_used[3]), " " * (19 - len("{}".format(debe_used[3]))), "| ",
                "{}".format(haber_used[3]), " " * (19 - len("{}".format(haber_used[3]))), "|",

                "\n| ", "{}".format(debe_used[4]), " " * (19 - len("{}".format(debe_used[4]))), "| ",
                "{}".format(haber_used[4]), " " * (19 - len("{}".format(haber_used[4]))), "|",

                "\n| ", "{}".format(debe_used[5]), " " * (19 - len("{}".format(debe_used[5]))), "| ",
                "{}".format(haber_used[5]), " " * (19 - len("{}".format(haber_used[5]))), "|",

                "\n|", "-" * 41, "|",

                "\n| ", "{}".format(cuenta.debe), " " * (19 - len("{}".format(cuenta.debe))), "| ",
                "{}".format(cuenta.haber), " " * (19 - len("{}".format(cuenta.haber))), "|",

                "\n|", "-" * 41, "|",

                "\n| ", cuenta.saldo_tipo, "",
                " " * (40 - len(cuenta.saldo_tipo)), "|",

                "\n|", "-" * 41, "|",

                sep=""
            )

def display_balance(libro):

    debe_total = 0
    haber_total = 0
    deudor_total = 0
    acreedor_total = 0

    print(
        "\n\n| ", "N°", " " * (5 - len("N°")),
        "| ", "Cuenta", " " * (40 - len("Cuenta")),
        "| ", "          Sumas", " " * (25 - len(("          Sumas"))),
        "| ", "         Saldos", " " * (25 - len("         Saldos")), "|"
    )

    print(
        "| ", "", " " * (5 - len("")),
        "| ", "", " " * (40 - len("")),
        "| ", "Debe", " " * (10 - len(("Debe"))),
        "| ", "Haber", " " * (10 - len("Haber")),
        "| ", "Deudor", " " * (10 - len(("Deudor"))),
        "| ", "Acreedor", " " * (10 - len("Acreedor")), "|"
    )

    print("|", "-" * 112, "|")

    for cuenta in list(cuentas_list.values()):

        if cuenta.debe == 0 and cuenta.haber == 0: continue

        debe_total += cuenta.debe
        haber_total += cuenta.haber

        cuenta.debe_display, cuenta.haber_display = cuenta.debe, cuenta.haber

        if cuenta.debe == 0: cuenta.debe_display = "    --    "
        if cuenta.haber == 0: cuenta.haber_display = "    --    "

        if cuenta.saldo_tipo == "Saldo Deudor":

            deudor_total += cuenta.saldo_valor

            print(
                "| ", cuenta.number, " " * (5 - len(cuenta.number)),
                "| ", cuenta.name, " " * (40 - len(cuenta.name)),
                "| ", cuenta.debe_display, " " * (10 - len(str(cuenta.debe_display))),
                "| ", cuenta.haber_display, " " * (10 - len(str(cuenta.haber_display))),
                "| ", str(cuenta.saldo_valor), " " * (10 - len(str(cuenta.saldo_valor))),
                "| ", "    --    ", " " * (10 - len("    --    ")), "|"
            )

        elif cuenta.saldo_tipo == "Saldo Acreedor":

            acreedor_total += cuenta.saldo_valor

            print(
                "| ", cuenta.number, " " * (5 - len(cuenta.number)),
                "| ", cuenta.name, " " * (40 - len(cuenta.name)),
                "| ", cuenta.debe_display, " " * (10 - len(str(cuenta.debe_display))),
                "| ", cuenta.haber_display, " " * (10 - len(str(cuenta.haber_display))),
                "| ", "    --    ", " " * (10 - len("    --    ")),
                "| ", str(cuenta.saldo_valor), " " * (10 - len(str(cuenta.saldo_valor))), "|"
            )

        elif cuenta.saldo_tipo == "Cuenta Saldada":

            print(
                "| ", cuenta.number, " " * (5 - len(cuenta.number)),
                "| ", cuenta.name, " " * (40 - len(cuenta.name)),
                "| ", cuenta.debe_display, " " * (10 - len(str(cuenta.debe_display))),
                "| ", cuenta.haber_display, " " * (10 - len(str(cuenta.haber_display))),
                "| ", "    --    ", " " * (10 - len("    --    ")),
                "| ", "    --    ", " " * (10 - len("    --    ")), "|"
            )



    print("|", "-" * 112, "|")

    print(
        "| ", "", " " * (5),
        "| ", "Total", " " * (40 - len("Total")),
        "| ", debe_total, " " * (10 - len(str(debe_total))),
        "| ", haber_total, " " * (10 - len(str(haber_total))),
        "| ", deudor_total, " " * (10 - len(str(deudor_total))),
        "| ", acreedor_total, " " * (10 - len(str(acreedor_total))), "|"
    )

    print("|", "-" * 112, "|")

def main():

    print("AlfaBOOK Edicion Consola\n",
          __version__)
    load_plan()

    while True:

        start = input(
        "Que desea hacer? \n"
        "1 = Nuevo archivo \n"
        "2 = Cargar archivo\n"
        "> "
        )
        while start != "1" and start != "2":
            start = input(
                "Que desea hacer? \n"
                "1 = Nuevo archivo \n"
                "2 = Cargar archivo\n"
                "> "
            )

        if start == "1":
            new()

        if start == "2":
            load()

main()

#load_plan()
#libro = Libro_Diario()
#asiento1 = Asiento(1)
#asiento2 = Asiento(2)
#asiento3 = Asiento(3)
#asiento4 = Asiento(4)
#asiento5 = Asiento(5)
#asiento6 = Asiento(6)
#
#asiento1.set_fecha("01/11")
#asiento1.set_segun("0")
#asiento1.add_cuenta("1.02","1","45000")
#asiento1.add_cuenta("1.10","1","16000")
#asiento1.add_cuenta("1.12","1","40000")
#asiento1.add_cuenta("1.01","1","25000")
#asiento1.add_cuenta("2.02","2","6500")
#asiento1.add_cuenta("4.01","2","119500")
#
#asiento2.set_fecha("03/11")
#asiento2.set_segun("2")
#asiento2.add_cuenta("1.14","1","3325")
#asiento2.add_cuenta("4.04","1","175")
#asiento2.add_cuenta("1.10","2","3500")
#
#asiento3.set_fecha("03/11")
#asiento3.set_segun("1")
#asiento3.add_cuenta("4.06","1","600")
#asiento3.add_cuenta("1.01","2","600")
#
#asiento4.set_fecha("04/11")
#asiento4.set_segun("1")
#asiento4.add_cuenta("1.10","1","5700")
#asiento4.add_cuenta("4.08","1","164")
#asiento4.add_cuenta("2.02","2","5864")
#
#asiento5.set_fecha("07/11")
#asiento5.set_segun("3")
#asiento5.add_cuenta("2.02","1","6500")
#asiento5.add_cuenta("1.02","2","6500")
#
#asiento6.set_fecha("08/11")
#asiento6.set_segun("5")
#asiento6.add_cuenta("1.15","1","13325")
#asiento6.add_cuenta("1.02","2","10000")
#asiento6.add_cuenta("1.14","2","3325")
#
#libro.add_asiento(asiento1)
#libro.add_asiento(asiento2)
#libro.add_asiento(asiento3)
#libro.add_asiento(asiento4)
#libro.add_asiento(asiento5)
#libro.add_asiento(asiento6)
#display_libro_diario(libro)
#display_libro_mayor(libro)
#display_balance(libro)

"""

|  Fecha       |  N°     |  Detalle                                   |  Debe        |  Haber       |
|              |         |  -------------------1--------------------  |              |              |
|  01/11       |  1.02   |  Caja(A+)                                  |  45000       |              |
|              |  1.10   |  Mercaderias(A+)                           |  16000       |              |
|              |  1.12   |  Rodados(A+)                               |  40000       |              |
|              |  1.01   |  BANCO "Comafi" Cta. Cte.(A+)              |  25000       |              |
|              |  2.02   |      Documentos a pagar(P+)                |              |  6500        |
|              |  4.01   |      Alquileres perdidos(R.N.)             |              |  119500      |
|              |         |  Segun Inventario Inicial                  |              |              |
|              |         |  -------------------2--------------------  |              |              |
|  03/11       |  1.14   |  Valores a depositar(A+)                   |  3325        |              |
|              |  4.04   |  Descuentos cedidos(R.N.)                  |  175         |              |
|              |  1.10   |      Mercaderias(A-)                       |              |  3500        |
|              |         |  Segun Factura Duplicado                   |              |              |
|              |         |  -------------------3--------------------  |              |              |
|  03/11       |  4.06   |  Gastos generales(R.N.)                    |  600         |              |
|              |  1.01   |      BANCO "Comafi" Cta. Cte.(A-)          |              |  600         |
|              |         |  Segun Factura Original                    |              |              |
|              |         |  -------------------4--------------------  |              |              |
|  04/11       |  1.10   |  Mercaderias(A+)                           |  5700        |              |
|              |  4.08   |  Intereses perdidos(R.N.)                  |  164         |              |
|              |  2.02   |      Documentos a pagar(P+)                |              |  5864        |
|              |         |  Segun Factura Original                    |              |              |
|              |         |  -------------------5--------------------  |              |              |
|  07/11       |  2.02   |  Documentos a pagar(P-)                    |  6500        |              |
|              |  1.02   |      Caja(A-)                              |              |  6500        |
|              |         |  Segun Recibo Original                     |              |              |
|              |         |  -------------------6--------------------  |              |              |
|  08/11       |  1.15   |  BANCO "Zurich" Cta. Cte.(A+)              |  13325       |              |
|              |  1.02   |      Caja(A-)                              |              |  10000       |
|              |  1.14   |      Valores a depositar(A-)               |              |  3325        |
|              |         |  Segun Boleta de Deposito                  |              |              |
|              |         |  Total                                     |  155789      |  155789      |


"""

"""
| Caja(1.02)                              |
|-----------------------------------------|
| Debe               | Haber              |
|-----------------------------------------|
| 1: 45000           | 5: 6500            |
|                    | 6: 10000           |
|                    |                    |
|                    |                    |
|                    |                    |
|                    |                    |
|-----------------------------------------|
| 45000              | 16500              |
|-----------------------------------------|
| Saldo Deudor: 28500                     |
|-----------------------------------------|
"""

"""

|  N°     |  Cuenta                                    |            Sumas            |           Saldos            |
|         |                                            |  Debe        |  Haber       |  Deudor      |  Acreedor    |
| ---------------------------------------------------------------------------------------------------------------- |
|  1.01   |  BANCO "Comafi" Cta. Cte.                  |  25000       |  600         |  24400       |      --      |
|  1.02   |  Caja                                      |  45000       |  16500       |  28500       |      --      |
|  1.10   |  Mercaderias                               |  21700       |  3500        |  18200       |      --      |
|  1.12   |  Rodados                                   |  40000       |      --      |  40000       |      --      |
|  1.14   |  Valores a depositar                       |  3325        |  3325        |      --      |      --      |
|  1.15   |  BANCO "Zurich" Cta. Cte.                  |  13325       |      --      |  13325       |      --      |
|  2.02   |  Documentos a pagar                        |  6500        |  12364       |      --      |  5864        |
|  4.01   |  Alquileres perdidos                       |      --      |  119500      |      --      |  119500      |
|  4.04   |  Descuentos cedidos                        |  175         |      --      |  175         |      --      |
|  4.06   |  Gastos generales                          |  600         |      --      |  600         |      --      |
|  4.08   |  Intereses perdidos                        |  164         |      --      |  164         |      --      |
| ---------------------------------------------------------------------------------------------------------------- |
|         |  Total                                     |  155789      |  155789      |  125364      |  125364      |
| ---------------------------------------------------------------------------------------------------------------- |

"""