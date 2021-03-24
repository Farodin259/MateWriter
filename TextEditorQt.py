from TextEditorUI import *
from PySide6.QtWidgets import QApplication
from TextEditorUI import Ui_MainWindow, QFont, QMainWindow, QAction  # импорт нашего сгенерированного файла
from PySide6.QtCore import QSettings, QPoint, QSize
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.settings = QSettings('My company', 'myApp')

        windowScreenGeometry = self.settings.value("windowScreenGeometry")
        windowScreenState = self.settings.value("windowScreenState")

        if windowScreenGeometry:
            self.restoreGeometry(windowScreenGeometry)

        else:
            self.resize(600, 400)

        if windowScreenState:
            self.restoreState(windowScreenState)

    def closeEvent(self, e):
        # Write window size and position to config file
        self.settings.setValue("windowScreenGeometry", self.saveGeometry())
        self.settings.setValue("windowScreenState", self.saveState())
        e.accept()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())