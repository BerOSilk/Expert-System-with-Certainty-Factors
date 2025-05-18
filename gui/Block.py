"""
Block module for GUI components.
This module defines the Block class which represents a single input block in the GUI,
consisting of a label and an entry field with its associated variable.
"""

from tkinter import *

class Block:
    """
    A class representing a single input block in the GUI.
    
    Each block consists of:
    - A key identifier
    - A label widget
    - An entry widget
    - A StringVar for the entry's value
    
    Attributes:
        key (str): The identifier for this block
        label (Label): The tkinter Label widget
        entry (Entry): The tkinter Entry widget
        entryVar (StringVar): The variable associated with the entry widget
    """

    def __init__(self, block_id: str, label_widget: Label, entry_widget: Entry, entry_variable: StringVar):
        """
        Initialize a new Block instance.
        
        Args:
            block_id (str): The identifier for this block
            label_widget (Label): The tkinter Label widget
            entry_widget (Entry): The tkinter Entry widget
            entry_variable (StringVar): The variable associated with the entry widget
        """
        self.key      = block_id
        self.label    = label_widget
        self.entry    = entry_widget
        self.entryVar = entry_variable
        
        # Configure the entry widget to use the StringVar
        self.entry.config(textvariable=self.entryVar)