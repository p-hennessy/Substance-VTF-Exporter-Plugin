# VTF Exporter for Substance 3D Designer

> [!WARNING]
> This plugin is still in very early alpha / active development. I made no gaurentees of stability or reverse compatibility.

A plugin for Substance 3D Designer that allows one to do bulk exporting of materials into the Source Engine's VTF format

# Installing

1. Find the latest release: https://github.com/p-hennessy/Substance-VTF-Exporter-Plugin/releases
2. Download the vtf_exporter.sdplugin file
3. In Substance Designer, open the Tools Menu and click on "Plugin Manager"
4. Use the "Install..." button and find the sdplugin file
5. If it installed correctly there should now be a "VTF Exporter" menu on your top bar

# Usage

This plugin works through Substance Designer Presets.
You will need to define at least one preset for it to work.

For each preset, it will export each of the outputs in your graph.

The naming pattern it follows is: 
`{graph_name}_{preset_name}_{output_name}.vtf`

#### Example: 
Graph name: "brick001"
Presets: "red" "yellow" and "blue"
Outpus: "diffuse" and "normal"

It would output:
- brick001_red_diffuse.vtf
- brick001_red_normal.vtf
- brick001_yellow_diffuse.vtf
- brick001_yellow_normal.vtf
- brick001_blue_diffuse.vtf
- brick001_blue_normal.vtf

# Configuration

In the VTF Exporter menu, there is a Configuration option to locate your `vtex.exe` program. 
You'll have to set this for this plugin to work.

This vtex program comes with any source game. 

Mine is located here: `C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/bin/vtex.exe`




