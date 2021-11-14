# Copyright 2021 LuminousLizard
# Licensed under the MIT-License

from src.node_functions import *


def linking_node_function(node_tag):
    link_dict = {
        "Node_Addition": node_addition_func.calc_addition,
        "Node_Subtraction": node_subtraction_func.calc_subtraction,
        "Multiplication": node_multiplication_func.calc_multiplication,
        "Division": node_division_func.calc_division
    }
    for key in link_dict:
        if key in node_tag[1]:
            link_dict[key](node_tag[0])
