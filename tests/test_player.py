import unittest
from unittest.mock import patch
from source.player import player_pon as pon

class TestPlayerPon(unittest.TestCase):

   @patch('builtins.input')
   def test_input_1(self, mock_input):
      mock_input.return_value = '1'
      self.assertEqual(pon(), 'グー')
      
   @patch('builtins.input')
   def test_input_2(self, mock_input):
      mock_input.return_value = '2'
      self.assertEqual(pon(), 'チョキ')
      
   @patch('builtins.input')
   def test_input_3(self, mock_input):
      mock_input.return_value = '3'
      self.assertEqual(pon(), 'パー')
      
   @patch('builtins.input')
   def test_input_4_0(self, mock_input):
      with self.assertRaises(StopIteration):
         mock_input.side_effect = ['0','4']
         self.assertFalse(pon())
