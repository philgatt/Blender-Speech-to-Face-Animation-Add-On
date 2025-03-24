from bpy.props import StringProperty, IntProperty, PointerProperty
from bpy.types import PropertyGroup

class LipSyncProperties(PropertyGroup):
    model_path: StringProperty(name="Model Path", subtype='DIR_PATH', default="D:\\LipSync\\model")
    audio_path: StringProperty(name="Audio File", subtype='FILE_PATH')
    PP: IntProperty(name="PP", default=20514)
    Silent: IntProperty(name="Silent", default=20514)