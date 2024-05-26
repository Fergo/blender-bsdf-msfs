import bpy
import os

# Blender - Principled BSDF to MSFS Material Params
# Created by: Fernando Birck - 2024 

# HOW IT WORKS
# This script converts from Principled BSDF to MSFS Material Params in Blender.
# It's intended to be used with the Skechtup Blender Importer, but might work with other imported meshes too.
# As SU only supports diffuse maps, it will convert from "Principled BSDF Base Color" to "MSFS Material Params Base Color"
# It will try to find the NORMAL and ARM maps from the "Base Color" texture file name by searching the 'texture_path' variable
# By default, if the "Base Color" texture map is called "Wood_DIFFUSE.png", it will try find the textures named "Wood_NORMAL.png" and "Wood_ARM.png"
# To use other naming schemes, see below

# HOW TO USE
#1) Change the variable 'texture_path' to the path where your texture maps are located (Normals and ARM (Ambient Occlusion/Roughness/Metallic))
#2) Change the 'suffix_' variables to the suffixes you use for those maps. This script will try to automatically find the NORMAL and ARM maps based on the base color map

def ConvertMaterials():
    suffix_arm = "_ARM"
    suffix_normal = "_NORMAL"
    suffix_diffuse = "_DIFFUSE"

    texture_path =  'C:\\PATH\\TO\\THE\\TEXTURES'
    
    for mat in bpy.data.materials:
        if mat.node_tree != None:
            if "Principled BSDF" in mat.node_tree.nodes:
                if "Base Color" in mat.node_tree.nodes["Principled BSDF"].inputs:
                    if len(mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].links) > 0:
                        node = mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].links[0].from_node
                        if node.type == "TEX_IMAGE":
                            print(f"Converting BSDF to MSFS: {mat.name}")

                            # Set the MSFS base color material do the be the same as the Principled BSDF base color material
                            # NOTE: when setting msfs_material_type, the MSFS GLTF Exporter will automatically delete the BSDF material
                            mat.msfs_base_color_texture = node.image
                            mat.msfs_material_type = 'msfs_standard'

                            # Try to find the NORMAL and ARM textures based on the base color texture
                            filename_diffuse = mat.msfs_base_color_texture.filepath
                            filepath, filename = os.path.split(filename_diffuse)
                            
                            filename_normal = os.path.join(texture_path, filename.replace(suffix_diffuse + '.', suffix_normal + '.'))
                            filename_arm = os.path.join(texture_path, filename.replace(suffix_diffuse + '.', suffix_arm + '.'))

                            if os.path.isfile(filename_normal):            
                                mat.msfs_normal_texture = bpy.data.images.load(filename_normal)
                                print(f"\tNormal texture found and loaded: {filename_normal}")
                            else:
                                print(f"\tFailed to find ARM texture: {filename_normal}")

                            if os.path.isfile(filename_arm): 
                                mat.msfs_occlusion_metallic_roughness_texture = bpy.data.images.load(filename_arm)
                                print(f"\tARM texture found and loaded: {filename_arm}")
                            else:
                                print(f"\tFailed to find ARM texture: {filename_arm}")
                                
if __name__ == "__main__":
    ConvertMaterials()