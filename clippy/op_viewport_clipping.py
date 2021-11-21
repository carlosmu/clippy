import bpy

# from .user_prefs import Clippy_Preferences

# ### Register preferences for use in properties
# bpy.utils.register_class(Clippy_Preferences)

class Clippy_OT_viewport_clipping(bpy.types.Operator):
    """Viewport Clipping Preferences"""
    bl_idname = "clippy.viewport_clipping"
    bl_label = "Clipping Presets"
    bl_options = {'REGISTER', 'UNDO'}

# Prevents operator appearing in unsupported editors
    # @classmethod
    # def poll(cls, context):
    #     if (context.area.ui_type == 'VIEW_3D'):
    #         return True

    ##############################################
    #   Playblast functionality
    ##############################################
    def execute(self, context):
        prefs = context.preferences.addons[__package__].preferences

        if context.scene.clippy_options == 'PRESET_1':
            context.space_data.clip_start = prefs.preset_1_start_clipping
            context.space_data.clip_end = prefs.preset_1_end_clipping
        elif context.scene.clippy_options == 'PRESET_2':
            context.space_data.clip_start = prefs.preset_2_start_clipping
            context.space_data.clip_end = prefs.preset_2_end_clipping
        elif context.scene.clippy_options == 'PRESET_3':
            context.space_data.clip_start = prefs.preset_3_start_clipping
            context.space_data.clip_end = prefs.preset_3_end_clipping
        elif context.scene.clippy_options == 'PRESET_4':
            context.space_data.clip_start = prefs.preset_4_start_clipping
            context.space_data.clip_end = prefs.preset_4_end_clipping
        elif context.scene.clippy_options == 'PRESET_5':
            context.space_data.clip_start = prefs.preset_5_start_clipping
            context.space_data.clip_end = prefs.preset_5_end_clipping
        else:
            context.space_data.clip_start = prefs.preset_6_start_clipping
            context.space_data.clip_end = prefs.preset_6_end_clipping

        return{'FINISHED'}





##############################################
# Register/unregister classes and functions
##############################################
def register():
    bpy.utils.register_class(Clippy_OT_viewport_clipping)


def unregister():
    bpy.utils.unregister_class(Clippy_OT_viewport_clipping)