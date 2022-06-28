from functools import reduce


def count_find_num(primes_l, limit):
    if (first := reduce(lambda x, y: x * y, primes_l)) > limit:
        return []
    composites = set()
    composites.add(first)

    def all_composites(_composites):
        temp = set()
        for prime in primes_l:
            for composite in _composites:
                if (new_composite := prime * composite) <= limit:
                    temp.add(new_composite)
        if (new_composites := _composites.union(temp)) == _composites:
            return _composites
        else:
            return all_composites(new_composites)

    composites = all_composites(composites)
    return [len(composites), max(composites)]


def main():
    primes_l = [2, 3]
    limit = 200
    assert count_find_num(primes_l, limit) == [13, 192]

    primes_l = [2, 5]
    limit = 200
    assert count_find_num(primes_l, limit) == [8, 200]

    primes_l = [2, 3, 5]
    limit = 500
    assert count_find_num(primes_l, limit) == [12, 480]

    primes_l = [2, 3, 5]
    limit = 1000
    assert count_find_num(primes_l, limit) == [19, 960]

    primes_l = [2, 3, 47]
    limit = 200
    assert count_find_num(primes_l, limit) == []


if __name__ == '__main__':
    main()
