import unittest
import io
from io import StringIO
from unittest.mock import patch
import sys
from test_base import captured_io
from test_base import run_unittests
import robot


class Testrobot(unittest.TestCase):

    def test_get_command(self):
        self.assertEqual("OFF".lower(),"off")
        self.assertEqual("HELP".lower(),"help")
        self.assertEqual("FORWARD".lower(),"forward")
        self.assertEqual("BACK".lower(),"back")
        self.assertEqual("RIGHT".lower(),"right")
        self.assertEqual("LEFT".lower(),"left")
        self.assertEqual("SPRINT".lower(),"sprint")
        self.assertEqual("REPLAY".lower(),"replay")
        self.assertEqual("REPLAY SILENT".lower(),"replay silent")
        self.assertEqual("REPLAY REVERSED".lower(),"replay reversed")
        self.assertEqual("REPLAY REVERSED SILENT".lower(),"replay reversed silent")

    def test_get_robot_name(self):
        with captured_io(StringIO("HAL\n")):
            self.assertEqual(robot.get_robot_name(),"HAL")


    def test_split_command_input(self):
        with captured_io(StringIO("")):
            self.assertEqual(robot.split_command_input("forward 10"),("forward", "10"))
            self.assertEqual(robot.split_command_input("back 5"),("back", "5"))
            self.assertEqual(robot.split_command_input("right"),("right", ""))
            self.assertEqual(robot.split_command_input("left"),("left", ""))
            self.assertEqual(robot.split_command_input("sprint"),("sprint", ""))
            self.assertEqual(robot.split_command_input("replay"),("replay", ""))
            self.assertEqual(robot.split_command_input("replay silent"),("replay", "silent"))
            self.assertEqual(robot.split_command_input("replay reversed"),("replay", "reversed"))
            self.assertEqual(robot.split_command_input("replay reversed silent"),("replay", "reversed silent"))


    def test_valid_command(self):
        with captured_io(StringIO("")):
            self.assertEqual(robot.valid_command("off"), True)
            self.assertEqual(robot.valid_command("help"), True)
            self.assertEqual(robot.valid_command("forward 10"), True)
            self.assertEqual(robot.valid_command("back 5"), True)
            self.assertEqual(robot.valid_command("right"), True)
            self.assertEqual(robot.valid_command("left"), True)
            self.assertEqual(robot.valid_command("sprint"), True)
            self.assertEqual(robot.valid_command("replay"), True)
            self.assertEqual(robot.valid_command("replay silent"), True)
            self.assertEqual(robot.valid_command("replay reversed"), True)
            self.assertEqual(robot.valid_command("replay reversed silent"), True)
            self.assertEqual(robot.valid_command("hello"), False)

    def test_do_forward(self):
        with captured_io(StringIO("forward 5\n")):
            self.assertEqual(robot.do_forward("HAL", 5), (True, " > HAL moved forward by 5 steps."))

    def test_do_back(self):
        with captured_io(StringIO("back 7\n")):
            self.assertEqual(robot.do_back("HAL", 7), (True," > HAL moved back by 7 steps."))

    def test_do_right_turn(self):
        with captured_io(StringIO("right\n")):
            self.assertEqual(robot.do_right_turn("HAL"), (True, " > HAL turned right."))
        
    def test_do_left_turn(self):
        with captured_io(StringIO("left\n")):
            self.assertEqual(robot.do_left_turn("HAL"), (True," > HAL turned left."))

if __name__ == "__main__":
    unittest.main()