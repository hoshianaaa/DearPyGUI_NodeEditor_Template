# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

import dearpygui.dearpygui as dpg
from src.chain_update import func_chain_update, func_link_destroyed
from src.nodes import *

LastNodePosition = [100, 100]


# Destroy window if closed
def callback_close_window(sender):
    dpg.delete_item(sender)


class NodeEditor:
    def __init__(self):
        with dpg.window(tag="NodeEditorWindow",
                        label="Node editor",
                        width=1000,
                        height=700,
                        pos=[50, 100],
                        menubar=True,
                        on_close=callback_close_window):
            # Add a menu bar to the window
            with dpg.menu_bar(label="MenuBar"):
                with dpg.menu(label="Input nodes"):
                    dpg.add_menu_item(tag="Menu_AddNode_InputFloat",
                                      label="Input float",
                                      callback=callback_add_node,
                                      user_data="Input_Float")
                    dpg.add_menu_item(tag="Menu_AddNode_OutputFloat",
                                      label="Output_Float",
                                      callback=callback_add_node,
                                      user_data="Output_Float")

                with dpg.menu(label="Math nodes"):
                    dpg.add_menu_item(tag="Menu_AddNode_Addition",
                                      label="Addition",
                                      callback=callback_add_node,
                                      user_data="Addition")

            # Add node editor to the window
            with dpg.node_editor(tag="NodeEditor",
                                 # Function call for updating all nodes if a new link is created
                                 callback=func_chain_update,
                                 # Function call for updating if a link is destroyed
                                 delink_callback=func_link_destroyed):
                pass

            with dpg.handler_registry():
                dpg.add_mouse_click_handler(callback=save_last_node_position)
        # End note editor


def save_last_node_position():
    global LastNodePosition
    if dpg.get_selected_nodes("NodeEditor") == []:
        print("Old position: {}".format(LastNodePosition))
    else:
        LastNodePosition = dpg.get_item_pos(dpg.get_selected_nodes("NodeEditor")[0])
        print("Node position {} saved !".format(dpg.get_item_pos(dpg.get_selected_nodes("NodeEditor")[0])))


def callback_add_node(sender, app_data, user_data):
    function_dict = {
        "Addition": node_addition.add_node_addition,
        "Input_Float": node_input_float.add_node_input_float,
        "Output_Float": node_output_float.add_node_output_float
    }
    function_dict[user_data](LastNodePosition)
