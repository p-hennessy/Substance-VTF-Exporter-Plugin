import os
import sys
import pathlib


def get_config_base_path():
    home = pathlib.Path.home()

    if sys.platform == "win32":
        return home / "AppData/Roaming"
    elif sys.platform == "linux":
        return home / ".local/share"
    elif sys.platform == "darwin":
        return home / "Library/Application Support"

SUBSTANCE_DIR = get_config_base_path() / "Allegorithmic" / "Substance Designer"

CONFIG_DIR = SUBSTANCE_DIR / "vtf_exporter"
GLOBAL_CONFIG_FILE = CONFIG_DIR / "global_configuration.json"

PLUGIN_VERSION = "0.2.0"