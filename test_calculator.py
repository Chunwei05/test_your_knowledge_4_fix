import pytest
from src.calculator import Calculator

class TestCalculatorInitialState:
    
    def test_initial_answer_is_zero(self):
        """Test that a new calculator starts with answer 0"""
        calc = Calculator()
        assert calc.get_answer() == 0

    def test_reset_returns_answer_to_zero(self):
        """Test that reset() returns the answer to 0"""
        calc = Calculator()
        # First change the answer from initial state
        calc.answer = 5  # Directly set for testing reset in isolation
        calc.reset()
        assert calc.get_answer() == 0
