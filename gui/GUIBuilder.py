"""
GUI Builder module for the Expert System.

This module implements a modern, user-friendly graphical interface for the expert system.
It provides an intuitive way for users to:
- Input evidence with certainty factors
- View real-time hypothesis results
- Understand the system's reasoning through visual feedback

The interface features:
- Clear input validation for certainty factors (-1 to 1)
- Real-time calculation of complementary values
- Color-coded results for easy interpretation
- Responsive layout that adapts to the number of rules
- Modern styling with consistent fonts and colors

Author: Baraa AbuKhalil
Copyright © 2025 Baraa AbuKhalil. All rights reserved.
"""

from tkinter import *
from tkinter import ttk
from expert.Expert import Expert
from .Block import Block

class GUIBuilder:
    """
    The builder of the GUI for the expert system.
    
    This class creates and manages a modern, user-friendly interface that allows users to:
    1. Input evidence with certainty factors
    2. View real-time hypothesis results
    3. Understand the system's reasoning through visual feedback
    
    The interface is built using tkinter and features:
    - Modern styling with consistent fonts and colors
    - Real-time validation and calculation
    - Responsive layout that adapts to content
    - Clear visual hierarchy and organization
    
    Attributes:
        expert (Expert): The expert system instance that processes the rules and evidence
        evidenceFirsts (dict): Dictionary storing evidence input blocks, organized by evidence type
        hypothesisFirsts (dict): Dictionary storing hypothesis display blocks, organized by hypothesis type
        resultLabels (dict): Dictionary storing result labels for each hypothesis
        root (Tk): The root window of the GUI application
    """
    
    def __init__(self, expert: Expert):
        """
        Initialize a new GUIBuilder instance.
        
        Sets up the main window and configures the initial styling and layout.
        The window is configured with a modern look and feel, including:
        - Light gray background for reduced eye strain
        - Consistent font family (Segoe UI) for better readability
        - Fixed window size to prevent layout issues
        - Modern color scheme for visual elements
        
        Args:
            expert (Expert): The expert system instance to use for processing rules and evidence
        """
        self.expert           = expert
        self.evidenceFirsts   = {}
        self.hypothesisFirsts = {}
        self.resultLabels     = {}
        self.root             = Tk()
        
        # Configure the root window
        self.root.title("Expert System")
        self.root.configure(bg='#f0f0f0')  # Light gray background
        self.root.resizable(0, 0)  # Prevent window resizing to maintain layout integrity
        
        # Configure styles for consistent look and feel
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Segoe UI', 10), background='#f0f0f0')
        self.style.configure('TEntry', font=('Segoe UI', 10))
        self.style.configure('Header.TLabel', font=('Segoe UI', 12, 'bold'), background='#f0f0f0')
        self.style.configure('Info.TLabel', font=('Segoe UI', 10, 'italic'), background='#f0f0f0', foreground='#666666')

        self.root.geometry(self.calculateGeometry())
        self.build()

    def calculateGeometry(self) -> str:
        """
        Calculate the window geometry based on the number of rules.
        
        The window height is dynamically calculated to accommodate:
        - Title and input range information (60px)
        - Section headers (40px)
        - Evidence and hypothesis sections (50px per rule)
        - Copyright notice (50px)
        - Additional padding (50px)
        
        Returns:
            str: The window geometry string in the format 'WIDTHxHEIGHT'
        """
        return '800x' + str(len(self.expert.rules) * 50 + 250)  # Increased height to accommodate copyright
    
    def build(self) -> None:
        """
        Build the complete GUI layout.
        
        This method constructs the entire interface, including:
        1. Title and input range information
        2. Section headers for evidence and hypothesis
        3. Evidence input section with validation
        4. Hypothesis display section with real-time updates
        5. Copyright notice
        
        The layout is organized with:
        - Clear visual hierarchy
        - Consistent spacing and alignment
        - Modern styling and colors
        - Responsive positioning
        """
        # Add title with modern styling
        title_label = Label(
            self.root,
            text="Expert System",
            font=('Segoe UI', 16, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.place(x=10, y=10)

        # Add input range information with helpful context
        input_range_label = Label(
            self.root,
            text="Input Range: -1 (Definitely False) to 1 (Definitely True)",
            font=('Segoe UI', 10),
            bg='#f0f0f0',
            fg='#2980b9'
        )
        input_range_label.place(x=10, y=45)

        # Add section headers with clear visual separation
        evidence_header = Label(
            self.root,
            text="Evidence Input",
            font=('Segoe UI', 12, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        evidence_header.place(x=10, y=80)

        hypothesis_header = Label(
            self.root,
            text="Hypothesis Results",
            font=('Segoe UI', 12, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        hypothesis_header.place(x=400, y=80)

        # Get and process evidence and hypothesis lists
        evidences = self.expert.getEvidence()
        hypothesis = self.expert.getHypothesis()

        # Build the main sections
        self.buildEvidence(evidences)
        self.buildHypothesis(hypothesis)

        # Create result labels for each hypothesis
        for hypo in hypothesis:
            self.resultLabels[hypo] = Label(
                self.root,
                font=('Segoe UI', 10),
                bg='#f0f0f0',
                fg='#2c3e50'
            )
        
        # Position result labels
        baseX = 400
        baseY = 120
        for label in self.resultLabels.values():
            label.place(x=baseX, y=baseY)
            baseY += 30

        # Add copyright notice
        copyright_label = Label(
            self.root,
            text="© 2025 Baraa AbuKhalil. All rights reserved.",
            font=('Segoe UI', 8),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        copyright_label.place(x=10, y=len(self.expert.rules) * 50 + 200)

    @staticmethod
    def is_valid_cf(new_value: str) -> bool:
        """
        Validates if the input is a valid Certainty Factor.
        
        Certainty Factors (CF) must be between -1 and 1, where:
        -1 means completely false
        0 means uncertain
        1 means completely true
        
        The validation allows for:
        - Empty string (for backspace)
        - Minus sign (for negative numbers)
        - Decimal point (for fractional values)
        - Partial input during typing
        
        Args:
            new_value (str): The value to validate
            
        Returns:
            bool: True if the value is a valid CF, False otherwise
        """
        if new_value in ("", "-", ".", "-."):
            return True
        try:
            new_value = float(new_value)
            if -1 <= new_value <= 1:
                return True
            return False
        except ValueError:
            return False

    def calculate_complementary_cf(self, cf_value: str, self_entry: Entry, target_evidence: str, key) -> None:
        """
        Calculates the complementary Certainty Factor for related evidence.
        
        When a user inputs a CF value, this method calculates the complementary
        value for related evidence statements. The calculation follows these rules:
        - If CF = 1: complementary = -1
        - If CF = -1: complementary = 1
        - If CF > 0: complementary = -1 + CF
        - If CF < 0: complementary = 1 + CF
        
        The complementary value is then distributed among related evidence
        statements to maintain consistency in the system.
        
        Args:
            cf_value (str): The current CF value being entered
            self_entry (Entry): The entry widget being modified
            target_evidence (str): The evidence being modified
            key: The key for the evidence block
        """
        try:
            # Preserve decimal places for consistency
            decimal_places = 0
            if '.' in cf_value:
                decimal_places = len(cf_value.split('.')[1])

            cf_value = float(cf_value)
            if cf_value <= 0:
                return 
            if cf_value == 1:
                complementary_cf = -1
            elif cf_value in [-1, 0]:
                complementary_cf = 1
            else:
                complementary_cf = 1 + cf_value if cf_value < 0 else -1 + cf_value
                
            complementary_cf = round(complementary_cf, decimal_places)
            length = len(self.evidenceFirsts[target_evidence]) - 1
            for val in self.evidenceFirsts[target_evidence].values():
                if val.entry in [self.root.focus_get(), self_entry]:
                    continue
                val.entry.delete(0, END)
                val.entry.insert(0, str(complementary_cf / length))
        except ValueError:
            pass

    @staticmethod
    def translateCF(cf_value):
        """
        Translates a certainty factor value into a human-readable string.
        
        This method converts numerical CF values into natural language
        descriptions to help users understand the system's confidence
        in each hypothesis. The translation follows this scale:
        
        CF Value    | Description
        ------------|------------
        1.0         | Definitely
        0.8 - 0.99  | Almost certainly
        0.6 - 0.79  | Probably
        0.4 - 0.59  | Maybe
        -0.2 - 0.39 | Unknown if
        -0.4 - -0.21| Maybe not
        -0.6 - -0.41| Probably not
        -0.99 - -0.61| Almost certainly not
        -1.0        | Definitely not
        
        Args:
            cf_value (float): The certainty factor value to translate
            
        Returns:
            str: A human-readable description of the certainty
        """
        if cf_value == 1:
            return "Definitely"
        elif cf_value >= 0.8:
            return "Almost certainly"
        elif cf_value >= 0.6:
            return "Probably"
        elif cf_value >= 0.4:
            return "Maybe"
        elif cf_value >= -0.2:
            return "Unknown if"
        elif cf_value >= -0.4:
            return "Maybe not"
        elif cf_value >= -0.6:
            return "Probably not"
        elif cf_value > -1:
            return "Almost certainly not"
        return "Definitely not"

    def calculate_facts_cf(self):
        """
        Calculate and update the certainty factors for all facts.
        
        This method processes all evidence inputs and updates the hypothesis
        results in real-time. It:
        1. Collects all evidence statements and their CF values
        2. Validates and converts input values
        3. Evaluates rules using the expert system
        4. Updates hypothesis displays with results
        5. Applies color coding to results:
           - Green for positive CF (likely true)
           - Red for negative CF (likely false)
           - Gray for neutral CF (uncertain)
        """
        evidences: list[str] = self.expert.getEvidence()

        # Process evidence statements
        lastEvidence = []
        for evidence in evidences:
            l = (evidence.split('AND'))
            for val in l:
                val = (val.split('OR'))
                for x in val:
                    lastEvidence.append(x)
                    
        # Collect CF values from input fields
        evidence_cfs = {}
        for key in self.evidenceFirsts.keys():
            for key1 in self.evidenceFirsts[key].keys():
                cf = self.evidenceFirsts[key][key1].entryVar.get()
                if key1.startswith(' '):
                    key1 = key1[1:]
                evidence_cfs[key1] = cf
                
        # Validate and convert CF values
        for key in evidence_cfs.keys():
            if evidence_cfs[key] == '':
                evidence_cfs[key] = 0
            elif evidence_cfs[key] == '-':
                return
            else:
                evidence_cfs[key] = float(evidence_cfs[key])
                
        # Evaluate rules and update results
        x = self.expert.evaluate_rule(evidence_cfs)
        for key in self.hypothesisFirsts.keys():
            for key1 in self.hypothesisFirsts[key]:
                block = self.hypothesisFirsts[key][key1]
                block.entry.config(state="normal")
                block.entry.delete(0, END)
                cf_value = (round(x[key1], 2)) if key1 in x else 0.0
                block.entry.insert(0, str(cf_value))
                
                # Update result label with color coding
                self.resultLabels[key1].config(
                    text=key1 + " " + self.translateCF(cf_value) + " Will happen",
                    fg='#27ae60' if cf_value > 0 else '#c0392b' if cf_value < 0 else '#7f8c8d'
                )
                block.entry.config(state="readonly")

    def buildEvidence(self, evidences: list[str]):
        """
        Build the evidence input section of the GUI.
        
        This method creates the input fields for evidence statements, including:
        - Labels for evidence types and statements
        - Entry fields with real-time validation
        - Automatic calculation of complementary values
        - Real-time updates of hypothesis results
        
        The layout is organized with:
        - Clear grouping of related evidence
        - Consistent spacing and alignment
        - Modern styling and colors
        - Responsive positioning
        
        Args:
            evidences (list[str]): List of evidence statements to create input fields for
        """
        baseX = 10
        baseY = 120  # Increased to make room for headers

        # Set up validation command for CF input
        vcmd = (self.root.register(self.is_valid_cf), "%P")

        # Process evidence statements
        lastEvidence = []
        for evidence in evidences:
            l = (evidence.split('AND'))
            for val in l:
                val = (val.split('OR'))
                for x in val:
                    lastEvidence.append(x)

        # Create input fields for each evidence statement
        for evidence in lastEvidence:
            evid = evidence.split('is')
            if not evid[0] in self.evidenceFirsts:
                self.evidenceFirsts[evid[0]] = {}
            if not evidence in self.evidenceFirsts[evid[0]]:
                # Create styled widgets
                label = Label(
                    self.root,
                    text=evid[1],
                    font=('Segoe UI', 10),
                    bg='#f0f0f0',
                    fg='#2c3e50'
                )
                entry = Entry(
                    self.root,
                    validate="key",
                    validatecommand=vcmd,
                    font=('Segoe UI', 10),
                    width=10
                )
                self.evidenceFirsts[evid[0]][evidence] = Block(evid[0], label, entry, StringVar())

        # Position and configure evidence input fields
        lastEvidence = ""
        for val in self.evidenceFirsts.values():
            for key,val1 in val.items():
                if val1.key != lastEvidence:
                    label = Label(
                        self.root,
                        text=val1.key,
                        font=('Segoe UI', 10, 'bold'),
                        bg='#f0f0f0',
                        fg='#2c3e50'
                    )
                    lastEvidence = val1.key
                    label.place(x=baseX, y=baseY)
                    baseY += 30
                
                val1.label.place(x=baseX + 10, y=baseY)
                val1.entry.place(x=baseX + 150, y=baseY+2)
                val1.entryVar.trace_add(
                                "write",
                                lambda *args, e=val1.entry ,ev=val1.key, v=val1.entryVar, k=key: self.calculate_complementary_cf(v.get(), e, ev, k)
                            )
                val1.entryVar.trace_add(
                                "write",
                                lambda * args: self.calculate_facts_cf()
                            )

                baseY += 30
    
    def buildHypothesis(self, hypothesis: list[str]):
        """
        Build the hypothesis display section of the GUI.
        
        This method creates the display fields for hypothesis results, including:
        - Labels for hypothesis types and statements
        - Read-only entry fields for CF values
        - Color-coded result labels
        - Real-time updates as evidence changes
        
        The layout is organized with:
        - Clear grouping of related hypotheses
        - Consistent spacing and alignment
        - Modern styling and colors
        - Responsive positioning
        
        Args:
            hypothesis (list[str]): List of hypothesis statements to create display fields for
        """
        baseX = 400
        baseY = 180  # Increased to match evidence section

        # Create display fields for each hypothesis
        for hypo in hypothesis:
            hyp = hypo.split('is')
            if not hyp[0] in self.hypothesisFirsts:
                self.hypothesisFirsts[hyp[0]] = {}
            if not hypo in self.hypothesisFirsts[hyp[0]]:
                # Create styled widgets
                label = Label(
                    self.root,
                    text=hyp[1],
                    font=('Segoe UI', 10),
                    bg='#f0f0f0',
                    fg='#2c3e50'
                )
                entry = Entry(
                    self.root,
                    state="readonly",
                    font=('Segoe UI', 10),
                    width=10
                )
                self.hypothesisFirsts[hyp[0]][hypo] = Block(hyp[0], label, entry, StringVar())
            
        # Position and configure hypothesis display fields
        lastHypothesis = ""
        for val in self.hypothesisFirsts.values():
            for val1 in val.values():
                if val1.key != lastHypothesis:
                    label = Label(
                        self.root,
                        text=val1.key,
                        font=('Segoe UI', 10, 'bold'),
                        bg='#f0f0f0',
                        fg='#2c3e50'
                    )
                    lastHypothesis = val1.key
                    label.place(x=baseX, y=baseY)
                    baseY += 30
                
                val1.label.place(x=baseX + 10, y=baseY)
                val1.entry.place(x=baseX + 150, y=baseY+2)
                baseY += 30
                       