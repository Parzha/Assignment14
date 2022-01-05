from PySide6 import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from PySide6.QtUiTools import QUiLoader
from math import *
from sympy import *


class Calculator(QMainWindow):
    operationPressed = False
    firstValue = -1
    secondValue = -1
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("untitled.ui")
        self.ui.show()

        self.ui.zero.clicked.connect(self.onPressedDigit)
        self.ui.one.clicked.connect(self.onPressedDigit)
        self.ui.two.clicked.connect(self.onPressedDigit)
        self.ui.three.clicked.connect(self.onPressedDigit)
        self.ui.four.clicked.connect(self.onPressedDigit)
        self.ui.five.clicked.connect(self.onPressedDigit)
        self.ui.six.clicked.connect(self.onPressedDigit)
        self.ui.seven.clicked.connect(self.onPressedDigit)
        self.ui.eight.clicked.connect(self.onPressedDigit)
        self.ui.nine.clicked.connect(self.onPressedDigit)
        self.ui.dot.clicked.connect(self.onPressedDigit)

        self.ui.plus.clicked.connect(self.onPressedOperation)
        self.ui.minus.clicked.connect(self.onPressedOperation)
        self.ui.multi.clicked.connect(self.onPressedOperation)
        self.ui.div.clicked.connect(self.onPressedOperation)
        self.ui.mode.clicked.connect(self.onPressedOperation)
        self.ui.sqrt.clicked.connect(self.onPressedOperation)
        self.ui.log.clicked.connect(self.onPressedOperation)
        self.ui.negative.clicked.connect(self.onPressedOperation)




        self.ui.sin.clicked.connect(self.onPressedOperation)
        self.ui.cos.clicked.connect(self.onPressedOperation)
        self.ui.tan.clicked.connect(self.onPressedOperation)
        self.ui.cot.clicked.connect(self.onPressedOperation)


        self.ui.equal.clicked.connect(self.onPressedEquals)
        self.ui.clear.clicked.connect(self.onPressedClear)

    def onPressedDigit(self):
        button: QPushButton = self.sender()
        if self.ui.outputlabel.text() == "0" and self.operationPressed == False:
            self.ui.outputlabel.setText(button.text())

        elif self.operationPressed != False:

            if self.ui.outputlabel.text() == "0":
                self.ui.outputlabel.setText(button.text())
            else:
                self.ui.outputlabel.setText(self.ui.outputlabel.text() + button.text())

            self.secondValue = float(self.ui.outputlabel.text())

        else:
            self.ui.outputlabel.setText(self.ui.outputlabel.text() + button.text())

    def onPressedOperation(self):

        button: QPushButton = self.sender()
        if self.ui.outputlabel.text() != "0" and self.operationPressed == False:
            self.operationPressed = button.text()
            self.firstValue = float(self.ui.outputlabel.text())
            self.holder = float(self.ui.outputlabel.text())
            if self.operationPressed =="sin" or self.operationPressed =="cos" or self.operationPressed =="tan" or self.operationPressed =="cot" or self.operationPressed =="log":
                self.ui.outputlabel.setText(f"{self.operationPressed}({str(self.ui.outputlabel.text())})")
            elif self.operationPressed == "sqrt":
                self.ui.outputlabel.setText(f"{str(self.ui.outputlabel.text())}^2")
            elif self.operationPressed =="+/-":
                self.ui.outputlabel.setText(f"{str(self.firstValue)} * (-1) ")
            else:
                self.ui.outputlabel.setText("0")

        if self.ui.outputlabel.text() != "0" and self.operationPressed != False:
            result = -1

            if self.operationPressed == "+":
                result = self.firstValue + self.secondValue
            elif self.operationPressed == "-":
                result = self.firstValue - self.secondValue
            elif self.operationPressed == "*":
                result = self.firstValue * self.secondValue
            elif self.operationPressed == "/":
                result = self.firstValue / self.secondValue
            elif self.operationPressed == "%":
                result = (self.firstValue / 100) * self.secondValue
            elif self.operationPressed == "sin":
                result = sin(self.firstValue)
            elif self.operationPressed == "cos":
                result = cos(self.firstValue)
            elif self.operationPressed == "tan":
                result = tan(self.firstValue)
            elif self.operationPressed == "cot":
                result = cot(self.firstValue)
            elif self.operationPressed == "log":
                inted = int(self.firstValue)
                result = log(inted,10)
            elif self.operationPressed == "sqrt":
                result = pow(self.firstValue , 2)
            elif self.operationPressed == "+/-":
                result =self.firstValue * (-1)
                self.ui.outputlabel.setText(str((result)))

            self.firstValue = result
            if self.operationPressed =="sin" or self.operationPressed =="cos" or self.operationPressed =="tan" or self.operationPressed =="cot" or self.operationPressed=="log" or self.operationPressed =="sqrt" or self.operationPressed =="+/-":
                pass
            else:
                self.ui.outputlabel.setText("0")


    def onPressedEquals(self):

        if self.operationPressed == "+":
            self.ui.outputlabel.setText(str(self.firstValue + self.secondValue))
        elif self.operationPressed == "-":
            self.ui.outputlabel.setText(str(self.firstValue - self.secondValue))
        elif self.operationPressed == "*":
            self.ui.outputlabel.setText(str(self.firstValue * self.secondValue))
        elif self.operationPressed == "/":
            self.ui.outputlabel.setText(str(self.firstValue / self.secondValue))
        elif self.operationPressed == "%":
            self.ui.outputlabel.setText(str((self.firstValue / 100) * self.secondValue))
        elif self.operationPressed == "sin":
            self.ui.outputlabel.setText(str((self.firstValue)))
        elif self.operationPressed == "cos":
            self.ui.outputlabel.setText(str((self.firstValue)))
        elif self.operationPressed == "tan":
            self.ui.outputlabel.setText(str((self.firstValue)))
        elif self.operationPressed == "cot":
            self.ui.outputlabel.setText(str((self.firstValue)))
        elif self.operationPressed == "log":
            self.ui.outputlabel.setText(str((self.firstValue)))
        elif self.operationPressed == "sqrt":
            self.ui.outputlabel.setText(str((self.firstValue)))
        # elif self.operationPressed == "+/-":
        #     self.ui.outputlabel.setText(str((self.firstValue)))


        if self.operationPressed == "log":
            self.firstValue = int(self.ui.outputlabel.text())
        else:
            self.firstValue = float(self.ui.outputlabel.text())
        self.secondValue = -1

    def onPressedClear(self):
        self.ui.outputlabel.setText("0")
        self.operationPressed = False
        self.firstValue = -1


if __name__ == "__main__":
    app = QApplication()
    cal = Calculator()
    app.exec()




