"""
Expert module for the Expert System.
This module defines the Expert class which implements the core logic of the expert system,
including rule evaluation and certainty factor calculations.
"""

from .Rule import Rule

class Expert:
    """
    A class representing the expert system's core logic.
    
    The Expert class handles:
    - Rule management
    - Evidence and hypothesis tracking
    - Certainty factor calculations
    - Rule evaluation
    
    Attributes:
        rules (list[Rule]): List of rules in the expert system
        fact_cf (dict): Dictionary storing certainty factors for facts
    """

    def __init__(self, rule_list: list[Rule]):
        """
        Initialize a new Expert instance.
        
        Args:
            rule_list (list[Rule]): List of rules to be used by the expert system
        """
        self.rules    = rule_list
        self.fact_cf = {}
    
    def getEvidence(self) -> list[str]:
        """
        Get all evidence statements from the rules.
        
        Returns:
            list[str]: List of evidence statements from all rules
        """
        evidence_list = []
        for rule in self.rules:
            evidence_list.append(rule.evidence)
        return evidence_list
    
    def getHypothesis(self) -> list[str]:
        """
        Get all hypothesis statements from the rules.
        
        Returns:
            list[str]: List of hypothesis statements from all rules
        """
        hypothesis_list = []
        for rule in self.rules:
            hypothesis_list.append(rule.hypothesis)
        return hypothesis_list

    @staticmethod
    def evaluate_cf_expression(rule_expression: str, evidence_certainty_factors: dict):
        """
        Evaluate a rule expression using certainty factors.
        
        This method processes a rule string containing AND/OR operators and evaluates
        the certainty factor based on the provided evidence certainty factors.
        
        Args:
            rule_expression (str): The rule expression to evaluate
            evidence_certainty_factors (dict): Dictionary mapping evidence to their certainty factors
            
        Returns:
            float: The calculated certainty factor for the rule expression
        """
        result_cf = -2
        current_evidence = ""
        rule_expression = rule_expression.strip()
        operator_flag = 0
        last_operator_flag = 0
        operator_count = 0
        
        for char_index in range(len(rule_expression)):
            if rule_expression[char_index] == ' ':
                if current_evidence.endswith(" AND"):
                    last_operator_flag = operator_flag
                    operator_flag = 1
                    operator_count = 1
                elif current_evidence.endswith(" OR"):
                    last_operator_flag = operator_flag
                    operator_flag = -1
                    operator_count = 1
                
                if operator_flag != 0 and operator_count == 1:
                    try:
                        current_evidence = current_evidence[:-(3 if operator_flag == 1 else 2)]
                        if evidence_certainty_factors[current_evidence] <= 0:
                            return 0
                        if result_cf == -2:
                            result_cf = evidence_certainty_factors[current_evidence]
                        elif last_operator_flag == 1:
                            result_cf = min(result_cf, evidence_certainty_factors[current_evidence])
                        elif last_operator_flag == -1:
                            result_cf = max(result_cf, evidence_certainty_factors[current_evidence])
                        current_evidence = ""
                        operator_count = 0
                    except Exception as error:
                        return result_cf
                else:
                    current_evidence += rule_expression[char_index]
            else:
                current_evidence += rule_expression[char_index]

        evidence_key = current_evidence + ' ' if not current_evidence.endswith(' ') else ''
        if evidence_certainty_factors[evidence_key] <= 0:
            return 0
        if result_cf == -2:
            result_cf = evidence_certainty_factors[evidence_key]
        elif operator_flag == 1:
            result_cf = min(result_cf, evidence_certainty_factors[evidence_key])
        elif operator_flag == -1:
            result_cf = max(result_cf, evidence_certainty_factors[evidence_key])
        return result_cf

    def evaluate_fact_cf(self, fact_statement: str, new_certainty_factor: float):
        """
        Evaluate and update the certainty factor for a fact.
        
        This method implements the certainty factor combination rules:
        - For positive CFs: CF = CF1 + CF2 * (1 - CF1)
        - For negative CFs: CF = CF1 + CF2 * (1 + CF1)
        - For mixed CFs: CF = (CF1 + CF2) / (1 - min(|CF1|, |CF2|))
        
        Args:
            fact_statement (str): The fact to evaluate
            new_certainty_factor (float): The new certainty factor to combine
            
        Returns:
            float: The updated certainty factor for the fact
        """
        if fact_statement not in self.fact_cf:
            self.fact_cf[fact_statement] = new_certainty_factor
        else:
            existing_cf = self.fact_cf[fact_statement]
            if existing_cf > 0 and new_certainty_factor > 0:
                self.fact_cf[fact_statement] = existing_cf + (new_certainty_factor * (1 - existing_cf))
            elif existing_cf < 0 and new_certainty_factor < 0:
                self.fact_cf[fact_statement] = existing_cf + (new_certainty_factor * (1 + existing_cf))
            else:
                self.fact_cf[fact_statement] = (existing_cf + new_certainty_factor) / (1 - min(abs(existing_cf), abs(new_certainty_factor)))
        return self.fact_cf[fact_statement]

    def evaluate_rule(self, evidence_certainty_factors: dict):
        """
        Evaluate all rules using the provided evidence certainty factors.
        
        This method:
        1. Resets the fact certainty factors
        2. Evaluates each rule's evidence expression
        3. Combines the rule's CF with the evidence CF
        4. Updates the hypothesis CFs
        
        Args:
            evidence_certainty_factors (dict): Dictionary mapping evidence to their certainty factors
            
        Returns:
            dict: Dictionary mapping hypotheses to their final certainty factors
        """
        self.fact_cf = {}
        for rule in self.rules:
            combined_cf = self.evaluate_cf_expression(rule.evidence, evidence_certainty_factors)
            if combined_cf != 0:
                combined_cf = combined_cf * rule.cf
                combined_cf = self.evaluate_fact_cf(rule.hypothesis, combined_cf)
        
        return self.fact_cf

    

    
    