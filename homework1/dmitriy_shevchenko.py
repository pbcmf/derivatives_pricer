class LinearInterpolator:

    @ staticmethod
    def interpolate(vals, z):

        k = None
        up_bnd = None
        low_bnd = None

        sorted_list = sorted(vals, key=lambda subl: subl[0])
        for i in range(len(sorted_list)):

            if z == sorted_list[i][0]:
                k = sorted_list[i][1]
            if (sorted_list[i][0] < z < sorted_list[i+1][0]) and (i != len(sorted_list) - 1):
                up_bnd, low_bnd = i+1, i

        if up_bnd is not None and low_bnd is not None:

            x1 = sorted_list[low_bnd][0]
            y1 = sorted_list[low_bnd][1]
            x2 = sorted_list[up_bnd][0]
            y2 = sorted_list[up_bnd][1]

            k = y1 + (z - x1) * (y2 - y1) / (x2 - x1)

        return k


def test_interpolation(vals, z):

    interpolator = LinearInterpolator()
    k = interpolator.interpolate(vals, z)
    print(f'For given array {vals} and argument {z} linear interpolation returns value {k:.2f}')


if __name__ == "__main__":

    test_array = [[10, 1000], [-2345, 1000], [1, 1.5], [-100, -200], [4, 6]]        # y = 1.5x
    test_interpolation(test_array, 2)
