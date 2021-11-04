# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

import dearpygui.dearpygui as dpg
from src.node_editor import NodeEditor

dpg.create_context()
dpg.create_viewport(title="Node Editor Template",
                    width=1500,
                    height=768)


def callback_close_program(sender, data):
    exit(0)


def callback_show_debugger(sender, data):
    dpg.show_debug()


with dpg.font_registry():
    default_font = dpg.add_font("fonts/OpenSans-Regular.ttf", 15)


with dpg.viewport_menu_bar():
    dpg.add_menu_item(label="Debugger", callback=callback_show_debugger)
    dpg.add_menu_item(label="Close", callback=callback_close_program)


with dpg.window(label="MainWindow",
                pos=[50, 50],
                width=700,
                height=200):
    dpg.bind_font(default_font)

    nodeEditor = NodeEditor()


# Main Loop
dpg.show_viewport()
dpg.setup_dearpygui()
dpg.start_dearpygui()
dpg.destroy_context()
