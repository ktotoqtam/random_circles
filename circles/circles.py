from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("circles.ui", self)

        self.btn.clicked.connect(self.clicked)

    def clicked(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        self.circle(qp)

        qp.end()

    def circle(self, qp):
        qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))

        radius = randint(10, 100)
        qp.drawEllipse(randint(0, 500), randint(0, 500), radius, radius)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
