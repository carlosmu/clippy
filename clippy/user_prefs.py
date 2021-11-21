import bpy
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty, IntProperty, FloatProperty, BoolProperty, EnumProperty

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
        default = "Product Design"
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
        default = "Landscape"
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
        default = 50000.0,
        precision = 3
    )
    # Preset 5
    preset_5_label : bpy.props.StringProperty(
        name = "Preset name",
        description = "Name for this preset",
        default = "Worlds"
    )
    preset_5_start_clipping : bpy.props.FloatProperty(
        name = "Clip Start",
        description = "Start clipping for this preset",
        default = 100,
        precision = 3
    )
    preset_5_end_clipping : bpy.props.FloatProperty(
        name = "Clip End",
        description = "End clipping for this preset",
        default = 1000000.0,
        precision = 3
    )
    # Preset 6
    preset_6_label : bpy.props.StringProperty(
        name = "Preset name",
        description = "Name for this preset",
        default = "Custom"
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

    # # Dropdown Menu
    # clippy_presets : bpy.props.EnumProperty(
    #     name = "Clip presets",
    #     description = "Presets for clipping",
    #     items = [
    #         ('PRESET_1', 'Linear', ''),
    #         ('PRESET_2', 'Cardinal', ''),
    #         ('PRESET_3', 'Catmull-Rom', ''),
    #         ('PRESET_4', 'BSpline', ''),
    #         ('PRESET_5', 'BSpline', ''),
    #         ('PRESET_6', 'BSpline', '')],
    #     default = 'PRESET_1'
    # )
    
    
    def draw(self, context):
        layout = self.layout 


        row = layout.row(align=True)   
        row.label(text="Preset Name")
        row.label(text="Start Clipping")
        row.label(text="End Clipping")

        row = layout.row(align=True)
        row.prop(self, "preset_1_label", text="")
        row.prop(self,"preset_1_start_clipping", text="")
        row.prop(self,"preset_1_end_clipping", text="")

        row = layout.row(align=True)
        row.prop(self, "preset_2_label", text="")
        row.prop(self,"preset_2_start_clipping", text="")
        row.prop(self,"preset_2_end_clipping", text="")

        row = layout.row(align=True)
        row.prop(self, "preset_3_label", text="")
        row.prop(self,"preset_3_start_clipping", text="")
        row.prop(self,"preset_3_end_clipping", text="")

        row = layout.row(align=True)
        row.prop(self, "preset_4_label", text="")
        row.prop(self,"preset_4_start_clipping", text="")
        row.prop(self,"preset_4_end_clipping", text="")

        row = layout.row(align=True)
        row.prop(self, "preset_5_label", text="")
        row.prop(self,"preset_5_start_clipping", text="")
        row.prop(self,"preset_5_end_clipping", text="")

        row = layout.row(align=True)
        row.prop(self, "preset_6_label", text="")
        row.prop(self,"preset_6_start_clipping", text="")
        row.prop(self,"preset_6_end_clipping", text="")

        layout.prop(self, "clippy_presets")

####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(Clippy_Preferences) 
        
def unregister():
    bpy.utils.unregister_class(Clippy_Preferences)