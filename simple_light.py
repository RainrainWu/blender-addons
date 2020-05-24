import bpy
from bpy.types import Menu


bl_info = {
    "name": "S.Simple Pie Menu",
    "author": "Syler",
    "version": (0, 0, 0, 1),
    "description": "Adds Pie Menus",
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
    # object Mode
    km = kc.keymaps.new(name='Object Mode', space_type='EMPTY')
    # here you can chose the keymapping.
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

        pie = layout.menu_pie()
        pie.operator("add.three_point_light")
        pie.operator("add.sun_light")

class PIE_MENU_SIMPLE_LIGHT_CALL(bpy.types.Operator):
    bl_idname = 'sop.sm_template'
    bl_label = 'S.Menu Navigation'
    bl_description = 'Calls simple light pie menu'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="PIE_MENU_SIMPLE_LIGHT")
        return {'FINISHED'}

class THREE_POINT_LIGHT(bpy.types.Operator):
    bl_idname = "add.three_point_light"
    bl_label = "Add three point light"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(15.0, 15.0, 0.0), rotation=(-1.57, -0.0, -0.77))
        object = bpy.context.object
        object.data.energy = 1200.0
        object.data.color = (0.079, 0.344, 0.231)
        object.data.use_shadow = False
        object.data.size = 20
        
        bpy.ops.object.light_add(type="AREA", align="WORLD", location=(-15.0, -15.0, 10.0), rotation=(1.0, -0.0, -0.77))
        object = bpy.context.object
        object.data.energy = 2000.0
        object.data.color = (1, 0.3, 0)
        object.data.size = 1
        
        bpy.ops.object.light_add(type="AREA", radius=5, align="WORLD", location=(0.0, 0.0, 20.0), rotation=(0.0, 0.0, 0.0))
        object = bpy.context.object
        object.data.energy = 1000.0
        object.data.color = (0.097, 0.421, 1)
        object.data.use_shadow = False
        object.data.size = 10

        return {"FINISHED"}

class SUN_LIGHT(bpy.types.Operator):
    bl_idname = "add.sun_light"
    bl_label = "Add sun light"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.light_add(type="AREA", radius=5, align="WORLD", location=(-10.0, 10.0, 10.0), rotation=(0.0, -0.77, -0.77))
        object = bpy.context.object
        object.data.energy = 6000.0
        object.data.color = (1, 0.855, 0.750)
        object.data.size = 0
        
        bpy.ops.object.light_add(type="AREA", radius=5, align="WORLD", location=(25.0, 10.0, 15.0), rotation=(0.0, -0.77, -1))
        object = bpy.context.object
        object.data.energy = 800.0
        object.data.color = (1, 0.409, 0.633)
        object.data.size = 20
        
        bpy.ops.object.light_add(type="AREA", radius=5, align="WORLD", location=(0, -25.0, 15.0), rotation=(0.0, -0.77, -0.5))
        object = bpy.context.object
        object.data.energy = 800.0
        object.data.color = (0.367, 1.0, 0.348)
        object.data.size = 20
        
        return {"FINISHED"}

def register():
    bpy.utils.register_class(PIE_MENU_SIMPLE_LIGHT)
    bpy.utils.register_class(PIE_MENU_SIMPLE_LIGHT_CALL)
    bpy.utils.register_class(THREE_POINT_LIGHT)
    bpy.utils.register_class(SUN_LIGHT)
    add_hotkey()

def unregister():
    bpy.utils.unregister_class(PIE_MENU_SIMPLE_LIGHT)
    bpy.utils.unregister_class(PIE_MENU_SIMPLE_LIGHT_CALL)
    bpy.utils.unregister_class(THREE_POINT_LIGHT)
    bpy.utils.unregister_class(SUN_LIGHT)
    remove_hotkey()

if __name__ == "__main__":
    register()