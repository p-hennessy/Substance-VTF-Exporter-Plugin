import os
import pathlib

from vtf_exporter.ui import dialogs
from vtf_exporter import config
from vtf_exporter import utils

from vtf_exporter.actions import export_presets


def on_graph_selected(widget):
    graph_uuid = utils.get_graph_uuid()
    graph_config = config.get_graph_config(graph_uuid)

    # TODO Error checking
    if graph_config:
       widget.le_export_location.setText(graph_config.get("export_location"))
    else:
        widget.le_export_location.setText("")


def on_btn_vtex_location(widget):
    directory = dialogs.get_directory() 

    if directory and os.path.exists(directory):
        widget.le_vtex_location.setText(directory)
        set_unsaved(widget.lbl_global_config)


def on_btn_save_global_config(widget):
    vtex_location = widget.le_vtex_location.text()
    vtex_location_path = pathlib.Path(vtex_location) / "vtex.exe"

    if not vtex_location_path.exists():
        dialogs.critical(f"vtex.exe could not be found at {vtex_location}")
        return

    config_data = {
        "vtex_location": vtex_location
    }
    
    try:
        config.save_global_config(config_data)
    except Exception as e:
        dialogs.critical(f"Failed to save global config.\n {e}")

    set_saved(widget.lbl_global_config)


def on_le_vtex_location(widget):
    set_unsaved(widget.lbl_global_config)


def on_btn_export_location(widget):
    directory = dialogs.get_directory() 

    if directory and os.path.exists(directory):
        widget.le_export_location.setText(directory)
        set_unsaved(widget.lbl_graph_config)


def on_le_export_location(widget):
    set_unsaved(widget.lbl_graph_config)


def on_btn_save_graph_config(widget):
    graph_uuid = utils.get_graph_uuid()

    export_location = widget.le_export_location.text()
    # TODO other graph settings

    config_data = {
        "export_location": export_location
    }

    try:
        config.save_graph_config(graph_uuid, config_data)
    except Exception as e:
        dialogs.critical(f"Failed to save graph config.\n {e}")
    
    set_saved(widget.lbl_graph_config)


def on_btn_export_graph_presets(widget):
    export_presets()


def set_unsaved(label):
    current_text = label.text()

    if not current_text.endswith("*"):
        label.setText(current_text + "*")


def set_saved(label):
    current_text = label.text()
    label.setText(current_text.rstrip("*"))