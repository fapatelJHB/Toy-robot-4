import unittest
import io
from io import StringIO
from unittest.mock import patch
import sys
from test_base import captured_io
from test_base import run_unittests
import world.text.world as world

class Testrobot(unittest.TestCase):
    def test_position_allowed_false(self):
        self.assertEqual(world.is_position_allowed(300, 500), False)

    def test_position_allowed_true(self):
        self.assertEqual(world.is_position_allowed(50, 50), True)

    def test_update_position(self):
        self.assertEqual(world.update_position(6), True)
    
    def test_update_position_out(self):
        self.assertEqual(world.update_position(206), False)


if __name__ == "__main__":
    unittest.main()