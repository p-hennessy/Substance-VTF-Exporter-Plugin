import sd
from sd.api.sdproperty import *
from sd.api.sdvaluetexture import SDValueTexture

from pathlib import Path
import subprocess
import os
import tempfile 
import logging

from vtf_exporter import config

logger = logging.getLogger("VTF Exporter") 


def bulk_export():
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()
    graph = uiMgr.getCurrentGraph()

    # TODO Error checking for if VTEX config is setup or not.

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
        save_outputs_as_vtf(graph, preset.getLabel())

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


def save_outputs_as_vtf(graph, preset_name):
    plugin_config = config.get_vtex_config_file()
    vtex_exe = plugin_config.get("vtex_path")
    # TODO Error handling if vtex path is not configured

    for node in graph.getOutputNodes():
        props = node.getProperties(SDPropertyCategory.Output)
        value = node.getPropertyValue(props[0])
        texture = SDValueTexture.get(value)

        output_name = props[0].getId()
        
        file_name = f"{graph.getIdentifier()}_{preset_name}_{output_name}"
        # logger.debug(f"File name will be {file_name}")

        save_temp_dir = tempfile.mkdtemp()
        save_temp_file = os.path.join(str(save_temp_dir), f"{file_name}.tga")
        save_vtex_config_file = os.path.join(str(save_temp_dir), f"{file_name}.txt")
        # logger.debug(f"Temp dir: {save_temp_dir}. Temp file: {save_temp_file}. VTEX Config File: {save_vtex_config_file}")

        # TODO Take a filepath in config?
        save_dir = Path(f'C:/Users/phenn/Desktop')

        # TODO Take additional args based on alpha channel
        # logger.debug(f"Saving config file to {save_vtex_config_file}")

        with open(save_vtex_config_file, "w") as file:
            file.write("stripalphachannel 1\n")

        # logger.debug(f"Saving file to {save_temp_file}")
        texture.save(save_temp_file)

        # logger.debug(f"Running VTEX on {save_vtex_config_file}")
        command = [str(vtex_exe), "-nopause", "-outdir", str(save_dir), save_vtex_config_file]
        output = subprocess.run(command, shell=True, capture_output=True)

        # logger.debug("Cleaning up temp files")
        os.remove(save_temp_file)
        os.remove(save_vtex_config_file)

        logger.info(f"Saved {file_name}.vtf to {save_dir}")