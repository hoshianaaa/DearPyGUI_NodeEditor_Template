# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

import dearpygui.dearpygui as dpg
from src.nodes.node_calculation import node_calculation


LinkList = []


# Function for updating all interconnected nodes if a link was created or a value has changed
def func_chain_update(sender, data):
    # If a link has changed (tuple "data" has 2 values)
    if type(data) == tuple:
        dpg.add_node_link(data[0], data[1], parent=sender)
        print("Following link was created or value changed:\nSender: " + str(sender) + "\nData: " + str(data))

        LinkList.append(data)

        # Move value between the new link
        dpg.set_value((data[1] + "_value"), dpg.get_value(data[0] + "_value"))
        # Disable connected input socket to prevent manual changes
        dpg.disable_item(data[1] + "_value")
        following_nodes = [data[1].split("!")]
    else:
        following_nodes = [sender.split("!")]

    # "following_nodes" contains the IDs of the nodes which are connected.
    # The list of connected nodes is modified inside the loop, if further connections are found.
    # The loop runs through all nodes which are connected, moves values between nodes and updates the nodes,
    # until he reaches the chain end (nodes without further connections).
    print("following_nodes at chain calculation start: " + str(following_nodes))
    print("Link list: " + str(LinkList))

    infinite_loop_check_list = []

    while following_nodes:
        # Checking if following node was already processed in this update
        # If yes, an infinite loop was created with the last connected link
        if following_nodes[0][0] in infinite_loop_check_list:
            dpg.set_value("InfoBar", "Exception: Infinite loop !")
            # Searching the item ID of the connected link
            # TODO: Better implementation without checking all items of the app but currently no
            #  good function in Dearpygui is available
            for item in dpg.get_all_items():
                # Checking the item has the link attribute "attr_1"
                if "attr_1" in dpg.get_item_configuration(item):
                    if dpg.get_item_configuration(item)["attr_1"] == data[0] and dpg.get_item_configuration(item)["attr_2"] == data[1]:
                        # Delete link to destroy infinite loop
                        dpg.delete_item(item)
                        raise Exception("Infinite loop ! Link deleted !")
        # If no, the updated is performed
        else:
            # Add currently processed node to list for checking infinite loop
            infinite_loop_check_list.append(following_nodes[0][0])
            print("Infinite loop check list: " + str(infinite_loop_check_list))

            print("================ Loop pass started ================")

            # Link to node calculation
            # TODO better implementation without hardcoding node funtion calls
            node_calculation(following_nodes)

            # Searching nodes, which are connected with the current node
            # 1. Run through all links
            for connections in LinkList:
                # 2. Extract ID from the starting node of the selected link
                connections_id = connections[0].split("!")
                # 3. Compare with the target node of the current link
                if following_nodes[0][0] == connections_id[0]:
                    print("Found further link ! " + str(connections))
                    # Move values to next node
                    # If float, round number
                    if isinstance(dpg.get_value(connections[0] + "_value"), float):
                        dpg.set_value((connections[1] + "_value"), round(dpg.get_value(connections[0] + "_value"), 3))
                    else:  # All other types
                        dpg.set_value((connections[1] + "_value"), dpg.get_value(connections[0] + "_value"))
                    # Add next node ID to list, which is interconnected inside the chain and must be updated
                    following_nodes.append(connections[1].split("!"))
                else:
                    continue

            # Remove ID of the node which was updated just now
            following_nodes.pop(0)
            print("Following nodes at loop end:" + str(following_nodes))
            print("================ Loop pass completed ================")

    del infinite_loop_check_list
    del following_nodes


def func_link_destroyed(sender, data):

    print("Following link was destroyed:\nSender: " + str(sender) +
          "\nData: " + str([dpg.get_item_configuration(data)["attr_1"], dpg.get_item_configuration(data)["attr_2"]]))

    # Enable target slot
    dpg.enable_item(dpg.get_item_configuration(data)["attr_2"] + "_value")
    # Removing the old connection from the LinkList
    LinkList.remove((dpg.get_item_configuration(data)["attr_1"], dpg.get_item_configuration(data)["attr_2"]))
    # Delete link
    dpg.delete_item(data)
