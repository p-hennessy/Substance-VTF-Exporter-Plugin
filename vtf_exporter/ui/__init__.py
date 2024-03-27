import sd 
from PySide2 import QtWidgets 
from PySide2 import QtCore, QtWidgets, QtUiTools
from PySide2.QtWidgets import QApplication, QFileDialog


from vtf_exporter.ui import dialogs
from vtf_exporter.ui.event_handlers import * 

DOCK = None


def create_panel():
    global DOCK
    app = sd.getContext().getSDApplication() 
    ui_manager = app.getQtForPythonUIMgr() 
    DOCK = ui_manager.newDockWidget(identifier="vtf_exporter", title="VTF Exporter") 

    widget = load_ui_file("panel.ui", parent=DOCK) 
    load_global_settings(widget)   
    setup_event_handlers(ui_manager, widget)
    widget.show()


def destroy_panel():
    global DOCK
    DOCK.close()
    DOCK.parent().close()
    DOCK = None


def load_ui_file(filename, parent=None): 
    current_directory = os.path.dirname(__file__)
    path = os.path.join(current_directory, filename)
    
    loader = QtUiTools.QUiLoader() 
    uifile = QtCore.QFile(path) 
    uifile.open(QtCore.QFile.ReadOnly) 
    ui = loader.load(uifile, parent) 
    uifile.close() 
    return ui 


def load_global_settings(widget):
    global_config = config.get_global_config()
    vtex_location = global_config.get("vtex_location")

    widget.le_vtex_location.setText(vtex_location)


def setup_event_handlers(ui_manager, widget):
    widget.btn_vtex_location.clicked.connect(lambda: on_btn_vtex_location(widget))
    widget.btn_save_global_config.clicked.connect(lambda: on_btn_save_global_config(widget))
    widget.le_vtex_location.textEdited.connect(lambda: on_le_vtex_location(widget))
    
    widget.btn_export_location.clicked.connect(lambda: on_btn_export_location(widget))
    widget.btn_save_graph_config.clicked.connect(lambda: on_btn_save_graph_config(widget))
    widget.le_export_location.textEdited.connect(lambda: on_le_export_location(widget))

    widget.btn_export_graph_presets.clicked.connect(lambda: on_btn_export_graph_presets(widget))

    ui_manager.registerGraphViewCreatedCallback(lambda gid: on_graph_selected(widget))

