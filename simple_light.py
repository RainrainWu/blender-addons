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

        left = bpy.ops.object.light_add(type="AREA", radius=5, align="WORLD", location=(5.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0))
        right = bpy.ops.object.light_add(type="AREA", radius=5, align="WORLD", location=(0.0, 5.0, 0.0), rotation=(0.0, 0.0, 0.0))
        top = bpy.ops.object.light_add(type="AREA", radius=5, align="WORLD", location=(0.0, 0.0, 5.0), rotation=(0.0, 0.0, 0.0))
        return {"FINISHED"}

def menu_func(self, context):
    self.layout.operator(THREE_POINT_LIGHT.bl_idname)

def register():
    bpy.utils.register_class(PIE_MENU_SIMPLE_LIGHT)
    bpy.utils.register_class(PIE_MENU_SIMPLE_LIGHT_CALL)
    bpy.utils.register_class(THREE_POINT_LIGHT)
    bpy.types.VIEW3D_MT_add.append(menu_func)
    add_hotkey()

def unregister():
    bpy.utils.unregister_class(PIE_MENU_SIMPLE_LIGHT)
    bpy.utils.unregister_class(PIE_MENU_SIMPLE_LIGHT_CALL)
    bpy.utils.unregister_class(THREE_POINT_LIGHT)
    bpy.types.VIEW3D_MT_add.remove(menu_func)
    remove_hotkey()

if __name__ == "__main__":
    register()