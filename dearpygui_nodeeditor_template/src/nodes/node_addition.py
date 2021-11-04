import dearpygui.dearpygui as dpg
import random
from src.chain_update import func_chain_update


def add_node_addition(user_data):
    # Create random ID and check that the ID does not exist yet for this node type
    random_id = random.randint(0, 50000)
    while dpg.does_item_exist(str(random_id) + "!Node_Addition"):
        random_id = random.randint(0, 50000)

    with dpg.node(tag=(str(random_id) + "!Node_Addition"),
                  parent="NodeEditor",
                  label="Addition",
                  pos=user_data):
        with dpg.node_attribute(tag=str(random_id) + "!Node_Addition_Input1"):
            dpg.add_input_float(tag=str(random_id) + "!Node_Addition_Input1_value",
                                label="Value 1",
                                width=100,
                                default_value=0,
                                callback=func_chain_update)
        with dpg.node_attribute(tag=str(random_id) + "!Node_Addition_Input2"):
            dpg.add_input_float(tag=str(random_id) + "!Node_Addition_Input2_value",
                                label="Value 2",
                                width=100,
                                default_value=0,
                                callback=func_chain_update)
        with dpg.node_attribute(tag=str(random_id) + "!Node_Addition_Output",
                                attribute_type=dpg.mvNode_Attr_Output):
            dpg.add_input_float(tag=str(random_id) + "!Node_Addition_Output_value",
                                label="Result",
                                width=100,
                                default_value=0,
                                readonly=True)
