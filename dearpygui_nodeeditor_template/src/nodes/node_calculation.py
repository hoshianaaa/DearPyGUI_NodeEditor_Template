import dearpygui.dearpygui as dpg


# TODO better implementation without hardcoding node funtion calls
def node_calculation(following_nodes):
    # If a following node is a operation node, the respective function is triggered to updating the values
    if "Node_Addition" in following_nodes[0][1]:
        calc_addition(following_nodes[0][0])
    if "Node_Subtraction" in following_nodes[0]:
        pass  # func_subtraction(following_nodes[0][0])


# Function of the "addition" node
def calc_addition(node_id):
    # Input + Static = Output
    addition_result = round(dpg.get_value(node_id + "!Node_Addition_Input1_value") +
                            dpg.get_value(node_id + "!Node_Addition_Input2_value"), 3)
    # Calculated value is set to the output socket
    dpg.set_value((node_id + "!Node_Addition_Output_value"), addition_result)