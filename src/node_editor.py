# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

from dearpygui.core import *
from dearpygui.simple import *
import random


LinkList = []
NodeEditorWindowID = 0


# Close function for modal popup (context menu)
def close(sender, data):
    close_popup(data)


# Destroy window if closed
def callback_close_window(sender, data):
    delete_item(sender)


# Function for updating all interconnected nodes if a link was created or a value has changed
def func_chain_update(data):
    global LinkList
    log_debug("Current links: " + str(get_links(str(NodeEditorWindowID) + "!NodeEditor")))

    # Check if a link or a value has been changed
    for connection in get_links(str(NodeEditorWindowID) + "!NodeEditor"):
        # If a link hast changed
        if connection not in LinkList:
            # Move value between the new link
            set_value((connection[1] + "_value"), get_value(connection[0] + "_value"))
            # Disable connected input socket to prevent manual changes
            configure_item((connection[1] + "_value"), enabled=False)
            # Save target socket of the new link for the following chain calculation
            data = connection[1]
            log_debug("Link connected ! Target socket: " + data)

        # If a value of a node has changed or when a link has been created.
        # "following_nodes" contains the IDs of the nodes which are connected.
        # The list of connected nodes is modified inside the loop, if further connections are found.
        # The loop runs through all nodes which are connected, moves values between nodes and updates the nodes,
        # until he reaches the chain end (nodes without further connections).
        following_nodes = [data.split("!")]
        log_debug("Following_nodes at chain calculation start: " + str(following_nodes))
        while following_nodes:
            log_debug("================ Loop pass started ================")
            # Links of ALL nodes to the respective function # TODO maybe a better implementation
            # If a following node is a operation node, the respective function is triggered to updating the values
            if "Node_Addition" in following_nodes[0][1]:
                func_addition(following_nodes[0][0])
            if "Node_Subtraction" in following_nodes[0]:
                pass  # func_subtraction(following_nodes[0][0])

            # Searching nodes, which are connected with the current node
            for next_connection in get_links(str(NodeEditorWindowID) + "!NodeEditor"):
                log_debug(next_connection)
                next_connection_id = next_connection[0].split("!")
                if following_nodes[0][0] == next_connection_id[0]:
                    log_debug("Found further link ! " + str(next_connection))
                    # Move values to next node
                    # If float, round number
                    if isinstance(get_value(next_connection[0] + "_value"), float):
                        set_value((next_connection[1] + "_value"), round(get_value(next_connection[0] + "_value"), 3))
                    else:  # All other types
                        set_value((next_connection[1] + "_value"), get_value(next_connection[0] + "_value"))
                    # Add next node ID to list, which is interconnected inside the chain and must be updated
                    following_nodes.append(next_connection[1].split("!"))
                else:
                    continue
            # Remove ID of the node which was updated just now
            following_nodes.pop(0)
            log_debug("Following nodes at loop end:" + str(following_nodes))
            log_debug("================ Loop pass completed ================")
        # After while loop
        log_debug("================ Chain update completed ================")

    # Save current link list for "link_destroyed" function
    LinkList = get_links(str(NodeEditorWindowID) + "!NodeEditor")


def func_link_destroyed():
    global LinkList
    # Compare old link list with current (modified) link list to identify destroyed link pair
    for old_connections in LinkList:
        if old_connections not in get_links(str(NodeEditorWindowID) + "!NodeEditor"):
            # Configure widgets of the former link pair
            configure_item((old_connections[1] + "_value"), enabled=True)


