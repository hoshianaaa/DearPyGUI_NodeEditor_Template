# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

import dearpygui.dearpygui as dpg


# Function of the "subtraction" node
def calc_subtraction(node_id):
    result = round(dpg.get_value(node_id + "!Node_Subtraction_Input1_value") -
                   dpg.get_value(node_id + "!Node_Subtraction_Input2_value"), 3)
    # Calculated value is set to the output socket
    dpg.set_value((node_id + "!Node_Subtraction_Output_value"), result)
