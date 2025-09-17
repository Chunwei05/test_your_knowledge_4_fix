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

class TestCalculatorAddMethod:
    
    def test_add_positive_number(self):
        """Test adding a positive number from initial state"""
        calc = Calculator()
        calc.add(3)
        assert calc.get_answer() == 3
    
    def test_add_negative_number(self):
        """Test adding a negative number from initial state"""
        calc = Calculator()
        calc.add(-2)
        assert calc.get_answer() == -2
    
    def test_add_zero(self):
        """Test adding zero from initial state"""
        calc = Calculator()
        calc.add(0)
        assert calc.get_answer() == 0
    
    def test_add_float_number(self):
        """Test adding a floating point number"""
        calc = Calculator()
        calc.add(2.5)
        assert calc.get_answer() == 2.5

class TestCalculatorSubtractMethod:
    
    def test_subtract_positive_number_from_zero(self):
        """Test subtracting from initial zero state"""
        calc = Calculator()
        calc.subtract(3)
        assert calc.get_answer() == -3
    
    def test_subtract_negative_number_from_zero(self):
        """Test subtracting negative number (equivalent to adding)"""
        calc = Calculator()
        calc.subtract(-2)
        assert calc.get_answer() == 2
    
    def test_subtract_zero(self):
        """Test subtracting zero"""
        calc = Calculator()
        calc.subtract(0)
        assert calc.get_answer() == 0

class TestCalculatorMultiplyMethod:
    
    def test_multiply_positive_number_from_initial_state(self):
        """Test multiplying from initial zero state"""
        calc = Calculator()
        calc.multiply(5)
        assert calc.get_answer() == 0  # 0 * anything = 0
    
    def test_multiply_from_non_zero_state(self):
        """Test multiplying from a non-zero state"""
        calc = Calculator()
        calc.answer = 4  # Set directly for isolation
        calc.multiply(3)
        assert calc.get_answer() == 12
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        calc = Calculator()
        calc.answer = 7  # Set directly for isolation
        calc.multiply(0)
        assert calc.get_answer() == 0
    
    def test_multiply_by_negative(self):
        """Test multiplying by negative number"""
        calc = Calculator()
        calc.answer = 3  # Set directly for isolation
        calc.multiply(-2)
        assert calc.get_answer() == -6

class TestCalculatorPowerMethod:
    
    def test_power_from_initial_state(self):
        """Test raising zero to a power"""
        calc = Calculator()
        calc.power(3)
        assert calc.get_answer() == 0  # 0^anything = 0 (except 0^0, but we'll handle that)
    
    def test_power_from_non_zero_state(self):
        """Test raising a number to a power"""
        calc = Calculator()
        calc.answer = 2  # Set directly for isolation
        calc.power(3)
        assert calc.get_answer() == 8
    
    def test_power_of_zero(self):
        """Test raising to power of 0"""
        calc = Calculator()
        calc.answer = 5  # Set directly for isolation
        calc.power(0)
        assert calc.get_answer() == 1
    
    def test_power_of_one(self):
        """Test raising to power of 1"""
        calc = Calculator()
        calc.answer = 7  # Set directly for isolation
        calc.power(1)
        assert calc.get_answer() == 7

class TestCalculatorMethodChaining:
    
    def test_simple_chaining(self):
        """Test basic method chaining"""
        calc = Calculator()
        calc.add(1).multiply(4).subtract(1)
        assert calc.get_answer() == 3
    
    def test_complex_chaining_operations(self):
        """Test more complex method chaining"""
        calc = Calculator()
        calc.add(10).subtract(3).multiply(2).power(2)
        assert calc.get_answer() == 196  # (10-3)*2 = 14, 14^2 = 196
    
    def test_chaining_with_negative_numbers(self):
        """Test chaining with negative numbers"""
        calc = Calculator()
        calc.add(-5).multiply(-2).subtract(3)
        assert calc.get_answer() == 7  # (-5)*(-2)=10, 10-3=7
    
    def test_reset_in_chain(self):
        """Test reset within a chain"""
        calc = Calculator()
        calc.add(5).multiply(3).reset().add(10)
        assert calc.get_answer() == 10
