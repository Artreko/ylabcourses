from itertools import combinations


def bananas(s):
    result = set()
    for combination in combinations(range(len(s)), len(s) - 6):
        temp = s[::-1][::-1]
        for i in combination:
            temp = f'{temp[:i]}-{temp[i+1:]}'
        if temp.replace('-', '') == 'banana':
            result.add(temp)
    return result


def main():
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


if __name__ == '__main__':
    main()
