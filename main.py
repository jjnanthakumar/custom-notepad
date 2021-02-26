import sys, os
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QAction,
    QLabel,
    QPlainTextEdit,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QFileDialog,
    QMessageBox,
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFontDatabase, QIcon, QKeySequence
from PyQt5.QtPrintSupport import QPrintDialog


class Notepad(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Notepad 2.0")
        self.screen_width, self.screen_height = (
            self.geometry().width(),
            self.geometry().height(),
        )
        self.resize(self.screen_width, self.screen_height)
        self.setWindowIcon(QIcon("images/notepad.png"))
        self.show()

        self.filterTypes = "Text Document (*.txt);; Python (*.py);; Markdown (*.md)"
        self.path = None

        fixedFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedFont.setPointSize(12)
        mainlayout = QVBoxLayout()

        # Editor
        self.editor = QPlainTextEdit()
        self.editor.setFont(fixedFont)
        mainlayout.addWidget(self.editor)

        # statusBar
        self.statusBar = self.statusBar()

        # app container
        container = QWidget()
        container.setLayout(mainlayout)
        self.setCentralWidget(container)

        # File menus
        filemenu = self.menuBar().addMenu("&File")

        # file Toolbar
        file_toolbar = QToolBar()
        file_toolbar.setIconSize(QSize(30, 30))
        self.addToolBar(Qt.BottomToolBarArea, file_toolbar)
        self.update_title()
        """
        open, save, saveAs
        """
        file_open = self.create_action(
            self,
            "images/file_open1.png",
            "Open File",
            "Open File",
            QKeySequence.Open,
            self.file_open,
        )
        file_save = self.create_action(
            self,
            "images/file_save1.png",
            "Save",
            "Save File",
            QKeySequence.Save,
            self.file_save,
        )
        file_saveas = self.create_action(
            self,
            "images/file_saveas1.png",
            "Save As",
            "Save As",
            QKeySequence.SaveAs,
            self.file_saveas,
        )
        file_print = self.create_action(
            self,
            "images/file_print1.png",
            "Print File",
            "Print File",
            QKeySequence.Print,
            self.file_print,
        )
        filemenu.addActions([file_open, file_save, file_saveas, file_print])
        file_toolbar.addActions([file_open, file_save, file_saveas, file_print])
    def file_save(self):
        if self.path is None:
            self.file_saveas()
        else:
            try:
                text= self.editor.toPlainText()
                with open(self.path,'w') as f:
                    f.write(text)
                self.dialog_message(f'File saved succesfully at {self.path}', QMessageBox.Information)
            except Exception as e:
                self.dialog_message(e, QMessageBox.Critical)
            else:
                pass
    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            'Save File',
            '',
            self.filterTypes
        )
        text= self.editor.toPlainText()
        try:
            with open(path,'w') as f:
                f.write(text)
            self.dialog_message(f'File saved succesfully at {path}', QMessageBox.Information)
        except Exception as e:
            self.dialog_message(e, QMessageBox.Critical)
        else:
            self.path=path
            self.update_title()


    def file_open(self):
        path,_=QFileDialog.getOpenFileName(
            self,
            caption='Open File',
            directory='',
            filter=self.filterTypes
        )
        if path:
            try:
                with open(path, 'r') as f:
                    text=f.read()
            except Exception as e:
                self.dialog_message(str(e))
            else:
                self.path= path
                self.editor.setPlainText(text)
                self.update_title()
                self.editor.update()
    def file_print(self):
        printDlg= QPrintDialog()
        if printDlg.exec_():
            self.editor.print(printDlg.printer())
        pass
    def update_title(self):
        self.setWindowTitle('{} - Notepad 2.0'.format(os.path.basename(self.path) if self.path is not None else 'Unititled'))
    
    def dialog_message(self, message,type):
        dlg = QMessageBox(self)
        dlg.setText(message)
        dlg.setIcon(type)
        dlg.show()

    def create_action(
        self, parent, icon, action_name, status_tip, shortcut, triggered_method
    ):
        action = QAction(QIcon(icon), action_name, parent)
        action.setStatusTip(status_tip)
        action.triggered.connect(triggered_method)
        action.setShortcut(shortcut)
        return action

    def save_file(self):
        pass


app = QApplication(sys.argv)
notepad = Notepad()
sys.exit(app.exec_())