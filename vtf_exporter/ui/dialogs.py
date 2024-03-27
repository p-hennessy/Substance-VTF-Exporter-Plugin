import sd 
from PySide2 import QtWidgets 
from PySide2 import QtCore, QtWidgets, QtUiTools
from PySide2.QtWidgets import QApplication, QFileDialog


def get_directory(prompt="Select a folder"):
    directory = QFileDialog.getExistingDirectory(None, prompt)
    return directory


def notify(msgbox_type, message):
    app = sd.getContext().getSDApplication() 
    uiMgr = app.getQtForPythonUIMgr() 
    mainWindow = uiMgr.getMainWindow() 

    dialog = msgbox_type(mainWindow, "VTF Exporter", message)
    dialog.show()


def critical(message):
    notify(QtWidgets.QMessageBox.critical, message)


def informational(message):
    notify(QtWidgets.QMessageBox.informational, message)


def warning(message):
    notify(QtWidgets.QMessageBox.warning, message)
