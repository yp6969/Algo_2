from functools import reduce

import pytest
import numpy as np

from binmatrix import BinMatrix, FormatError, DataError, RankError


# if __name__ == "__main__":
#
# 	m = [[1,1,0],[0,0,1],[1,0,1]]
# 	try:
# 		matrix = BinMatrix(m)
# 		print "matrix = %s" % str(matrix.m)
# 		print "rank = %d" % matrix.rank()
# 		print "det = %d" % matrix.det()
# 		print "inv = %s" % str(matrix.inv())
# 	except FormatError as e1:
# 		e1.printError()
# 	except DataError as e2:
# 		e2.printError()
# 	except RankError as e3:
# 		e3.printError()


@pytest.fixture()
def base_matrix():
    return BinMatrix(np.array([[1, 1, 0, 0],
                               [0, 0, 1, 1],
                               [1, 0, 1, 1],
                               [0, 0, 0, 1]]))


@pytest.fixture()
def natural_base():
    return BinMatrix(np.array([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]]))


@pytest.fixture()
def not_base():
    return BinMatrix(np.array([[1, 0, 0, 1],
                               [0, 1, 0, 0],
                               [1, 0, 1, 1],
                               [0, 1, 1, 0]]))


def test_is_base(natural_base, not_base):
    assert natural_base.is_base() is True
    assert natural_base.is_base2() is True
    assert not_base.is_base() is False
    assert not_base.is_base2() is False


def test_rank(natural_base):
    print()
    # print(natural_base)
    assert natural_base.rank() == 4

