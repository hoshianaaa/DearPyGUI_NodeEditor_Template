# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

import dearpygui.dearpygui as dpg


# Function of the "addition" node
def calc_multiplication(node_id):
    # Input + Static = Output
    result = round(dpg.get_value(node_id + "!Node_Multiplication_Input1_value") *
                   dpg.get_value(node_id + "!Node_Multiplication_Input2_value"), 3)
    # Calculated value is set to the output socket
    dpg.set_value((node_id + "!Node_Multiplication_Output_value"), result)
