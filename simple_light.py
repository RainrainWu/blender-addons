"""
Simple Light provides a convenient way to set up lighting for small-scale artworks.

The default hot key is "L", you can use it to open the pie menu.
"""


import bpy
from bpy.types import Menu


bl_info = {
    "name": "Simple Light",
    "author": "Rain Wu <s0958334772@gmail.com>",
    "version": (1, 0, 0),
    "description": "Adds simple light for small-scale artworks",
    "blender": (2, 80, 0),
    "category": "3D view"
}

addon_keymaps = []


def add_hotkey():

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if not kc:
        print('Keymap Error')
        return

    # activate while in object mode
    km = kc.keymaps.new(name='Object Mode', space_type='EMPTY')
    
    # hotkey operation assignment
    kmi = km.keymap_items.new(PIE_MENU_SIMPLE_LIGHT_CALL.bl_idname, 'L', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))


def remove_hotkey():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()


class PIE_MENU_SIMPLE_LIGHT(Menu):
    bl_label = 'Add simple light'

    def draw(self, context):
        layout = self.layout
        prefs = context.preferences
        inputs = prefs.inputs

        # pie menu options assignment
        pie = layout.menu_pie()
        pie.operator("add.three_point_light_city")
        pie.operator("add.three_point_light_forest")
        pie.operator("add.sky_light_holy")
        pie.operator("add.sky_light_scifi")
        pie.operator("add.moon_light_full")
        pie.operator("add.moon_light_blood")
        pie.operator("object.remove_simple_light")


class PIE_MENU_SIMPLE_LIGHT_CALL(bpy.types.Operator):
    bl_idname = 'add.simple_light'
    bl_label = 'SAdd simple light'
    bl_description = 'Calls simple light pie menu'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        # draw pie menu while execute
        bpy.ops.wm.call_menu_pie(name="PIE_MENU_SIMPLE_LIGHT")

        return {'FINISHED'}


# simple lighting for the city atmosphere
class THREE_POINT_LIGHT_CITY(bpy.types.Operator):
    bl_idname = "add.three_point_light_city"
    bl_label = "Add three point light (city)"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(15.0, 15.0, 0.0), rotation=(-1.57, -0.0, -0.77))
        object = bpy.context.object
        object.name = 'simple_light_0'
        object.data.name = "simple_light_0"
        object.data.energy = 1200.0
        object.data.color = (0.079, 0.344, 0.231)
        object.data.use_shadow = False
        object.data.size = 20

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(-15.0, -15.0, 10.0), rotation=(1.0, -0.0, -0.77))
        object = bpy.context.object
        object.name = 'simple_light_1'
        object.data.name = "simple_light_1"
        object.data.energy = 2000.0
        object.data.color = (1, 0.3, 0)
        object.data.size = 1

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(0.0, 0.0, 20.0), rotation=(0.0, 0.0, 0.0))
        object = bpy.context.object
        object.name = 'simple_light_2'
        object.data.name = "simple_light_2"
        object.data.energy = 1000.0
        object.data.color = (0.097, 0.421, 1)
        object.data.use_shadow = False
        object.data.size = 10

        return {"FINISHED"}


# simple lighting for the forest atmosphere
class THREE_POINT_LIGHT_FOREST(bpy.types.Operator):
    bl_idname = "add.three_point_light_forest"
    bl_label = "Add three point light (forest)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(15.0, 15.0, 0.0), rotation=(-1.57, -0.0, -0.77))
        object = bpy.context.object
        object.name = 'simple_light_0'
        object.data.name = "simple_light_0"
        object.data.energy = 1200.0
        object.data.color = (0.489, 0.394, 0.710)
        object.data.use_shadow = False
        object.data.size = 20

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(-15.0, -15.0, 10.0), rotation=(1.0, -0.0, -0.77))
        object = bpy.context.object
        object.name = 'simple_light_1'
        object.data.name = "simple_light_1"
        object.data.energy = 2000.0
        object.data.color = (0.923, 1, 0.210)
        object.data.size = 1
        
        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(0.0, 0.0, 20.0), rotation=(0.0, 0.0, 0.0))
        object = bpy.context.object
        object.name = 'simple_light_2'
        object.data.name = "simple_light_2"
        object.data.energy = 1000.0
        object.data.color = (0.684, 1, 0.677)
        object.data.use_shadow = False
        object.data.size = 10

        return {"FINISHED"}


# simple lighting for the holy sky light
class SKY_LIGHT_HOLY(bpy.types.Operator):
    bl_idname = "add.sky_light_holy"
    bl_label = "Add sky light (holy)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(-10.0, 10.0, 10.0), rotation=(0.0, -0.77, -0.77))
        object = bpy.context.object
        object.name = 'simple_light_0'
        object.data.name = "simple_light_0"
        object.data.energy = 8000.0
        object.data.color = (1, 1, 0.437)
        object.data.size = 0

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(25.0, 0.0, 15.0), rotation=(0.0, -0.77, -3.14))
        object = bpy.context.object
        object.name = 'simple_light_1'
        object.data.name = "simple_light_1"
        object.data.energy = 800.0
        object.data.color = (1, 0.409, 0.633)
        object.data.size = 20

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(0, -25.0, 15.0), rotation=(0.0, -0.77, 1.57))
        object = bpy.context.object
        object.name = 'simple_light_2'
        object.data.name = "simple_light_2"
        object.data.energy = 800.0
        object.data.color = (0.367, 1.0, 0.348)
        object.data.size = 20
        
        return {"FINISHED"}


