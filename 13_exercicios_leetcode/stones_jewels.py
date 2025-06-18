# https://leetcode.com/problems/jewels-and-stones/description/


def stones_jewels(stones, jewels):
    jewels_conjunto = set(jewels)
    contador = 0
    for stone in stones:
        if stone in jewels_conjunto:
            contador += 1
    return contador

def test():
    assert stones_jewels(jewels="aA", stones="aAAbbbb") == 3
    assert stones_jewels(jewels="z", stones="ZZ") == 0
