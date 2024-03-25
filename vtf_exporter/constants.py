import os

SUBSTANCE_DIR = os.path.join(os.getenv('APPDATA') , "Allegorithmic", "Substance Designer")
CONFIG_DIR = os.path.join(SUBSTANCE_DIR, "vtf_exporter")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

PLUGIN_VERSION = "0.1.0"
MAIN_MENU_NAME = "vtf_exporter_main"