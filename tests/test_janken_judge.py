import unittest
from unittest.mock import patch
from source.janken_judge import judge

class TestjankenJudge(unittest.TestCase):
    def testjadge(self):
        patterns = [
            (("チョキ","グー"),'player_win'),
            (("パー","チョキ"),'player_win'),
            (("グー","パー"),'player_win'),
            
            (("グー","チョキ"),'computer_win'),
            (("チョキ","パー"),'computer_win'),
            (("パー","グー"),'computer_win'),
        ]
        
        for (computer,player), expected in patterns: 
            with self.subTest(f'computer: {computer}, player: {player}'): 
                self.assertEqual(judge( computer,player), expected)