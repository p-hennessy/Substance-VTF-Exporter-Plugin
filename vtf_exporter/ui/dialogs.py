import sd 
from PySide2 import QtWidgets 
from PySide2 import QtCore, QtWidgets, QtUiTools
from PySide2.QtWidgets import QApplication, QFileDialog


def get_directory(prompt="Select a folder"):
    directory = QFileDialog.getExistingDirectory(None, prompt)
    return directory


def notify(message):
    app = sd.getContext().getSDApplication() 
    uiMgr = app.getQtForPythonUIMgr() 
    mainWindow = uiMgr.getMainWindow() 

    dialog = QtWidgets.QMessageBox(parent=mainWindow)
    dialog.setWindowTitle("VTF Exporter")
    dialog.setText(message)
    dialog.show()