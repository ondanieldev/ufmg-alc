def getNumberAlgarisms(value, algarisms):
    algarisms.append(value % 10)
    if value // 10 == 0:
        return algarisms
    return getNumberAlgarisms(value // 10, algarisms)


def algarismo_mais_comum(numbers):
    algarisms = []
    for number in numbers:
        algarisms.extend(getNumberAlgarisms(number, []))
    algarismsWithCount = []
    for algarism in algarisms:
        for algarismWithCount in algarismsWithCount:
            if algarismWithCount[0] == algarism:
                algarismWithCount[1] += 1
                break
        else:
            algarismsWithCount.append([algarism, 1])
    maxAlgarism = algarismsWithCount[0][0]
    maxCount = algarismsWithCount[0][1]
    for algarismWithCount in algarismsWithCount:
        if algarismWithCount[1] > maxCount:
            maxAlgarism = algarismWithCount[0]
            maxCount = algarismWithCount[1]
    return (maxAlgarism, maxCount)
