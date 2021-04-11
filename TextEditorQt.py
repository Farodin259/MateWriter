# pyside6-uic test.ui -o TextEditorUI.py
from PySide6 import QtGui
from TextEditorUI import *
from PySide6.QtWidgets import QApplication
from TextEditorUI import Ui_MainWindow, QMainWindow  # импорт нашего сгенерированного файла
from PySide6.QtCore import QSettings, QPoint, QSize
from Titlebar import FramelessWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.setupUi(self)
        self.curFile = ''
        self.setCurrentFile('')
        self.createStatusBar()

        self.textEdit.document().contentsChanged.connect(self.documentWasModified)

        self.setCurrentFile('')
        self.settings = QSettings('Matewriter', 'Matewriter')
        self.exit_action.triggered.connect(QApplication.quit)
        self.save_action.triggered.connect(self.save)
        self.open_action.triggered.connect(self.open)
        self.newfile_action.triggered.connect(self.newFile)
        self.saveas_action.triggered.connect(self.saveAs)
        self.open_action.setShortcut('Ctrl+O')
        self.newfile_action.setShortcut('Ctrl+N')
        self.save_action.setShortcut('Ctrl+S')
        # Конфиги окна
        windowScreenGeometry = self.settings.value("windowScreenGeometry")
        windowScreenState = self.settings.value("windowScreenState")
        if windowScreenGeometry:
            self.restoreGeometry(windowScreenGeometry)

        else:
            self.resize(600)

        if windowScreenState:
            self.restoreState(windowScreenState)

    def closeEvent(self, event):
        self.settings.setValue("windowScreenGeometry", self.saveGeometry())
        self.settings.setValue("windowScreenState", self.saveState())
        if self.maybeSave():
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    def newFile(self):
        if self.maybeSave():
            self.textEdit.clear()
            self.setCurrentFile('')

    def open(self):
        if self.maybeSave():
            fileName, _ = QFileDialog.getOpenFileName(self)
            if fileName:
                self.loadFile(fileName)

    def save(self):
        if self.curFile:
            return self.saveFile(self.curFile)

        return self.saveAs()

    def saveAs(self):
        fileName, _ = QFileDialog.getSaveFileName(self)
        if fileName:
            return self.saveFile(fileName)

        return False

    def documentWasModified(self):
        self.setWindowModified(self.textEdit.document().isModified())

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def readSettings(self):
        settings = QSettings("MateWriter")
        pos = settings.value("pos", QPoint(200, 200))
        size = settings.value("size", QSize(400, 400))
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        settings = QSettings("MateWriter")
        settings.setValue("pos", self.pos())
        settings.setValue("size", self.size())

    def maybeSave(self):
        if self.textEdit.document().isModified():
            ret = QMessageBox.warning(self, "MateWriter",
                                      "The document has been modified.\nDo you want to save "
                                      "your changes?",
                                      QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

            if ret == QMessageBox.Save:
                return self.save()

            if ret == QMessageBox.Cancel:
                return False

        return True

    def loadFile(self, fileName):
        file = QFile(fileName)
        if not file.open(QFile.ReadOnly | QFile.Text):
            QMessageBox.warning(self, "MateWriter",
                                "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            return

        inf = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.textEdit.setPlainText(inf.readAll())
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("File loaded", 2000)

    def saveFile(self, fileName):
        file = QFile(fileName)
        if not file.open(QFile.WriteOnly | QFile.Text):
            QMessageBox.warning(self, "MateWriter",
                                "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            return False

        outf = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        outf << self.textEdit.toPlainText()
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("File saved", 2000)
        return True

    def setCurrentFile(self, fileName):
        self.curFile = fileName
        self.textEdit.document().setModified(False)
        self.setWindowModified(False)

        if self.curFile:
            shownName = self.strippedName(self.curFile)
        else:
            shownName = 'untitled.txt'

        self.setWindowTitle(" %s[*] - MateWriter" % shownName)

    def strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    app.setStyleSheet('Titlebar.qss')
    w = FramelessWindow()

    w.setWindowTitle('Тестовая строка заголовка')
    w.setWindowIcon(QIcon('icon.ico'))

    #    w.setWidget(MainWindow(MainWindow))       # Добавить свое окно
    w.setWidget(MainWindow())  # !!!

    w.show()
    sys.exit(app.exec_())