# Create "addition" node
def add_addition(sender, data):
    # Create random ID and check that the ID does not exist yet for this node type
    random_id = random.randint(0, 50000)
    while is_item_shown(str(random_id) + "!Node_Addition"):
        random_id = random.randint(0, 50000)

    with node(name=(str(random_id) + "!Node_Addition"),
              parent=(str(NodeEditorWindowID) + "!NodeEditor"),
              label="Addition",
              x_pos=500,
              y_pos=200):
        with node_attribute(name=str(random_id) + "!Node_Addition_Input1"):
            add_input_float(name=str(random_id) + "!Node_Addition_Input1_value",
                            label="Value 1",
                            width=100,
                            default_value=0,
                            callback=func_chain_update,
                            callback_data=(str(random_id) + "!Node_Addition_Input1"))
        with node_attribute(name=str(random_id) + "!Node_Addition_Input2"):
            add_input_float(name=str(random_id) + "!Node_Addition_Input2_value",
                            label="Value 2",
                            width=100,
                            default_value=0,
                            callback=func_chain_update)
        with node_attribute(name=str(random_id) + "!Node_Addition_Output", output=True):
            add_input_float(name=str(random_id) + "!Node_Addition_Output_value",
                            label="Result",
                            width=100,
                            default_value=0,
                            readonly=True)
    # If node is added via modal popup (context menu), close popup
    close(sender, "ModalPopup")


# Function of the "addition" node
def func_addition(node_id):
    # Input + Static = Output
    addition_result = round(get_value(node_id + "!Node_Addition_Input1_value") +
                            get_value(node_id + "!Node_Addition_Input2_value"), 3)
    # Calculated value is set to the output socket
    set_value((node_id + "!Node_Addition_Output_value"), addition_result)


# Create window
def callback_show_node_editor(sender, data):
    global NodeEditorWindowID

    # Create random ID and check that the ID does not exist yet for this window
    # It's required to allow multiple windows of the same type
    random_id = random.randint(0, 50000)
    while is_item_shown(str(random_id) + "!NodeEditorWindow"):
        random_id = random.randint(0, 50000)

    # Save ID because it's used by a number of widgets
    NodeEditorWindowID = random_id

    with window(name=(str(random_id) + "!NodeEditorWindow"),
                label="Node editor",
                width=1000,
                height=700,
                x_pos=50,
                y_pos=100,
                menubar=True,
                on_close=callback_close_window):

        with menu_bar("MenuBar"):
            with menu("Add math nodes"):
                add_menu_item("Menu_AddNode_Addition", label="Addition", callback=add_addition)

        # Create node editor
        with node_editor(str(random_id) + "!NodeEditor",
                         link_callback=func_chain_update,
                         delink_callback=func_link_destroyed):
            # Simple input node for an int value with hard coded ID
            with node(name="1!Node_InputFloat",
                      label="Input float",
                      x_pos=50,
                      y_pos=100):
                with node_attribute("1!Node_InputFloat_Output", output=True):
                    add_input_float("1!Node_InputFloat_Output_value",
                                    label="Float value",
                                    width=150,
                                    default_value=0,
                                    callback=func_chain_update)

            # Simple input node for an int value with hard coded ID
            with node(name="2!Node_InputFloat",
                      label="Input Float",
                      x_pos=50,
                      y_pos=200):
                with node_attribute("2!Node_InputFloat_Output", output=True):
                    add_input_float("2!Node_InputFloat_Output_value",
                                    label="Float value",
                                    width=150,
                                    default_value=0,
                                    callback=func_chain_update)

            # Simple result node for an int value with hard coded ID
            with node(name="3!Node_Result",
                      label="Result",
                      x_pos=800,
                      y_pos=150):
                with node_attribute("3!Node_Result_Input"):
                    add_group("1!TextGroup", width=100)
                    add_label_text(name="3!Node_Result_Input_value",
                                   default_value="None",
                                   label="Result")
                    end()  # End group "1!TextGroup"
            # End note editor

        # Add context menu to node editor for adding nodes
        with popup(str(NodeEditorWindowID) + "!NodeEditor", "ModalPopup", modal=True, mousebutton=mvMouseButton_Right):
            add_text("Popup menu")
            with menu("Math"):
                add_menu_item("Popup_AddNode_Addition", label="Addition", callback=add_addition)
