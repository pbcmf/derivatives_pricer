import numpy as np


class Liner:
    def __init__(self, X, target):
        tmp = np.array([X, target])
        self.table = tmp[:, tmp[0, :].argsort()]

    def func(self, z):
        x = self.table[0, :]
        y = self.table[1, :]
        right = np.searchsorted(x, z)
        answer = (y[right] - y[right - 1]) / (x[right] - x[right - 1]) * (z - x[right - 1])
        answer += y[right - 1]
        return answer


def test1():
    x = np.arange(-10, 10).astype('float')
    x[4] = -4.5
    y = x ** 2
    print(Liner(x, y).func(-7.7))


if __name__ == '__main__':
    test1()
