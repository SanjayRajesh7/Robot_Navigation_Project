# Unit Tests
import unittest
from Terrain import Terrain

class TestRobotMovement(unittest.TestCase):
    def setUp(self):
        self.terrain = Terrain()
        self.assertEqual(self.terrain.create_robot(1), "Robot with ID 1 is created successfully!!!.")
        self.assertEqual(self.terrain.create_robot(2), "Robot with ID 2 is created successfully!!!.")
        self.assertEqual(self.terrain.create_robot(1), "Robot with ID 1 already exists.")

    def test_robot_initial_position(self):
        self.assertEqual(self.terrain.get_robot_position(1), "The position of 1 is (0, 0).")
        self.assertEqual(self.terrain.get_robot_position(2), "The position of 2 is (0, 0).")
        self.assertEqual(self.terrain.get_robot_position(3), "Robot with ID 3 does not exist.")

    def test_move_robot(self):
        self.assertEqual(self.terrain.move_robot(1, "3E", False), "Robot with ID 1 is moved successfully!!!.")
        self.assertEqual(self.terrain.move_robot(1, "3N", False), "Robort could not be moved outside the grid")
        self.assertEqual(self.terrain.get_robot_position(1), "The position of 1 is (0, 3).")

    def test_collision_prevention(self):
        self.assertEqual(self.terrain.move_robot(1, "2S", False), "Robot with ID 1 is moved successfully!!!.")
        self.assertEqual(self.terrain.move_robot(2, "2S", False), "Robot with ID 2 is moved successfully!!!.")
        self.assertEqual(self.terrain.get_robot_position(1), "The position of 1 is (2, 0).")
        self.assertEqual(self.terrain.get_robot_position(2), "The position of 2 is (1, 0).")

    def test_multiple_movements(self):
        self.terrain.move_robot(1, "2E", False)
        self.terrain.move_robot(1, "1S", False)
        self.terrain.move_robot(2, "1S", False)
        self.assertEqual(self.terrain.get_robot_position(1), "The position of 1 is (1, 2).")
        self.assertEqual(self.terrain.get_robot_position(2), "The position of 2 is (1, 0).")