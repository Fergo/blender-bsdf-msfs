# Blender - Principled BSDF to MSFS Material Params 

This script converts from `Principled BSDF` to `MSFS Material Params` in Blender, for use with Microsoft Flight Simulator GLTF Exporter

# How it works

It's was created with the workflow of importing SketchUp models with the Sketchup Importer for Blender, but might work with other imported meshes too.

As SketchUp only supports diffuse maps, it will convert from `Principled BSDF Base Color` to `MSFS Material Params Base Color`. It will try to find the NORMAL and ARM (Ambient Occlusion, Rooughness and Metallic) maps from the `Base Color` texture file name by searching the `texture_path` variable. For example (and by default): if the `Base Color` texture map is called `Wood_DIFFUSE.png`, it will try find the textures named `Wood_NORMAL.png` and `Wood_ARM.png`

To use other naming schemes, see below.

# How to use
1) Load `converter_sketchup.py` in Blender's `Scripting` tab
2) Change the variable `texture_path` to the path where your other texture maps are located
3) Change the `suffix_` variables to the suffixes you use for those maps. This script will try to automatically find the NORMAL and ARM maps based on the base color map
4) Run the script
