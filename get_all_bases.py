

import itertools
#  product -> מכפלה קרטזית
#  combinations -> קבוצות וקטורים מועמודות להיות בסיס

N = 2


def GetAllVectors(size):
    vectors = list(itertools.product([0, 1], repeat=size))
    vectors.remove(tuple([0]*size))
    return vectors


def GetAllVectorGroups(size):
    vectors = GetAllVectors(size)
    groups_of_vectors = list(itertools.combinations(vectors, size))
    return groups_of_vectors


def GetBasesFromPossibleOptions(group_of_groups):
    pass


def GroupsToStrings(group_of_groups):
    lst = []
    for group in group_of_groups:
        s = ""
        for vector in group:
            s += "".join(list(map(str, vector)))
        lst.append(s)

    return lst


all_groups = GetAllVectorGroups(N)
# bases = GetBasesFromPossibleOptions(all_groups)
groups_as_strings = GroupsToStrings(all_groups)
