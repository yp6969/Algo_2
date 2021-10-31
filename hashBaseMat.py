from BinaryLinearSpace import *

"""
Written By:
Mor Nagli, Tom Eliya, Hen Ben LuLu, Niv Nagli
"""


class hashBaseMat:
    def __init__(self, groupOfBases):
        self.__bases = groupOfBases
        self.__hashTable = self.addAllBases()

    @staticmethod
    def baseToInt(tupleOfTuples):
        res = ""
        for innerTuple in tupleOfTuples:
            res += "".join(str(ele) for ele in innerTuple)
        return int(res, 2)

    def addAllBases(self):
        res = {}
        for base in self.__bases:
            res[self.baseToInt(base)] = base
        return res

    def getHashTable(self):
        return self.__hashTable


if __name__ == '__main__':
    x = BinaryLinearSpace().get_group_of_bases(BinaryLinearSpace().get_all_groups_of_vectors())  # get all the bases
    print('Example for the hash implementation for the return value from the "BinaryLinearSpace" class')
    print(hashBaseMat(x).getHashTable())
