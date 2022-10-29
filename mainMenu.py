from PyQt5.QtWidgets import *
from PyQt5 import uic


class AppGUI(QMainWindow):
    def __init__(self):
        super(AppGUI, self).__init__()
        uic.loadUi("app.ui", self)
        self.show()

def main():
    app = QApplication([])
    window = AppGUI()
    app.exec_()

if __name__=='__main__':
    main()