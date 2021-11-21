import bpy

from .user_prefs import Clippy_Preferences

### Register preferences for use in dropdown items
bpy.utils.register_class(Clippy_Preferences)

def clippy_view_button(self, context):
    layout = self.layout
    box = layout.box()
    box.label(text="Clipping Presets", icon='IMAGE_ZDEPTH')

    row = box.row(align=True)
    if context.area.ui_type == 'VIEW_3D':
        row.prop(context.scene, "clippy_viewport_options", text="")
    elif context.area.ui_type == 'PROPERTIES':
        row.prop(context.scene, "clippy_camera_options", text="")

    row.scale_x = 0.3
    row.operator("clippy.apply_clipping", text="Apply")
    layout.separator()

prefs = bpy.context.preferences.addons[__package__].preferences
items = [
    ('PRESET_1', prefs.preset_1_label, ''),    
    ('PRESET_2', prefs.preset_2_label, ''),
    ('PRESET_3', prefs.preset_3_label, ''),
    ('PRESET_4', prefs.preset_4_label, ''),
    ('PRESET_5', prefs.preset_5_label, ''),
    ('PRESET_6', prefs.preset_6_label, ''),
    ('PRESET_7', prefs.preset_7_label, ''),
    ('PRESET_8', prefs.preset_8_label, ''),
    ]

### Unregister Preferences for use in main functionality
bpy.utils.unregister_class(Clippy_Preferences)

##############################################
## Register/unregister classes and functions
##############################################
def register():
    bpy.types.VIEW3D_PT_view3d_properties.prepend(clippy_view_button)
    bpy.types.DATA_PT_lens.prepend(clippy_view_button)
    
    bpy.types.Scene.clippy_viewport_options = bpy.props.EnumProperty(
        name = "Clip presets",
        description = "Presets for clipping",
        items = items,
        default = 'PRESET_1',
    )
    bpy.types.Scene.clippy_camera_options = bpy.props.EnumProperty(
        name = "Clip presets",
        description = "Presets for clipping",
        items = items,
        default = 'PRESET_2',
    )
        
def unregister():
    bpy.types.VIEW3D_PT_view3d_properties.remove(clippy_view_button) 
    bpy.types.DATA_PT_lens.remove(clippy_view_button) 

    del bpy.types.Scene.clippy_viewport_options
    del bpy.types.Scene.clippy_camera_options