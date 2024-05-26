import bpy
import os

def ConvertMaterials():
    suffix_arm = "_ARM"
    suffix_normal = "_NORMAL"
    suffix_diffuse = "_DIFFUSE"
    
    for mat in bpy.data.materials:
        if mat.node_tree != None:
            if "Principled BSDF" in mat.node_tree.nodes:
                if "Base Color" in mat.node_tree.nodes["Principled BSDF"].inputs:
                    if len(mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].links) > 0:
                        node = mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].links[0].from_node
                        if node.type == "TEX_IMAGE":
                            #new_image = node.image.copy()
                            mat.msfs_base_color_texture = node.image
                            mat.msfs_material_type = 'msfs_standard'
                            
                            print(f"Converting BSDF to MSFS: {mat.name}")

                            texture_path =  'C:\\Users\\Birck\\Desktop\\teste\\box'
                            
                            filename_diffuse = node.image.filepath
                            filepath, filename = os.path.split(filename_diffuse)
                            
                            filename_normal = os.path.join(texture_path, filename.replace(suffix_diffuse + '.', suffix_normal + '.'))
                            filename_arm = os.path.join(texture_path, filename.replace(suffix_diffuse + '.', suffix_arm + '.'))
                            
                            print(f"\tDiffuse texture: {filename_diffuse}")
                            print(f"\tNormal texture: {filename_normal}")
                            print(f"\tARM texture: {filename_arm}")
                                                    
                            mat.msfs_normal_texture = bpy.data.images.load(filename_normal)
                            mat.msfs_occlusion_metallic_roughness_texture = bpy.data.images.load(filename_arm)
if __name__ == "__main__":
    ConvertMaterials()

# for mat in bpy.data.materials:
    # if mat.node_tree != None:
        # if "Principled BSDF" in mat.node_tree.nodes:
            # if "Base Color" in mat.node_tree.nodes["Principled BSDF"].inputs:
                # if len(mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].links) > 0:
                    # node = mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].links[0].from_node
                    # if node.type == "TEX_IMAGE":
                        # change the diffuse texture and material type
                        # mat.msfs_base_color_texture = node.image
                        # mat.msfs_material_type = 'msfs_standard'
                        
                        # # try to find the normal map
                        # try:
                            # mat_normal = bpy.data.materials[mat.name + suffix_normal]
                            # image_normal = mat_normal.node_tree.nodes["Principled BSDF"].inputs["Base Color"].links[0].from_node
                            # mat.msfs_normal_texture = image_normal
                        # finally:
                            # pass
                        
                        # # try to find the ARM map
                        # try:
                            # mat_arm = bpy.data.materials[mat.name + suffix_arm]
                            # image_arm = mat_arm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].links[0].from_node
                            # mat.msfs_occlusion_metallic_roughness_texture = image_arm
                        # finally:
                            # pass