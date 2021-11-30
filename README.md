# DearPyGUI NodeEditor Template

A node editor template using DearPyGUI.

It's intended as a demonstration and template for anyone who would like to create a node editor with DearPyGUI. It is licensed under the MIT licenses, so anyone can copy it and extend it as they wish. It contains the most functions needed for building an own node editor with DearPyGUI:

* Structure of a DearPyGUI program
* Structure of nodes (widgets, input and output sockets)
* Nodes with a variable number of input sockets
* Adding nodes at the position of the last selected node
* Giving nodes a function
* Update function (chain update) to update all following nodes if a new link was applied or a value was changed
* Using callbacks
* Using random IDs (together with ID checks) to create theoreticaly infinite widgets and nodes without ID overlapping
* Menu bar for adding nodes and/or other possible options

## Requiremens
* Python 3.9 (maybe other Python 3 versions also work)
* Poetry >=1.1.11 (as package manager)
    * DearPyGUI = 1.0.2

## Usage
- Download or clone repository
- Inside the folder with the main.py run `poetry install` to create a virtualenv and install dependencies (DearPyGUI)
- Execute via `poetry run python3 main.py`

## License
MIT-License