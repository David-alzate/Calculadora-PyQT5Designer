class ConversionNumero:
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    diez_a_diecinueve = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    def __init__(self, numero):
        self.numero = numero
    
    def convertir(self, numero=None):
        if numero is None:
            numero = self.numero

        if numero == 0:
            return "cero"

        if numero < 0:
            return "menos " + self.convertir(-numero)

        if numero < 10:
            return self.unidades[numero]

        if numero < 20:
            return self.diez_a_diecinueve[numero - 10]

        if numero < 100:
            return self.decenas[numero // 10] + (" y " + self.convertir(numero % 10) if numero % 10 > 0 else "")
        
        if numero == 100:
            return "cien"

        if numero < 1000:
            return self.centenas[numero // 100] + (" " + self.convertir(numero % 100) if numero % 100 > 0 else "")
        
        if numero == 1000:
            return "mil"

        if numero < 1000000:
            return self.convertir(numero // 1000) + " mil" + (" " + self.convertir(numero % 1000) if numero % 1000 > 0 else "")
        
        if numero == 1000000:
            return "un millón"

        if numero < 1000000000:
            return self.convertir(numero // 1000000) + " millones" + (" " + self.convertir(numero % 1000000) if numero % 1000000 > 0 else "")
        
        if numero == 1000000000:
            return "mil millones"
        
        if numero < 1000000000000:
            return self.convertir(numero // 1000000000) + " mil millones" + (" " + self.convertir(numero % 1000000000) if numero % 1000000000 > 0 else "")
        
        if numero == 1000000000000:
            return "un billón"
        
        if numero < 1000000000000000:
            return self.convertir(numero // 1000000000000) + " billones" + (" " + self.convertir(numero % 1000000000000) if numero % 1000000000000 > 0 else "")
        
        if numero == 1000000000000000:
            return "mil billones"
        
        if numero < 1000000000000000000:
            return self.convertir(numero // 1000000000000000) + " mil billones" + (" " + self.convertir(numero % 1000000000000000) if numero % 1000000000000000 > 0 else "")
        
        if numero == 1000000000000000000:
            return "un trillón"
        
        if numero < 1000000000000000000000:
            return self.convertir(numero // 1000000000000000000) + " trillones" + (" " + self.convertir(numero % 1000000000000000000) if numero % 1000000000000000000 > 0 else "")

        return "Número demasiado grande para ser convertido"


    
        
    def convertirDecimal(self, numero=None):
        if numero is None:
            numero = self.numero

        entero, decimal = str(numero).split(".")
        entero = int(entero)
        decimal = int(decimal)

        if entero == 0:
            return "cero coma " + self.convertir(decimal)

        if entero < 0:
            return "menos " + self.convertir_decimal(-numero)

        resultado = self.convertir(entero) + " coma " + self.convertir(decimal)
        return resultado
    


