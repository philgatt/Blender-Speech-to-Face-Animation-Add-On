import bpy
import os
from bpy.types import Operator
from .utils import RunScript

class OBJECT_OT_RunLipSync(Operator):
    bl_idname = "object.run_lipsync"
    bl_label = "Run Lip Sync"
    bl_description = "Process the audio file for lip sync animation"

    def execute(self, context):
        props = context.scene.lipsync_props
        if not os.path.exists(props.model_path) or not os.path.exists(props.audio_path):
            self.report({'ERROR'}, "Model or audio file path is invalid!")
            return {'CANCELLED'}
        RunScript(props)
        return {'FINISHED'}