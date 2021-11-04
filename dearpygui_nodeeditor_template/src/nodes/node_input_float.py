# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

import dearpygui.dearpygui as dpg
from random import randint
from src.chain_update import func_chain_update


# Add simple input node for an int value with hard coded ID "1"
def add_node_input_float(user_data):
    # Create random ID and check that the ID does not exist yet for this node type
    random_id = randint(0, 50000)
    while dpg.does_item_exist(str(random_id) + "!Node_Addition"):
        random_id = randint(0, 50000)

    with dpg.node(tag=str(random_id) + "!Node_InputFloat",
                  parent="NodeEditor",
                  label="Input float",
                  pos=user_data):
        with dpg.node_attribute(tag=str(random_id) + "!Node_InputFloat_Output", attribute_type=dpg.mvNode_Attr_Output):
            dpg.add_input_float(tag=str(random_id) + "!Node_InputFloat_Output_value",
                                label="Float value",
                                width=150,
                                default_value=0,
                                callback=func_chain_update)
