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

class Asiento():

    def __init__(self):

        self.cuentas = []

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

            self.cuentas.append({
                "cuenta": cuenta,
                "cuenta_nombre": cuenta_nombre,
                "tipo": "pasivo",
                "debe_o_haber": debe_o_haber,
                "valor": valor
            })

        self.cuentas.append({
            "cuenta" : cuenta,
            "debe_o_haber" : debe_o_haber,
            "valor": valor
        })

    def set_fecha(self, fecha):

        self.fecha = fecha

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

        asiento.add_cuenta(cuenta,debe_o_haber,valor)

        continuar = input(
            "\n¿Que desea hacer?"
            "\n1 = Continuar otra cuenta"
            "\n2 = Continuar con el libro"
            "\n3 = Parar"
            "\n> "
        )

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
                    "\n3 = Parar"
                    "\n> "
                )

                asiento.add_cuenta(cuenta,debe_o_haber,valor)
                if continuar == "2" or continuar == "3": break

        libro.add_asiento(asiento)
        if continuar == "3": break

    display(libro)

def display(libro):
    print("| ", "Fecha", " " * (6 - len("fecha")), "| ", "Detalle", " " * (40 - len("detalle")), "| ", "Debe",
    " " * (10 - len(("debe"))), "| ", "Haber", " " * (10 - len("haber")), "|")

    for asiento in libro.asientos:

        print("| ", asiento.fecha, " " * (6 - len(asiento.fecha)),
              "| ", asiento.cuentas[0].get("display"), " " * (40 - len(asiento.cuentas[0].get("display"))),
              "| ", asiento.cuentas[0].get("valor"), " " * (10 - len((asiento.cuentas[0].get("valor")))),
              "| ", "", " " * (10), "|")

        for cuenta in asiento.cuentas:

            if cuenta.get("tipo") == "activo":
                print("|", asiento.fecha, " " * (6 - len(asiento.fecha)), "| ", asiento.cuentas[0].get("display"),
                      " " * (40 - len(asiento.cuentas[0].get("display"))), "| ", asiento.cuentas[0].get("valor"),
                      " " * (10 - len((asiento.cuentas[0].get("valor")))), "| ", "", " " * (10), "|")



print("AlfaBOOK Edicion Consola\n"
      "Version 1.0")

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
