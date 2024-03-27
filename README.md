# VTF Exporter for Substance 3D Designer

![Static Badge](https://img.shields.io/badge/Compatible_Versions-%3E2022.2-blue?style=flat-square&logo=adobe)
![GitHub License](https://img.shields.io/github/license/p-hennessy/Substance-VTF-Exporter-Plugin?style=flat-square)


> [!CAUTION]
> This plugin is still in very early alpha / active development. I make no gaurentees of stability or reverse compatibility.

A plugin for [Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html) that allows one to do bulk exporting of materials into the Source Engine's VTF format. 

The goal of this plugin is to speed up the workflow for texture artists using Substance Designer for Source Games.

---

# Installing

1. Find the latest release: https://github.com/p-hennessy/Substance-VTF-Exporter-Plugin/releases
2. Download the `vtf_exporter.sdplugin` file
3. In Substance Designer, open the Tools Menu and click on "Plugin Manager"
4. Use the "Install..." button and find the sdplugin file
5. If it installed correctly there should now be a "VTF Exporter" dock. If it does not appear automatically you can find it by looking in the "Windows" menu.


# Features

- [x] Export bulk textures to VTF format
- [x] Saves settings per graph.
- [ ] Export VMT's along with textures
- [ ] Support for multiple VTF compression formats
- [ ] Import VTF as Bitmap node
- [ ] Export a single texture directly to VTF
- [ ] Output animated VTF driven by input variables


# Usage

This plugin works through Substance Designer [Parameter Presets](https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/exposing-a-parameter/parameter-presets.html).

You will need to define at least one preset for it to work.

For each preset, it will export each of the outputs in your graph. You must have at least one [output](https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/output.html) node in the graph.

The plugin outputs at the texture resolution that the final output node has. If you want a smaller resolution texture then it needs to be scaled down before the output node.

The naming pattern is as follows: 
`{graph_name}_{preset_name}_{output_name}.vtf`

#### Example: 
- Graph name: "brick001"
- Presets: "red" "yellow" and "blue"
- Outpus: "diffuse" and "normal"

Outputs:
- brick001_red_diffuse.vtf
- brick001_red_normal.vtf
- brick001_yellow_diffuse.vtf
- brick001_yellow_normal.vtf
- brick001_blue_diffuse.vtf
- brick001_blue_normal.vtf


# Configuration

These config's are stored at:

- Windows: `C:/Users/<USER>/AppData/Roaming/Allegorithmic/Substance Designer/vtf_exporter/`
- Linux: `/home/<USER>/.local/share/vtf_exporter`
- OSX: `/Users/<USER>/Library/Application Support/vtf_exporter`

Graph's configurations will use Substance Designer's built in UUID's as their filenames.

### Global Configuration
<details>
<summary>vtex location</summary>
This is needed so the plugin can convert to VTF format.

This vtex program comes with any source game. 

Mine is located here: `C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/bin/vtex.exe`

More info on vtex: https://developer.valvesoftware.com/wiki/VTEX_(Source)/en
</details>

### Graph Configuration
<details>
<summary>export location</summary>
This is the location that the vtf / vmt files will be exported to.
</details>
