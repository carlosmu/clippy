import bpy

class Clippy_OT_apply_clipping(bpy.types.Operator):
    """Apply Clipping Presets"""
    bl_idname = "clippy.apply_clipping"
    bl_label = "Clipping Presets"
    bl_options = {'REGISTER', 'UNDO'}

    # Prevents operator appearing in unsupported editors
    @classmethod
    def poll(cls, context):
        if (context.area.ui_type == 'VIEW_3D') or (context.area.ui_type == 'PROPERTIES'):
            return True

    ##############################################
    #   Apply Clipping functionality
    ##############################################
    def execute(self, context):
        prefs = context.preferences.addons[__package__].preferences

        # If editor is 3dView
        if context.area.ui_type == 'VIEW_3D':
            if context.scene.clippy_viewport_options == 'PRESET_1':
                context.space_data.clip_start = prefs.preset_1_start_clipping
                context.space_data.clip_end = prefs.preset_1_end_clipping

            elif context.scene.clippy_viewport_options == 'PRESET_2':
                context.space_data.clip_start = prefs.preset_2_start_clipping
                context.space_data.clip_end = prefs.preset_2_end_clipping

            elif context.scene.clippy_viewport_options == 'PRESET_3':
                context.space_data.clip_start = prefs.preset_3_start_clipping
                context.space_data.clip_end = prefs.preset_3_end_clipping
            
            elif context.scene.clippy_viewport_options == 'PRESET_4':
                context.space_data.clip_start = prefs.preset_4_start_clipping
                context.space_data.clip_end = prefs.preset_4_end_clipping
            
            elif context.scene.clippy_viewport_options == 'PRESET_5':
                context.space_data.clip_start = prefs.preset_5_start_clipping
                context.space_data.clip_end = prefs.preset_5_end_clipping
            
            elif context.scene.clippy_viewport_options == 'PRESET_6':
                context.space_data.clip_start = prefs.preset_6_start_clipping
                context.space_data.clip_end = prefs.preset_6_end_clipping
            
            elif context.scene.clippy_viewport_options == 'PRESET_7':
                context.space_data.clip_start = prefs.preset_7_start_clipping
                context.space_data.clip_end = prefs.preset_7_end_clipping
            
            elif context.scene.clippy_viewport_options == 'PRESET_8':
                context.space_data.clip_start = prefs.preset_8_start_clipping
                context.space_data.clip_end = prefs.preset_8_end_clipping

        # If editor is Properties
        elif context.area.ui_type == 'PROPERTIES':
            if context.scene.clippy_camera_options == 'PRESET_1':
                context.object.data.clip_start = prefs.preset_1_start_clipping
                context.object.data.clip_end = prefs.preset_1_end_clipping
                
            elif context.scene.clippy_camera_options == 'PRESET_2':
                context.object.data.clip_start = prefs.preset_2_start_clipping
                context.object.data.clip_end = prefs.preset_2_end_clipping

            elif context.scene.clippy_camera_options == 'PRESET_3':
                context.object.data.clip_start = prefs.preset_3_start_clipping
                context.object.data.clip_end = prefs.preset_3_end_clipping

            elif context.scene.clippy_camera_options == 'PRESET_4':
                context.object.data.clip_start = prefs.preset_4_start_clipping
                context.object.data.clip_end = prefs.preset_4_end_clipping

            elif context.scene.clippy_camera_options == 'PRESET_5':
                context.object.data.clip_start = prefs.preset_5_start_clipping
                context.object.data.clip_end = prefs.preset_5_end_clipping

            elif context.scene.clippy_camera_options == 'PRESET_6':
                context.object.data.clip_start = prefs.preset_6_start_clipping
                context.object.data.clip_end = prefs.preset_6_end_clipping

            elif context.scene.clippy_camera_options == 'PRESET_7':
                context.object.data.clip_start = prefs.preset_7_start_clipping
                context.object.data.clip_end = prefs.preset_7_end_clipping

            elif context.scene.clippy_camera_options == 'PRESET_8':
                context.object.data.clip_start = prefs.preset_8_start_clipping
                context.object.data.clip_end = prefs.preset_8_end_clipping

        return{'FINISHED'}


##############################################
# REGISTER/UNREGISTER
##############################################
def register():
    bpy.utils.register_class(Clippy_OT_apply_clipping)

def unregister():
    bpy.utils.unregister_class(Clippy_OT_apply_clipping)