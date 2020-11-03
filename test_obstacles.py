import unittest
import io
from io import StringIO
from unittest.mock import patch
import sys
from test_base import captured_io
from test_base import run_unittests
import world.obstacles as obstacles
import robot

class TestRobot(unittest.TestCase):

    def test_is_position_blocked(self):
        obstacles.random.randint = lambda a, b :40
        obstacles.get_obstacles()

        self.assertEqual(obstacles.is_position_blocked(40,40), True)
        self.assertEqual(obstacles.is_position_blocked(39,39), False)

    def test_is_position_blocked_range(self):
        obstacles.random.randint = lambda a, b : 40
        obstacles.get_obstacles()


        self.assertEqual(obstacles.is_position_blocked(43,43), True)
        self.assertEqual(obstacles.is_position_blocked(41,42), True)
        self.assertEqual(obstacles.is_position_blocked(50,50), False)
        self.assertEqual(obstacles.is_position_blocked(56,56), False)

    def test_is_path_blocked(self):
        obstacles.random.randint = lambda a, b :40
        obstacles.get_obstacles()

        self.assertEqual(obstacles.is_path_blocked(40, 20, 40, 70), True)


if __name__ == "__main__":
    unittest.main()





