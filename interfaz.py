from operaciones import *
from Conversion import *
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets

   

class GUI(QMainWindow, Operaciones,ConversionNumero):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz.ui", self)
        self.num1 = 0  # Variable para almacenar el primer número
        self.operador = ""  # Variable para almacenar el operador
        self.btnPequeno.hide()
   
        # Conecta los botones numéricos
        self.btn0.clicked.connect(self.cero)
        self.btn1.clicked.connect(self.uno)
        self.btn2.clicked.connect(self.dos)
        self.btn3.clicked.connect(self.tres)
        self.btn4.clicked.connect(self.cuatro)
        self.btn5.clicked.connect(self.cinco)
        self.btn6.clicked.connect(self.seis)
        self.btn7.clicked.connect(self.siete)
        self.btn8.clicked.connect(self.ocho)
        self.btn9.clicked.connect(self.nueve)

        # Conecta los botones de operadores
        self.btnMas.clicked.connect(self.mas)
        self.btnMenos.clicked.connect(self.menos)
        self.btnDividir.clicked.connect(self.dividir)
        self.btnProducto.clicked.connect(self.producto)

        # Otros botones y operaciones
        self.btnSigno.clicked.connect(self.signo)
        self.btnSen.clicked.connect(self.sen)
        self.btnCos.clicked.connect(self.cos)
        self.btnTan.clicked.connect(self.tan)
        self.btnMax.clicked.connect(self.max)
        self.btnMin.clicked.connect(self.min)
        self.btnMedia.clicked.connect(self.media)
        self.btnIgual.clicked.connect(self.igual)
        self.btnBorrar.clicked.connect(self.borrar)

        #Control de barra de titulos
        self.btnCerrar.clicked.connect(lambda: self.close())
        self.btnGrande.clicked.connect(self.crontrolBtGrande)
        self.btnPequeno.clicked.connect(self.crontrolBtPequeno)
        self.btnMinimizar.clicked.connect(self.crontrolBtMinimizar)

        # Eliminar Barra de titulo y opacidad
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        

        #Redimensionar ventana
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
   
        # Mover Ventana 
        self.frameSuperior.mouseMoveEvent = self.moverVentana


    def cero(self):
      text = self.labelResultado1.text()
      if (len(self.labelResultado1.text()) < 10):
         self.labelResultado1.setText(text + "0")

      
    def uno(self):
      text = self.labelResultado1.text()
      if (len(self.labelResultado1.text()) < 10):
         self.labelResultado1.setText(text + "1")

    def dos(self):
      text = self.labelResultado1.text()
      if (len(self.labelResultado1.text()) < 10):
          self.labelResultado1.setText(text + "2")

    def tres(self):
      text = self.labelResultado1.text()
      if (len(self.labelResultado1.text()) < 10):
         self.labelResultado1.setText(text + "3")

    def cuatro(self):
      text = self.labelResultado1.text()
      if (len(self.labelResultado1.text()) < 10):
          self.labelResultado1.setText(text + "4")

    def cinco(self):
      text = self.labelResultado1.text()
      if (len(self.labelResultado1.text()) < 10):
          self.labelResultado1.setText(text + "5")
    
    def seis(self):
      text = self.labelResultado1.text()
      if (len(self.labelResultado1.text()) < 10):
         self.labelResultado1.setText(text + "6")

    def siete(self):
      text = self.labelResultado1.text()
      if (len(self.labelResultado1.text()) < 10):
         self.labelResultado1.setText(text + "7")

    def ocho(self):
      text = self.labelResultado1.text()
      if (len(self.labelResultado1.text()) < 10):
         self.labelResultado1.setText(text + "8")

    def nueve(self):
      text = self.labelResultado1.text()
      if (len(self.labelResultado1.text()) < 10):
         self.labelResultado1.setText(text + "9")

    def signo(self):
      text = self.labelResultado1.text()
      if text:
         if ((self.labelResultado1.text())[0] != "-"):
            self.labelResultado1.setText("-" + text)
      else:
         self.labelResultado1.setText("-" + text)


    def sen(self):
       try:
          text = self.labelResultado1.text()
          if text:
             self.num1 = int(text)
             self.operador = "sen"
             self.labelResultado1.setText("seno" + text)
          else:
             pass
       except:
         pass
      
    def cos(self):
      try:
         text = self.labelResultado1.text()
         if text:
             self.num1 = int(text)
             self.operador = "cos"
             self.labelResultado1.setText("cos" + text)
         else:
             pass
      except:
         pass

    def tan(self):
       try:
            text = self.labelResultado1.text()
            if text:
               self.num1 = int(text)
               self.operador = "tan"
               self.labelResultado1.setText("tan" + text)
            else:
               pass
       except:
          pass
    
    
    def max(self):
      try:
         text = self.labelResultado1.text()
         if text:
             self.num1 = int(text)  # Almacena el primer número
             self.operador = ">"  # Establece el operador
             self.labelResultado1.clear()
         else:
             pass
      except:
         pass
    
    def min(self):
      try:
        text = self.labelResultado1.text()
        if text:
            self.num1 = int(text)  # Almacena el primer número
            self.operador = "<"  # Establece el operador
            self.labelResultado1.clear()
        else:
            pass
      except:
         pass
    
    def media(self):
      try:
        text = self.labelResultado1.text()
        if text:
            self.num1 = int(text)  # Almacena el primer número
            self.operador = "X"  # Establece el operador
            self.labelResultado1.clear()
        else:
            pass
      except:
         pass

    def borrar(self):
      self.labelResultado1.clear()
      self.labelResultado2.clear()
      self.num1 = 0
      self.num2 = 0
      self.operador = ""

    def mas(self):
        try:
          text = self.labelResultado1.text()
          if text:
             self.num1 = int(text)  # Almacena el primer número
             self.operador = "+"  # Establece el operador
             self.labelResultado1.clear()
          else:
             pass
        except:
           pass

    def menos(self):
        try:
          text = self.labelResultado1.text()
          if text:
             self.num1 = int(text)  # Almacena el primer número
             self.operador = "-"  # Establece el operador
             self.labelResultado1.clear()
          else:
             pass
        except:
           pass

    def dividir(self):
        try:
          text = self.labelResultado1.text()
          if text:
             self.num1 = int(text)  # Almacena el primer número
             self.operador = "/"  # Establece el operador
             self.labelResultado1.clear()
          else:
             pass
        except:
           pass

    def producto(self):
        try:
          text = self.labelResultado1.text()
          if text:
             self.num1 = int(text)  # Almacena el primer número
             self.operador = "*"  # Establece el operador
             self.labelResultado1.clear()
          else:
             pass
        except:
           pass
        

    def igual(self):
      try:
           if self.operador == "sen":
              resultado = self.calcularSeno(self.num1)
           elif self.operador == "cos":
              resultado = self.calcularCoseno(self.num1)
           elif self.operador == "tan":
              resultado = self.calcularTangente(self.num1)
           self.labelResultado1.setText(str(resultado))
           if isinstance(resultado, int):
               convertidor = ConversionNumero(resultado)
               texto = convertidor.convertir()
               self.labelResultado2.setText(str(texto))
           else:
               convertidor = ConversionNumero(resultado)
               texto = convertidor.convertirDecimal()
               self.labelResultado2.setText(str(texto))
         
      except:  
         pass
         
      try:
         text = self.labelResultado1.text()
         if text:
            self.num2 = int(text)  # Obtiene el segundo número
            if self.operador == "+":
               resultado = self.sumar(self.num1, self.num2)
            elif self.operador == "-":
               resultado = self.restar(self.num1, self.num2)
            elif self.operador == "*":
               resultado = self.multiplicar(self.num1, self.num2)
            elif self.operador == "/":
               resultado = self.calcularDivision(self.num1, self.num2)
            elif self.operador == "X":
               resultado = self.calcularMedia(self.num1, self.num2)
            elif self.operador == ">":
               resultado = self.calcularMax(self.num1, self.num2)
            elif self.operador == "<":
               resultado = self.calcularMin(self.num1, self.num2)
            self.labelResultado1.setText(str(resultado))
            if isinstance(resultado, int):
               convertidor = ConversionNumero(resultado)
               texto = convertidor.convertir()
               self.labelResultado2.setText(str(texto))
            else:
               convertidor = ConversionNumero(resultado)
               texto = convertidor.convertirDecimal()
               self.labelResultado2.setText(str(texto))
         else:
             pass
      except:
         pass

        

    # Otros metodos 
    # Control de barra de titulo
    def crontrolBtMinimizar(self):
       self.showMinimized()

    def crontrolBtPequeno(self):
       self.showNormal()
       self.btnPequeno.hide()
       self.btnGrande.show()
      
    def crontrolBtGrande(self):
       self.showMaximized()
       self.btnGrande.hide()  
       self.btnPequeno.show()
    
    # Redimensionar ventana 
    def resizeEvent(self, event):
       rect = self.rect()
       self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # Mover ventana 
    def mousePressEvent(self, event):
       self.clickPosition = event.globalPos()

    def moverVentana(self, event):
       if self.isMaximized() == False:
          if event.buttons() == QtCore.Qt.LeftButton:
             self.move(self.pos() + event.globalPos() - self.clickPosition)
             self.clickPosition = event.globalPos()
             event.accept()
       if event.globalPos().y() <= 10:
          self.showMaximized()
          self.btnGrande.hide()
          self.btnPequeno.show()
       else:
          self.showNormal()
          self.btnPequeno.hide()
          self.btnGrande.show()

