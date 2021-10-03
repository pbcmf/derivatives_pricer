#code v.1

class LinearInterpolation(object):
    """Create a linear interpolation method"""

    def interpolate(x_val, y_val, z):
        # z must be in a range from min(x) to max(x)
        if (z >= min(x_val) and z <= max(x_val)):
            pass
        else:
            raise ValueError("z is not in a range from min(x) to max(x)")

        # find position of z in x_val
        for index, element in enumerate(x_val):
            if z <= element:
                k = (y_val[index - 1] + (z - x_val[index - 1]) / (x_val[index] - x_val[index-1]) * (y_val[index] - y_val[index - 1]))
        return k


import unittest
import numpy as np

class TestInterpolation(unittest.TestCase):
    """Testing of z range and correct output values of LinearInterpolation class"""

    def test_range(self):
        """z range"""
        x_val = [1,2,3,4,5]
        y_val = [15,25,35,45,55]
        z = 100
        with self.assertRaises(ValueError):
            k = LinearInterpolation.interpolate(x_val, y_val, z)

    def test_values(self):
        """Output Values"""
        x_val = [1,2,3,4,5]
        y_val = [15,25,35,45,55]
        z = 4.44
        self.assertEqual(LinearInterpolation.interpolate(x_val, y_val, z), np.interp(z, x_val, y_val))
if __name__ == '__main__':
    unittest.main()
