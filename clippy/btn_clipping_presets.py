import bpy

from .user_prefs import Clippy_Preferences

### Register preferences for use in dropdown items
bpy.utils.register_class(Clippy_Preferences)

def clippy_ui(self, context):
    layout = self.layout
    layout.label(text="Clipping Presets", icon='PRESET')
    box = layout.box()
    row = box.row(align=True)
    row.scale_y = 1.5
    if context.area.ui_type == 'VIEW_3D':
        row.prop(context.scene, "clippy_viewport_options", text="")
    elif context.area.ui_type == 'PROPERTIES':
        row.prop(context.scene, "clippy_camera_options", text="")

    row.scale_x = 0.3
    row.operator("clippy.apply_clipping", text="Apply")
    layout.separator()

prefs = bpy.context.preferences.addons[__package__].preferences
items = [
    ('PRESET_1', prefs.preset_1_label, '', 'RESTRICT_VIEW_OFF', 0),    
    ('PRESET_2', prefs.preset_2_label, '', 'VIEW_CAMERA', 1),
    ('PRESET_3', prefs.preset_3_label, '', 'MATCLOTH', 2),
    ('PRESET_4', prefs.preset_4_label, '', 'OUTLINER_OB_ARMATURE', 3),
    ('PRESET_5', prefs.preset_5_label, '', 'FILE_IMAGE', 4),
    ('PRESET_6', prefs.preset_6_label, '', 'USER', 5),
    ('PRESET_7', prefs.preset_7_label, '', 'USER', 6),
    ('PRESET_8', prefs.preset_8_label, '', 'USER', 7),
    ]

### Unregister Preferences for use in main functionality
bpy.utils.unregister_class(Clippy_Preferences)

####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.types.VIEW3D_PT_view3d_properties.prepend(clippy_ui)
    bpy.types.DATA_PT_lens.prepend(clippy_ui)
    
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
    bpy.types.VIEW3D_PT_view3d_properties.remove(clippy_ui)
    bpy.types.DATA_PT_lens.remove(clippy_ui)

    del bpy.types.Scene.clippy_viewport_options
    del bpy.types.Scene.clippy_camera_options