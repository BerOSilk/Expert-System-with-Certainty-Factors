"""
Rule module for the Expert System.
This module defines the Rule class which represents a single rule in the expert system,
consisting of evidence, hypothesis, and a certainty factor.
"""

class Rule:
    """
    A class representing a single rule in the expert system.
    
    Each rule consists of:
    - Evidence: The conditions that must be met
    - Hypothesis: The conclusion that follows
    - Certainty Factor (CF): A value between -1 and 1 indicating the confidence in the rule
    
    Attributes:
        evidence (str): The conditions/evidence part of the rule
        hypothesis (str): The conclusion/hypothesis part of the rule
        cf (float): The certainty factor (-1 to 1) for this rule
    """
    
    def __init__(self, evidence_condition: str, hypothesis_conclusion: str, certainty_factor: float):
        """
        Initialize a new Rule instance.
        
        Args:
            evidence_condition (str): The conditions/evidence part of the rule
            hypothesis_conclusion (str): The conclusion/hypothesis part of the rule
            certainty_factor (float): The certainty factor (-1 to 1) for this rule
        """
        self.evidence   = evidence_condition
        self.hypothesis = hypothesis_conclusion
        self.cf         = certainty_factor