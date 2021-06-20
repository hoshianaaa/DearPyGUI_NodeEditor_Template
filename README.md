# DearPyGUI NodeEditor Template

A node editor template using DearPyGUI.

It's intended as a demonstration and template for anyone who would like to create a node editor with DearPyGUI. It is licensed under the MIT licenses, so anyone can copy it and extend it as they wish. It contains the most functions needed for building an own node editor with DearPyGUI:

* Structure of a DearPyGUI program
* Structure of nodes (widgets, input and output sockets)
* Giving nodes a function
* Update function (chain update) to update all follwing nodes if a new link was applied or a value was changed
* Using callbacks
* Using random IDs (together with ID checks) to create theoreticaly infinite windows, widgets and nodes without ID overlapping
* Context menu (right mouse click modal popup) for adding nodes and/or other possible options
* Menu bar for adding nodes and/or other possible options

## Requiremens
* Python 3.9 (maybe other Python 3 versions also work)
* Poetry >=1.0.0 (as package manager)
    * DearPyGUI = ^0.6.415

## Usage
- Download or clone repository
- Execute via `poetry run python3 dearpygui_nodeeditor_template/main.py`

## Help
Any help in the form of comments, improvements or extensions are welcome.

## Credits:
Owner and developer: LuminousLizard

## License
MIT-License