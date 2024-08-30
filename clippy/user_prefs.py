import bpy

##############################################
#    USER PREFERENCES 
##############################################

class Clippy_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    # Preset 1
    preset_1_label : bpy.props.StringProperty(
        name = "Preset name",
        description = "Name for this preset",
        default = "Viewport Default"
    )
    preset_1_start_clipping : bpy.props.FloatProperty(
        name = "Clip Start",
        description = "Start clipping for this preset",
        default = 0.01,
        precision = 3
    )
    preset_1_end_clipping : bpy.props.FloatProperty(
        name = "Clip End",
        description = "End clipping for this preset",
        default = 1000.0,
        precision = 3
    )

    # Preset 2
    preset_2_label : bpy.props.StringProperty(
        name = "Preset name",
        description = "Name for this preset",
        default = "Camera Default"
    )
    preset_2_start_clipping : bpy.props.FloatProperty(
        name = "Clip Start",
        description = "Start clipping for this preset",
        default = 0.1,
        precision = 3
    )
    preset_2_end_clipping : bpy.props.FloatProperty(
        name = "Clip End",
        description = "End clipping for this preset",
        default = 100.0,
        precision = 3
    )

    # Preset 3
    preset_3_label : bpy.props.StringProperty(
        name = "Preset name",
        description = "Name for this preset",
        default = "Products / 3D Print"
    )
    preset_3_start_clipping : bpy.props.FloatProperty(
        name = "Clip Start",
        description = "Start clipping for this preset",
        default = 0.001,
        precision = 3
    )
    preset_3_end_clipping : bpy.props.FloatProperty(
        name = "Clip End",
        description = "End clipping for this preset",
        default = 2.0,
        precision = 3
    )

    # Preset 4
    preset_4_label : bpy.props.StringProperty(
        name = "Preset name",
        description = "Name for this preset",
        default = "Archviz / Characters"
    )
    preset_4_start_clipping : bpy.props.FloatProperty(
        name = "Clip Start",
        description = "Start clipping for this preset",
        default = 0.1,
        precision = 3
    )
    preset_4_end_clipping : bpy.props.FloatProperty(
        name = "Clip End",
        description = "End clipping for this preset",
        default = 1000.0,
        precision = 3
    )

    # Preset 5
    preset_5_label : bpy.props.StringProperty(
        name = "Preset name",
        description = "Name for this preset",
        default = "Landscape"
    )
    preset_5_start_clipping : bpy.props.FloatProperty(
        name = "Clip Start",
        description = "Start clipping for this preset",
        default = 0.5,
        precision = 3
    )
    preset_5_end_clipping : bpy.props.FloatProperty(
        name = "Clip End",
        description = "End clipping for this preset",
        default = 50000.0,
        precision = 3
    )

    # Preset 6
    preset_6_label : bpy.props.StringProperty(
        name = "Preset name",
        description = "Name for this preset",
        default = "Custom 1"
    )
    preset_6_start_clipping : bpy.props.FloatProperty(
        name = "Clip Start",
        description = "Start clipping for this preset",
        default = 10,
        precision = 3
    )
    preset_6_end_clipping : bpy.props.FloatProperty(
        name = "Clip End",
        description = "End clipping for this preset",
        default = 5000.0,
        precision = 3
    )

    # Preset 7
    preset_7_label : bpy.props.StringProperty(
        name = "Preset name",
        description = "Name for this preset",
        default = "Custom 2"
    )
    preset_7_start_clipping : bpy.props.FloatProperty(
        name = "Clip Start",
        description = "Start clipping for this preset",
        default = 10,
        precision = 3
    )
    preset_7_end_clipping : bpy.props.FloatProperty(
        name = "Clip End",
        description = "End clipping for this preset",
        default = 15000.0,
        precision = 3
    )

    # Preset 8
    preset_8_label : bpy.props.StringProperty(
        name = "Preset name",
        description = "Name for this preset",
        default = "Custom 3"
    )
    preset_8_start_clipping : bpy.props.FloatProperty(
        name = "Clip Start",
        description = "Start clipping for this preset",
        default = 50,
        precision = 3
    )
    preset_8_end_clipping : bpy.props.FloatProperty(
        name = "Clip End",
        description = "End clipping for this preset",
        default = 150000.0,
        precision = 3
    )
    
    # Preferences UI
    def draw(self, context):
        layout = self.layout 

        
        col = layout.column(align=True)
        col.scale_y = 1.5

        row = col.row(align=True)
        row.label(text="Preset Name", icon='PRESET')
        # row.scale_x = .5
        row.label(text="Clip Start", icon='ZOOM_OUT')
        row.label(text="Clip End", icon='ZOOM_IN')

        row = col.row(align=True)
        row.prop(self, "preset_1_label", text="")
        row.prop(self,"preset_1_start_clipping", text="")
        row.prop(self,"preset_1_end_clipping", text="")

        row = col.row(align=True)
        row.prop(self, "preset_2_label", text="")
        row.prop(self,"preset_2_start_clipping", text="")
        row.prop(self,"preset_2_end_clipping", text="")

        row = col.row(align=True)
        row.prop(self, "preset_3_label", text="")
        row.prop(self,"preset_3_start_clipping", text="")
        row.prop(self,"preset_3_end_clipping", text="")

        row = col.row(align=True)
        row.prop(self, "preset_4_label", text="")
        row.prop(self,"preset_4_start_clipping", text="")
        row.prop(self,"preset_4_end_clipping", text="")

        row = col.row(align=True)
        row.prop(self, "preset_5_label", text="")
        row.prop(self,"preset_5_start_clipping", text="")
        row.prop(self,"preset_5_end_clipping", text="")

        row = col.row(align=True)
        row.prop(self, "preset_6_label", text="")
        row.prop(self,"preset_6_start_clipping", text="")
        row.prop(self,"preset_6_end_clipping", text="")

        row = col.row(align=True)
        row.prop(self, "preset_7_label", text="")
        row.prop(self,"preset_7_start_clipping", text="")
        row.prop(self,"preset_7_end_clipping", text="")

        row = col.row(align=True)
        row.prop(self, "preset_8_label", text="")
        row.prop(self,"preset_8_start_clipping", text="")
        row.prop(self,"preset_8_end_clipping", text="")

        layout.separator()

        box = layout.box()
        box.label(text="Notice:", icon='INFO')
        box.label(text="The values above are expressed in meters.")
        box.label(text="To update the presets names, restart blender is needed.")

        layout.separator()

####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(Clippy_Preferences) 
        
def unregister():
    bpy.utils.unregister_class(Clippy_Preferences)