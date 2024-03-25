import os
import json
from vtf_exporter.constants import *


def get_vtex_config_file():
    if os.path.exists(CONFIG_DIR):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE) as file:
                return json.load(file)

    return {}


def save_vtex_config_file(config_data):
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)
    
    with open(CONFIG_FILE, "w") as file:
        file.write(json.dumps(config_data, indent=4))
    
