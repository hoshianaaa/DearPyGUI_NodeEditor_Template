# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

import dearpygui.dearpygui as dpg
import random
from src.chain_update import func_chain_update


class AddNodeAddition:
    def __init__(self, user_data):

        self.node_type = "!Node_Addition"
        self.slot_number = 2

        # Create random ID and check that the ID does not exist yet for this node type
        self.random_id = random.randint(0, 50000)
        while dpg.does_item_exist(str(self.random_id) + self.node_type):
            self.random_id = random.randint(0, 50000)

        with dpg.node(tag=(str(self.random_id) + self.node_type),
                      parent="NodeEditor",
                      label="Addition",
                      pos=user_data):
            with dpg.node_attribute(tag=str(self.random_id) + self.node_type + "_Slot",
                                    attribute_type=dpg.mvNode_Attr_Static):
                dpg.add_input_int(tag=str(self.random_id) + self.node_type + "Slot_number",
                                  label="Slot number",
                                  width=100,
                                  callback=self.add_slots,
                                  min_value=2,
                                  min_clamped=True,
                                  max_value=10,
                                  max_clamped=True,
                                  default_value=2)
            with dpg.node_attribute(tag=str(self.random_id) + self.node_type + "_Input1"):
                dpg.add_input_float(tag=str(self.random_id) + self.node_type + "_Input1_value",
                                    label="Value 1",
                                    width=100,
                                    default_value=0,
                                    callback=func_chain_update)
            with dpg.node_attribute(tag=str(self.random_id) + self.node_type + "_Input2"):
                dpg.add_input_float(tag=str(self.random_id) + self.node_type + "_Input2_value",
                                    label="Value 2",
                                    width=100,
                                    default_value=0,
                                    callback=func_chain_update)
            with dpg.node_attribute(tag=str(self.random_id) + self.node_type + "_Output",
                                    attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_input_float(tag=str(self.random_id) + self.node_type + "_Output_value",
                                    label="Result",
                                    width=100,
                                    default_value=0,
                                    readonly=True)

    def add_slots(self, sender, app_data):
        print(app_data)
        if app_data < self.slot_number:
            dpg.delete_item(str(self.random_id) + self.node_type + "_Input" + str(self.slot_number) + "_value")
            dpg.delete_item(str(self.random_id) + self.node_type + "_Input" + str(self.slot_number))
            self.slot_number -= 1
            func_chain_update(sender=str(self.random_id) + self.node_type, data=0)
        else:
            with dpg.node_attribute(tag=str(self.random_id) + self.node_type + "_Input" + str(app_data),
                                    parent=str(self.random_id) + self.node_type,
                                    before=str(self.random_id) + self.node_type + "_Output"):
                dpg.add_input_float(tag=str(self.random_id) + self.node_type + "_Input" + str(app_data) + "_value",
                                    label="Value " + str(app_data),
                                    width=100,
                                    default_value=0,
                                    callback=func_chain_update)
            self.slot_number += 1
