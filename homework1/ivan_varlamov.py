class Interpolator:
    """Linear interpolator.

    """

    @staticmethod
    def interpolate(x_list: list, y_list: list, z: float):
        """Linear interpolate.

        Parameters
        __________
        x_list : list
            x values.
        y_list: list
            y values.
        z: float
            Interpolate in that point z.

        Returns
        _______
        float
            Interpolate value.

        Raises
        ______
        ValueError
            x_list must be sorted ASC.
        """
        if x_list != sorted(x_list):
            raise ValueError('x_list must be sorted ASC')
        for index, element in enumerate(x_list):
            if z <= element:
                delta = (z - x_list[index - 1]) / (x_list[index] - x_list[index - 1])
                answer = y_list[index - 1] + (y_list[index] - y_list[index - 1]) * delta
                break
        return answer


class TestInterpolator:

    def setup_method(self):
        self.f = Interpolator()

    def test_correct_work(self):
        assert self.f.interpolate(x_list=[0, 1, 2, 3, 5], y_list=[0, 1, 4, 9, 25], z=2.5) == 6.5

    def test_correct_work_on_bound(self):
        assert self.f.interpolate(x_list=[0, 1, 2, 3, 5], y_list=[0, 1, 4, 9, 25], z=3) == 9

    def test_raise(self):
        try:
            self.f.interpolate(x_list=[1, 50, 2, 3, 5], y_list=[0, 1, 4, 9, 25], z=2.5)
        except ValueError:
            assert True
