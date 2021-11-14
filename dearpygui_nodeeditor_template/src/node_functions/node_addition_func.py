# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

import dearpygui.dearpygui as dpg


# Function of the "addition" node
def calc_addition(node_id):
    result = 0
    for i in range(1, 11):
        if dpg.does_item_exist(node_id + "!Node_Addition_Input" + str(i) + "_value"):
            result += round(dpg.get_value(node_id + "!Node_Addition_Input" + str(i) + "_value"), 3)
        else:
            break
    # Calculated value is set to the output socket
    dpg.set_value((node_id + "!Node_Addition_Output_value"), result)
