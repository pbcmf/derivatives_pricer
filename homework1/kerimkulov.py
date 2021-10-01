import numpy as np


class LinInter(object):

    def __init__(self, x, y):
      self.x = x
      self.y = y

      if len(self.x) != len(self.y):
            raise ValueError("the x array and the y array must have exactly the same dimension.")


    def evalf(self, z):
      l = len(self.x)
      left_position = np.argmin(self.x)
      right_position = np.argmax(self.x)
      left = self.x[left_position]
      right = self.x[right_position]
      left_value = self.y[left_position]
      right_value = self.y[right_position]

      if (z < left or z > right):
        raise ValueError("z should be between min(x) and max(x)")

      for i in range(l):
        if (self.x[i]<=z and self.x[i]>left):
          left = self.x[i]
          left_value = self.y[i]
        if (self.x[i]>=z and self.x[i]<right):
          right = self.x[i]
          right_value = self.y[i]

      if right == left:
        k = right_value
      else:
        k = left_value + (right_value - left_value) * (z - left) / (right - left)
      
      return k

import unittest

class TestLinInter(unittest.TestCase):

    def test_diffDim(self):
        x = [0, 1, 2, 3]
        y = [0, 2, 4]
        with self.assertRaises(ValueError):
            LinInter(x,y)

    def test_range_z(self):
        x = [0, 1, 2, 3]
        y = [0, 2, 4, 6]
        with self.assertRaises(ValueError):
            lin = LinInter(x,y)
            lin.evalf(4)

    def test_equal(self):
        x = [0, 1, 2, 3]
        y = [0, 2, 4, 6]
        lin = LinInter(x,y)
        self.assertEqual(lin.evalf(2.5), 5)
        self.assertEqual(lin.evalf(0), 0)

    def test_not_equal(self):
        x = [0, 1, 2, 3]
        y = [0, 2, 4, 6]
        lin = LinInter(x,y)
        self.assertNotEqual(lin.evalf(2.5), 4)
        

if __name__ == '__main__':
  unittest.main()