# simple lighting for the holy scifi light
class SKY_LIGHT_SCIFI(bpy.types.Operator):
    bl_idname = "add.sky_light_scifi"
    bl_label = "Add sky light (scifi)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(-10.0, 10.0, 10.0), rotation=(0.0, -0.77, -0.77))
        object = bpy.context.object
        object.name = 'simple_light_0'
        object.data.name = "simple_light_0"
        object.data.energy = 8000.0
        object.data.color = (0.429, 1, 1)
        object.data.size = 0
        
        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(25.0, 0, 15.0), rotation=(0.0, -0.77, -3.14))
        object = bpy.context.object
        object.name = 'simple_light_1'
        object.data.name = "simple_light_1"
        object.data.energy = 800.0
        object.data.color = (1, 0.547, 0.312)
        object.data.size = 20
        
        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(0, -25.0, 15.0), rotation=(0.0, -0.77, 1.57))
        object = bpy.context.object
        object.name = 'simple_light_2'
        object.data.name = "simple_light_2"
        object.data.energy = 800.0
        object.data.color = (0.367, 1.0, 0.348)
        object.data.size = 20
        
        return {"FINISHED"}


# simple lighting for the full moonlight
class MOON_LIGHT_FULL(bpy.types.Operator):
    bl_idname = "add.moon_light_full"
    bl_label = "Add moon light (full)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(-20, 8, 10), rotation=(0, -1.047, -0.523))
        object = bpy.context.object
        object.name = 'simple_light_0'
        object.data.name = "simple_light_0"
        object.data.energy = 6000
        object.data.color = (0.045, 0.192, 0.344)
        object.data.size = 5
        
        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(12, -12, 3), rotation=(0, 0.785, -0.785))
        object = bpy.context.object
        object.name = 'simple_light_1'
        object.data.name = "simple_light_1"
        object.data.energy = 500
        object.data.color = (0.296, 0.089, 0.003)
        object.data.use_shadow = False
        object.data.size = 5

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(15, 15, 12), rotation=(0, 1.047, 0.785))
        object = bpy.context.object
        object.name = 'simple_light_2'
        object.data.name = "simple_light_2"
        object.data.energy = 800
        object.data.color = (0.117, 0.095, 0.296)
        object.data.use_shadow = False
        object.data.size = 30

        return {"FINISHED"}


# simple lighting for the bloodly moonlight
class MOON_LIGHT_BLOOD(bpy.types.Operator):
    bl_idname = "add.moon_light_blood"
    bl_label = "Add moon light (blood)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(-20, 8, 10), rotation=(0, -1.047, -0.523))
        object = bpy.context.object
        object.name = 'simple_light_0'
        object.data.name = 'simple_light_0'
        object.data.energy = 6000
        object.data.color = (0.330, 0.05, 0.05)
        object.data.size = 5
        
        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(12, -12, 3), rotation=(0, 0.785, -0.785))
        object = bpy.context.object
        object.name = 'simple_light_1'
        object.data.name = "simple_light_1"
        object.data.energy = 500
        object.data.color = (0.078, 0.296, 0.219)
        object.data.use_shadow = False
        object.data.size = 5

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(15, 15, 12), rotation=(0, 1.047, 0.785))
        object = bpy.context.object
        object.name = "simple_light_2"
        object.data.name = 'simple_light_2'
        object.data.energy = 800
        object.data.color = (0.296, 0.290, 0.061)
        object.data.use_shadow = False
        object.data.size = 30

        return {"FINISHED"}


# clear all simple light objects
class CLEAR_SIMPLE_LIGHT(bpy.types.Operator):
    bl_idname = "object.remove_simple_light"
    bl_label = "Remove simple light"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        # select object by name, then delete them
        for obj in bpy.data.objects:
            if obj.name in ["simple_light_0", "simple_light_1", "simple_light_2"]:
                obj.select_set(True)
            else:
                obj.select_set(False)
        bpy.ops.object.delete()

        return {"FINISHED"}    


# register class
def register():
    bpy.utils.register_class(PIE_MENU_SIMPLE_LIGHT)
    bpy.utils.register_class(PIE_MENU_SIMPLE_LIGHT_CALL)
    bpy.utils.register_class(THREE_POINT_LIGHT_CITY)
    bpy.utils.register_class(THREE_POINT_LIGHT_FOREST)
    bpy.utils.register_class(SKY_LIGHT_HOLY)
    bpy.utils.register_class(SKY_LIGHT_SCIFI)
    bpy.utils.register_class(MOON_LIGHT_FULL)
    bpy.utils.register_class(MOON_LIGHT_BLOOD)
    bpy.utils.register_class(CLEAR_SIMPLE_LIGHT)
    add_hotkey()


# unregister class
def unregister():
    bpy.utils.unregister_class(PIE_MENU_SIMPLE_LIGHT)
    bpy.utils.unregister_class(PIE_MENU_SIMPLE_LIGHT_CALL)
    bpy.utils.unregister_class(THREE_POINT_LIGHT_CITY)
    bpy.utils.unregister_class(THREE_POINT_LIGHT_GENERAL)
    bpy.utils.unregister_class(SKY_LIGHT_HOLY)
    bpy.utils.unregister_class(SKY_LIGHT_SCIFI)
    bpy.utils.unregister_class(MOON_LIGHT_FULL)
    bpy.utils.unregister_class(MOON_LIGHT_BLOOD)
    bpy.utils.unregister_class(CLEAR_SIMPLE_LIGHT)
    remove_hotkey()


# auto register while run script
if __name__ == "__main__":
    register()