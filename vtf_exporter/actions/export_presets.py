import sd
from sd.api.sdproperty import *
from sd.api.sdvaluetexture import SDValueTexture

from pathlib import Path
import subprocess
import os
import tempfile 
import logging

from vtf_exporter import config
from vtf_exporter.ui import dialogs
from vtf_exporter.utils import get_graph_uuid

logger = logging.getLogger("VTF Exporter") 


def export_presets():
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()
    graph = uiMgr.getCurrentGraph()
    global_config = config.get_global_config()

    logger.info("Running error checking before export...")

    if not global_config.get("vtex_location"):
        dialogs.critical("You need to configure your VTEX location to run this function.")
        return

    vtex_location = Path(global_config.get("vtex_location"))
    vtex_exe = vtex_location / "vtex.exe"
    if not vtex_exe.exists():
        dialogs.critical(f"vtex.exe could not be found at {vtex_location}") 
        return

    if not graph:
        dialogs.critical("Please select a graph to run this function on")
        return

    graph_uuid = get_graph_uuid()
    graph_config = config.get_graph_config(graph_uuid)

    if not graph_config:
        dialogs.critical("You must setup and / or save your graph configuration to run this function")
        return

    if not graph_config.get("export_location"):
        dialogs.critical("You must have a valid export location")
        retur 

    if len(graph.getOutputNodes()) == 0:
        dialogs.critical("You need graph outputs to run this function")
        return

    if len(graph.getPresets()) == 0:
        dialogs.critical("You need to set up graph presets to run this function")
        return 

    logger.info("Saving current graph input settings...")

    # Save current graph inputs
    current_props = {}
    props = graph.getProperties(SDPropertyCategory.Input)
    for prop in props:
        id = prop.getId()
        value = graph.getInputPropertyValueFromId(id) 
        current_props[id] = value
								
    # Go through each preset and render it out
    logger.info("Starting VTF Rendering...")

    for preset in graph.getPresets():
        set_preset(graph, preset)
        save_outputs_as_vtf(
            graph, 
            preset.getLabel(), 
            global_config['vtex_location'], 
            graph_config['export_location']
        )

    # Reset graph inputs
    logger.info("Reseting graph input settings...")

    for id, value in current_props.items():
        graph.setInputPropertyValueFromId(id, value)
    graph.compute()



def set_preset(graph, preset):
    logger.info(f"Setting preset to {preset.getLabel()}...")

    for preset_input in preset.getInputs():
        value = preset_input.getValue()
        id = preset_input.getIdentifier()
        graph.setInputPropertyValueFromId(id, value)
        
    graph.compute()


def save_outputs_as_vtf(graph, preset_name, vtex_location, export_location):
    vtex_exe = Path(vtex_location) / "vtex.exe"

    for node in graph.getOutputNodes():
        props = node.getProperties(SDPropertyCategory.Output)
        value = node.getPropertyValue(props[0])
        texture = SDValueTexture.get(value)

        output_name = props[0].getId()
        
        file_name = f"{graph.getIdentifier()}_{preset_name}_{output_name}"

        save_temp_dir = tempfile.mkdtemp()
        save_temp_file = os.path.join(str(save_temp_dir), f"{file_name}.tga")
        save_vtex_config_file = os.path.join(str(save_temp_dir), f"{file_name}.txt")

        save_dir = Path(export_location)

        with open(save_vtex_config_file, "w") as file:
            # TODO change this to change compression format
            file.write("stripalphachannel 1\n")

        texture.save(save_temp_file)

        command = [str(vtex_exe), "-nopause", "-outdir", str(save_dir), save_vtex_config_file]
        subprocess.run(command, shell=True, capture_output=True)

        os.remove(save_temp_file)
        os.remove(save_vtex_config_file)

        logger.info(f"Saved {file_name}.vtf to {save_dir}")