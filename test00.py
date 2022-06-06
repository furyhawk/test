def findIntersection():
    strArr = ["1, 3, 4, 7, 13, 5", "1, 2, 4, 13, 15, 5"]

    setA = set(strArr[0].split(', '))
    setB = set(strArr[1].split(', '))

    result = sorted(list(setA.intersection(setB)), key=lambda str: int(str))

    return ', '.join(result) if len(result) > 0 else False

print(findIntersection())