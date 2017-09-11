# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.

import hashlib
from math import ceil, log
from qrl.core import logger


def numlist(array):
    for a, b in enumerate(array):
        logger.info((a, b))
    return


def sha256(message):
    return hashlib.sha256(message).hexdigest()


def closest_number(one, many):
    """
    return closest number in a list..
    :param one:
    :param many:
    :return:
    """
    return min(many, key=lambda x: abs(x - one))


def merkle_tx_hash(hashes):
    """
    merkle tree root hash of tx from pool for next POS block
    :param hashes:
    :return:
    """
    if len(hashes) == 64:  # if len = 64 then it is a single hash string rather than a list..
        return hashes
    j = int(ceil(log(len(hashes), 2)))
    l_array = [hashes]
    for x in range(j):
        next_layer = []
        i = len(l_array[x]) % 2 + len(l_array[x]) / 2
        z = 0
        for _ in range(i):
            if len(l_array[x]) == z + 1:
                next_layer.append(l_array[x][z])
            else:
                next_layer.append(sha256(l_array[x][z] + l_array[x][z + 1]))
            z += 2
        l_array.append(next_layer)

    return ''.join(l_array[-1])