import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Calculadora(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()

