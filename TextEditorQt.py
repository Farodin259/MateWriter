# pyside6-uic TextEditor.ui -o TextEditorUI.py
from TextEditorUI import *
from PySide6.QtWidgets import QApplication
from TextEditorUI import Ui_MainWindow, QFont, QMainWindow, QAction  # импорт нашего сгенерированного файла
from PySide6.QtCore import QSettings, QPoint, QSize
import sys

file_path = None


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.settings = QSettings('My company', 'myApp')

        def new_file(e):
            if not self.textEdit.document().isModified():
                return
            answer = QMessageBox.question(
                window, None,
                "У вас есть носохраненные изменения. Сохранить перед закрытием?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
            )
            if answer & QMessageBox.Save:
                file_save()
            elif answer & QMessageBox.Cancel:
                e.ignore()

        def open_file():
            global file_path
            path = QFileDialog.getOpenFileName(window, "Open")[0]
            if path:
                self.textEdit.setPlainText(open(path).read())
                file_path = path

        def file_save():
            if file_path is None:
                save_as()
            else:
                with open(file_path, "w") as f:
                    f.write(self.textEdit.toPlainText())

                self.textEdit.document().setModified(False)

        def save_as():
            global file_path
            path = QFileDialog.getSaveFileName(window, "Save As")[0]
            if path:
                file_path = path
                file_save()

        self.exit_action.triggered.connect(QApplication.quit)
        self.save_action.triggered.connect(file_save)
        self.open_action.triggered.connect(open_file)
        self.newfile_action.triggered.connect(new_file)
        self.saveas_action.triggered.connect(save_as)
        self.open_action.setShortcut('Ctrl+O')
        self.newfile_action.setShortcut('Ctrl+N')
        self.save_action.setShortcut('Ctrl+S')
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
