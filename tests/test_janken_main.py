import unittest
from unittest.mock import patch
import source.janken_judge
import source.janken_main
import source.computer
import source.player



class Testmain(unittest.TestCase):
    @patch('builtins.input')
    def test_input_1(self,mock_input):
     self.assertEqual(source.janken_main.result(2,1), 'player_win')
     
    @patch('builtins.input')
    def test_input_2(self,mock_input):
     self.assertEqual(source.janken_main.result(3,0), 'player_win')
     
    @patch('builtins.input')
    def test_input_3(self,mock_input):
     self.assertEqual(source.janken_main.result(0,3), 'computer_win')