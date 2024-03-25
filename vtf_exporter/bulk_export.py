import sd
from sd.api.sdproperty import *
from sd.api.sdvaluetexture import SDValueTexture

from pathlib import Path
import subprocess
import os
import tempfile 

from vtf_exporter import config


def bulk_export():
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()

    graph = uiMgr.getCurrentGraph()

    # Get current graph inputs

    for preset in graph.getPresets():
        set_preset(graph, preset)
        save_outputs_as_vtf(graph, preset.getLabel())

    # Reset graph inputs

	
def set_preset(graph, preset):
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
        
        save_temp_dir = tempfile.mkdtemp()
        save_temp_file = os.path.join(str(save_temp_dir), f"{file_name}.tga")
        save_vtex_config_file = os.path.join(str(save_temp_dir), f"{file_name}.txt")

        # TODO Take a filepath in config?
        save_dir = Path(f'C:/Users/phenn/Desktop')

        # TODO Take additional args based on alpha channel
        with open(save_vtex_config_file, "w") as file:
            file.write("stripalphachannel 1\n")

        texture.save(save_temp_file)

        command = [str(vtex_exe), "-nopause", "-outdir", str(save_dir), save_vtex_config_file]
        output = subprocess.run(command, shell=True, capture_output=True)

        os.remove(save_temp_file)
        os.remove(save_vtex_config_file)