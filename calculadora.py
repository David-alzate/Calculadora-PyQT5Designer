from interfaz import *
import sys
from PyQt5.QtWidgets import QApplication

class Calculadora():
    def __init__(self):
        super().__init__()
        
    def EjecutarCalculadora(self):
        if __name__ == '__main__':
            app = QApplication(sys.argv)
            gui = GUI()
            gui.show()
            sys.exit(app.exec_())
    

main = Calculadora()
main.EjecutarCalculadora()