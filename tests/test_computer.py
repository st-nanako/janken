import unittest
from unittest.mock import patch
from source.computer import computer_pon as pon

class TestComputerPon(unittest.TestCase):
   @patch('random.choice')
   def test_input_1(self, mock_choice):
      mock_choice.return_value = "グー"
      self.assertEqual(pon(), "グー")
      
   @patch('random.choice')
   def test_input_2(self, mock_choice):
      mock_choice.return_value = "チョキ"
      self.assertEqual(pon(), "チョキ")
      
   @patch('random.choice')
   def test_input_3(self, mock_choice):
      mock_choice.return_value = "パー"
      self.assertEqual(pon(), "パー")