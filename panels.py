import bpy
from bpy.types import Panel

class OBJECT_PT_LipSyncPanel(Panel):
    bl_label = "Lip Sync Panel"
    bl_idname = "OBJECT_PT_lipsync"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lip Sync'

    def draw(self, context):
        layout = self.layout
        props = context.scene.lipsync_props

        layout.prop(props, "model_path")
        layout.prop(props, "audio_path")
        layout.separator()
        layout.label(text="Phoneme Reference Poses:")
        layout.prop(props, "PP")
        layout.prop(props, "FF")
        layout.prop(props, "TH")
        layout.prop(props, "DD")
        layout.prop(props, "kk")
        layout.prop(props, "CH")
        layout.prop(props, "SS")
        layout.prop(props, "nn")
        layout.prop(props, "RR")
        layout.prop(props, "aa")
        layout.prop(props, "E")
        layout.prop(props, "I")
        layout.prop(props, "O")
        layout.prop(props, "U")
        layout.prop(props, "Silent")
        layout.operator("object.run_lipsync")