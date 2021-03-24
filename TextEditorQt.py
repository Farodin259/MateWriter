from PySide6.QtWidgets import QApplication
from TextEditorUI import Ui_MainWindow, QFont, QMainWindow  # импорт нашего сгенерированного файла
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Roboto", 10, QFont.Normal))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())