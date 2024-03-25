import sd 
from PySide2 import QtWidgets

from vtf_exporter import config
from vtf_exporter.bulk_export import bulk_export


def create_menu():
    app = sd.getContext().getSDApplication() 
    uiMgr = app.getQtForPythonUIMgr() 
    
    menu = uiMgr.newMenu(
        menuTitle="VTF Exporter", 
        objectName="vtf_exporter_main"
    ) 

    act_bulk_export = QtWidgets.QAction("Bulk Export Graph Presets", menu) 
    act_bulk_export.triggered.connect(bulk_export) 
    menu.addAction(act_bulk_export)
    
    menu.addSeparator()

    configure = QtWidgets.QAction("Configure", menu) 
    configure.triggered.connect(create_config_dialog) 
    menu.addAction(configure)



def destroy_menu():
    app = sd.getContext().getSDApplication() 
    uiMgr = app.getQtForPythonUIMgr() 
    uiMgr.deleteMenu("vtf_exporter_main")


def create_config_dialog():
    app = sd.getContext().getSDApplication() 
    uiMgr = app.getQtForPythonUIMgr() 
    
    mainWindow = uiMgr.getMainWindow() 
    dialog = QtWidgets.QDialog(parent=mainWindow) 
    
    layout = QtWidgets.QVBoxLayout() 
    layout2 = QtWidgets.QHBoxLayout()

    label_vtex_location = QtWidgets.QLabel("vtex.exe")

    vtex_path = config.get_vtex_config_file().get("vtex_path")
    if vtex_path:
        txt_vtex_location = QtWidgets.QLineEdit(vtex_path)
    else:
        txt_vtex_location = QtWidgets.QLineEdit()

    layout2.addWidget(label_vtex_location) 
    layout2.addWidget(txt_vtex_location) 

    layout.addLayout(layout2)

    btn_save = QtWidgets.QPushButton("Save")
    def save_config():
        config_data = {"vtex_path": txt_vtex_location.text()}
        save_vtex_config_file(config_data)
        dialog.accept()

    btn_save.clicked.connect(save_config) 

    layout.addWidget(btn_save) 

    dialog.setLayout(layout) 
    
    dialog.show()