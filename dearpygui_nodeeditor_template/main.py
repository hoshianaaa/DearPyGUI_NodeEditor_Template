# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

from dearpygui.core import *
from dearpygui.simple import *
from node_editor import callback_show_node_editor


def callback_close_program(sender, data):
    exit(0)


def callback_show_debugger(sender, data):
    show_debug()


def callback_show_logger(sender, data):
    show_logger()


with window("MainWindow",
            x_pos=0,
            y_pos=0,
            width=700,
            height=200):

    set_theme("Cherry")
    set_main_window_size(1500, 900)
    add_additional_font("dearpygui_nodeeditor_template/fonts/OpenSans-Regular.ttf", 20)

    with menu_bar("MainMenuBar"):
        with menu("Node editor"):
            add_menu_item("Open a new node editor", callback=callback_show_node_editor)
        add_menu_item("Debugger", callback=callback_show_debugger)
        add_menu_item("Logger", callback=callback_show_logger)

        add_menu_item("Close", callback=callback_close_program)

    add_text("Start a node editor from the menu bar.\n"
             "Nodes (here only one) can be added via the menu bar or context menu (right mouse click).\n"
             "Scrolling is possible via middle mouse button.\n"
             "See \"node_editor.py\" how it works, I have written in some comments.")

start_dearpygui()
