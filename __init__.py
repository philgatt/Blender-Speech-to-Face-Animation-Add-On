import bpy
from .properties import LipSyncProperties
from .operators import OBJECT_OT_RunLipSync
from .panels import OBJECT_PT_LipSyncPanel

bl_info = {
    "name": "Audio to Face",
    "author": "Philipp",
    "version": (1, 0, 0),
    "blender": (3, 3, 0),  # Minimum Blender version
    "location": "View3D > UI > Motion Capture",
    "description": "Captures facial motion and applies it to a Blender character.",
    "warning": "",
    "doc_url": "",
    "category": "Motion Capture",
}

def register():
    bpy.utils.register_class(LipSyncProperties)
    bpy.utils.register_class(OBJECT_OT_RunLipSync)
    bpy.utils.register_class(OBJECT_PT_LipSyncPanel)
    bpy.types.Scene.lipsync_props = bpy.props.PointerProperty(type=LipSyncProperties)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_LipSyncPanel)
    bpy.utils.unregister_class(OBJECT_OT_RunLipSync)
    bpy.utils.unregister_class(LipSyncProperties)
    del bpy.types.Scene.lipsync_props

if __name__ == "__main__":
    register()