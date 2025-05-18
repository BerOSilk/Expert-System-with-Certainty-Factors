"""
Main module for the Expert System application.
This module serves as the entry point for the application and handles the initialization
of the expert system and GUI components.
"""

from expert.Rule import Rule
from expert.Expert import Expert
from gui.GUIBuilder import GUIBuilder

def read_rules():
    """
    Reads the rules from rules.txt file.
    Each rule should be in the format: {evidence} then {hypothesis} \\cf {cf value}
    
    The rules file should contain one rule per line, with the following format:
    - Evidence and hypothesis are separated by 'then'
    - Certainty factor (CF) is specified after '\\cf'
    - Logical operators 'and' and 'or' are automatically converted to uppercase
    
    Returns:
        list[Rule]: A list of Rule objects parsed from the rules file
        
    Raises:
        FileNotFoundError: If rules.txt file is not found
        Exception: For any other errors during file reading or parsing
    """
    rule_list = []
    try:
        with open('rules.txt', 'r') as rules_file:
            for line in rules_file:
                line = line.strip()
                if line and not line.startswith('#'):
                    if 'then' in line and '\\cf' in line:
                        evidence_part, result_part = line.split('then')
                        hypothesis_part, certainty_factor = result_part.split('\\cf')
                        
                        evidence_part = evidence_part.replace(' and ', ' AND ')
                        evidence_part = evidence_part.replace(' or ', ' OR ')
                        
                        rule_list.append(Rule(evidence_part, hypothesis_part, float(certainty_factor)))

    except FileNotFoundError:
        print("rules.txt file not found")
    except Exception as error:
        print(f"Error reading rules: {error}")
    
    return rule_list

def main():
    """
    Main function that initializes and runs the expert system application.
    
    This function:
    1. Reads the rules from rules.txt
    2. Creates an Expert instance with the rules
    3. Initializes the GUI using GUIBuilder
    4. Returns the root window for the application
    
    Returns:
        Tk: The root window of the GUI application
    """
    rule_list = read_rules()
    expert_system = Expert(rule_list)
    gui = GUIBuilder(expert_system)
    return gui.root

if __name__ == "__main__":
    main_window = main()
    main_window.mainloop()
