from TextEditorUI import *
from PySide6.QtWidgets import QApplication
from TextEditorUI import Ui_MainWindow, QFont, QMainWindow, QAction  # импорт нашего сгенерированного файла
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())