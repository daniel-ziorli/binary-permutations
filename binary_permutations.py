import itertools
import sys


def bin_permu(n):
    return ["".join(seq) for seq in itertools.product("01", repeat=n)]


print (bin_permu(int(sys.argv[1])))
