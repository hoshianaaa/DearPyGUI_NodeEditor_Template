import dearpygui.dearpygui as dpg
from random import randint


# Add simple input node for an int value with hard coded ID "1"
def add_node_output_float(user_data):
    # Create random ID and check that the ID does not exist yet for this node type
    random_id = randint(0, 50000)
    while dpg.does_item_exist(str(random_id) + "!Node_Addition"):
        random_id = randint(0, 50000)

    # Simple result node for an int value with hard coded ID "3"
    with dpg.node(tag=str(random_id) + "!Node_Result",
                  parent="NodeEditor",
                  label="Result",
                  pos=user_data):
        with dpg.node_attribute(tag=str(random_id) + "!Node_Result_Input"):
            dpg.add_group(tag=str(random_id) + "!TextGroup", width=100)
            dpg.add_input_text(tag=str(random_id) + "!Node_Result_Input_value",
                               default_value="None",
                               enabled=False,
                               label="Result")