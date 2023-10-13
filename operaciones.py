import math

class Operaciones:
    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def calcularDivision(self, num1, num2):
        if num2 == 0:
            return "No se puede dividir por cero"
        return num1 / num2
    
    def calcularMedia(self, num1, num2):
        med = (num1 + num2) / 2
        return med
    
    def calcularMax(self, num1, num2):
        if num1 > num2:
            max = num1
        elif num1 < num2:
            max = num2
        elif num1 == num2:
            max = num1
        return max
    
    def calcularMin(self, num1, num2):
        if num1 > num2:
            min = num2
        elif num1 < num2:
            min = num1
        elif num1 == num2:
            min = num1
        return min
    
    def calcularSeno(self,num1):
        if num1 % 180 == 0:  # Verifica si el ángulo es un múltiplo de 180 grados
            return 0
        sen = math.sin(math.radians(num1))
        seno = round(sen, 6)
        if sen == 1.0:
            seno = 1
        elif sen == -1.0:
            seno = -1
        return seno
    
    
    def calcularCoseno(self,num1):
        if num1 % 90 == 0 and num1 % 180 != 0:  # Verifica si el ángulo es un múltiplo de 90 pero no de 180
            return 0
        cos = math.cos(math.radians(num1))
        coseno = round(cos, 6)
        if cos == 1.0:
            coseno = 1
        elif cos == -1.0:
            coseno = -1
        return coseno

    
    
    def calcularTangente(self,num1):
        if num1 % 90 == 0 and num1 % 180 != 0:  # Verifica si el ángulo es un múltiplo de 90 pero no de 180
            return "Tangente no definida"
        elif num1 % 180 == 0:  # Verifica si el ángulo es un múltiplo de 180 grados
            return 0
        tan = math.tan(math.radians(num1))
        tangente = round(tan, 6)
        return tangente


    
