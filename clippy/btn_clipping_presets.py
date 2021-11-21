import bpy

##############################################
#   DRAW BUTTON
##############################################
def clippy_view_button(self, context):
    # prefs = context.preferences.addons[__package__].preferences
    layout = self.layout
    layout.label(text="Clipping Presets", icon='IMAGE_ZDEPTH')
    row = layout.row(align=True)
    row.prop(context.scene, "clippy_options", text="")
    row.operator("clippy.viewport_clipping", text="Apply")
    layout.separator()


##############################################
## Register/unregister classes and functions
##############################################
def register():
    bpy.types.VIEW3D_PT_view3d_properties.prepend(clippy_view_button)
    
    bpy.types.Scene.clippy_options = bpy.props.EnumProperty(
        name = "Clip presets",
        description = "Presets for clipping",
        items = [
            ('PRESET_1', 'Viewport Default', ''),    
            ('PRESET_2', 'Camera Default', ''),
            ('PRESET_3', 'Product Design', ''),
            ('PRESET_4', 'Landscape', ''),
            ('PRESET_5', 'Worlds', ''),
            ('PRESET_6', 'Custom', '')
            ],
        default = 'PRESET_1'
    )
        
def unregister():
    bpy.types.VIEW3D_PT_view3d_properties.remove(clippy_view_button) 

    del bpy.types.Scene.clippy_options