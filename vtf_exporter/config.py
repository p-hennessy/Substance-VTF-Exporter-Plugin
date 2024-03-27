import os
import json
from vtf_exporter.constants import *


def save_global_config(config_data):
    if not CONFIG_DIR.exists():
        os.mkdir(CONFIG_DIR)
    
    with open(GLOBAL_CONFIG_FILE, "w") as file:
        file.write(json.dumps(config_data, indent=4))
    

def get_global_config():
    if GLOBAL_CONFIG_FILE.exists():
        with GLOBAL_CONFIG_FILE.open("r") as file:          
            return json.load(file)
    return {}


def save_graph_config(graph_uuid, config_data):
    config_file = CONFIG_DIR / f"{graph_uuid}.json"

    if not CONFIG_DIR.exists():
        os.mkdir(CONFIG_DIR)

    with config_file.open("w") as file:
        file.write(json.dumps(config_data, indent=4))
    

def get_graph_config(graph_uuid):
    config_file = CONFIG_DIR / f"{graph_uuid}.json"

    if config_file.exists():
        with config_file.open("r") as file:
            return json.load(file)
    return {}