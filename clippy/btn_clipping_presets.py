import bpy

##############################################
#   DRAW BUTTON
##############################################
class Clippy_PT_ClippyPresets(bpy.types.Panel):
    bl_label = "Clippy"
    bl_idname = "Clippy_PT_ClippyPresets"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'View'
    bl_order = 100
    bl_parent_id = "VIEW3D_PT_view3d_properties"

    def draw(self, context):
        # prefs = context.preferences.addons[__package__].preferences
        layout = self.layout
        layout.label(text="Clipping Presets", icon='IMAGE_ZDEPTH')
        row = layout.row(align=True)
        row.scale_x = 2.0
        row.prop(context.scene, "clippy_options", text="")
        row.scale_x = 0.5
        row.operator("clippy.viewport_clipping", text="Apply")
        layout.separator()

items = [
    ('PRESET_1', 'Viewport Default', ''),    
    ('PRESET_2', 'Camera Default', ''),
    ('PRESET_3', 'Product Design', ''),
    ('PRESET_4', 'Landscape', ''),
    ('PRESET_5', 'Worlds', ''),
    ('PRESET_6', 'Custom', '')
    ]

##############################################
## Register/unregister classes and functions
##############################################
def register():
    # bpy.types.VIEW3D_PT_view3d_properties.prepend(clippy_view_button)
    bpy.utils.register_class(Clippy_PT_ClippyPresets)
    
    bpy.types.Scene.clippy_options = bpy.props.EnumProperty(
        name = "Clip presets",
        description = "Presets for clipping",
        items = items,
        default = 'PRESET_1',
    )
        
def unregister():
    # bpy.types.VIEW3D_PT_view3d_properties.remove(clippy_view_button) 
    bpy.utils.unregister_class(Clippy_PT_ClippyPresets)

    del bpy.types.Scene.clippy_options