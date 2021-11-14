# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

import dearpygui.dearpygui as dpg


# Function of the "addition" node
def calc_division(node_id):
    # Input + Static = Output
    if dpg.get_value(node_id + "!Node_Division_Input2_value") == 0:
        dpg.set_value("InfoBar", "Division by zero not possible !")
        raise ValueError()
    else:
        result = round(dpg.get_value(node_id + "!Node_Division_Input1_value") /
                       dpg.get_value(node_id + "!Node_Division_Input2_value"), 3)
        # Calculated value is set to the output socket
        dpg.set_value((node_id + "!Node_Division_Output_value"), result)
