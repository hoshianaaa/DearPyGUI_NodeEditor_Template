import dearpygui.dearpygui as dpg
from src.nodes.node_calculation import node_calculation


LinkList = []


# Function for updating all interconnected nodes if a link was created or a value has changed
def func_chain_update(sender, data):
    # If a link has changed (tuple "data" has 2 values)
    print("Data is: " + str(data))

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
    while following_nodes:
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


def func_link_destroyed(sender, data):

    print("Following link was destroyed:\nSender: " + str(sender) +
          "\nData: " + str([dpg.get_item_configuration(data)["attr_1"], dpg.get_item_configuration(data)["attr_2"]]))

    # Enable target slot
    dpg.enable_item(dpg.get_item_configuration(data)["attr_2"] + "_value")
    # Removing the old connection from the LinkList
    LinkList.remove((dpg.get_item_configuration(data)["attr_1"], dpg.get_item_configuration(data)["attr_2"]))
    # Delete link
    dpg.delete_item(data)
