"""
The default hot key is "L", you can use it to open the pie menu.
"""


import bpy
from bpy.types import Menu


bl_info = {
    "name": "Colorful Python Logo",
    "author": "Rain Wu <s0958334772@gmail.com>",
    "version": (1, 0, 0),
    "description": "Change colors on Python logo conveniently.",
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
    kmi = km.keymap_items.new(PieMenuColorfulCall.bl_idname, 'L', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))


def remove_hotkey():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()


class PieMenuColorful(Menu):
    bl_label = 'Change Python Color'

    def draw(self, context):
        layout = self.layout
        prefs = context.preferences
        inputs = prefs.inputs

        # pie menu options assignment
        pie = layout.menu_pie()
        pie.operator("object.common_color")
        pie.operator("object.cyberpunk_color")
        pie.operator("object.error_color")


class PieMenuColorfulCall(bpy.types.Operator):
    bl_idname = 'object.colorful'
    bl_label = 'colorful python logo'
    bl_description = 'change the colors on Python logo.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        # draw pie menu while execute
        bpy.ops.wm.call_menu_pie(name="PieMenuColorful")

        return {'FINISHED'}

# give python logo common color
class CommonColor(bpy.types.Operator):
    bl_idname = "object.common_color"
    bl_label = "Common"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.data.materials["Top"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0, 0.312, 0.8, 1)
        bpy.data.materials["Down"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.661, 0, 1)
        return {"FINISHED"}


# give python logo cyberpunk color
class CyberpunkColor(bpy.types.Operator):
    bl_idname = "object.cyberpunk_color"
    bl_label = "Cyberpunk"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.data.materials["Top"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.5, 0, 0.8, 1)
        bpy.data.materials["Down"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0, 0.8, 0.4, 1)
        return {"FINISHED"}


# give python logo error color
class ErrorColor(bpy.types.Operator):
    bl_idname = "object.error_color"
    bl_label = "Error"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.data.materials["Top"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0, 0, 1)
        bpy.data.materials["Down"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.15, 0.15, 1)
        return {"FINISHED"}

# register class
def register():
    bpy.utils.register_class(PieMenuColorful)
    bpy.utils.register_class(PieMenuColorfulCall)
    bpy.utils.register_class(CommonColor)
    bpy.utils.register_class(CyberpunkColor)
    bpy.utils.register_class(ErrorColor)
    add_hotkey()


# unregister class
def unregister():
    bpy.utils.unregister_class(PieMenuColorful)
    bpy.utils.unregister_class(PieMenuColorfulCall)
    bpy.utils.unregister_class(CommonColor)
    bpy.utils.unregister_class(CyberpunkColor)
    bpy.utils.unregister_class(ErrorColor)
    remove_hotkey()


# auto register while run script
if __name__ == "__main__":
    register()