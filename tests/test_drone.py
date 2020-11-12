import unittest

from drone import gg


class TestDrone(unittest.TestCase):

  def test_drone(self):
    self.assertEqual(gg(), 1)


