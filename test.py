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
def binary_matrix():
    return np.array([[1, 1, 0, 0],
                     [0, 0, 1, 1],
                     [1, 0, 1, 1],
                     [0, 0, 0, 1]])


base = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

not_base = np.array([[1, 0, 0, 1],
                     [0, 1, 0, 0],
                     [1, 0, 1, 1],
                     [0, 1, 1, 0]])


def test_is_base():
    b_matrix = BinMatrix(base)
    b_matrix2 = BinMatrix(not_base)
    assert b_matrix.is_base() is True
    assert b_matrix.is_base2() is True
    assert b_matrix2.is_base() is False
    assert b_matrix2.is_base2() is False
