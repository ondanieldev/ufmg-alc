def nome_mais_comum(names):
    namesWithValues = []
    for name in names:
        for nameWithValue in namesWithValues:
            if nameWithValue[0] == name:
                nameWithValue[1] += 1
                break
        else:
            namesWithValues.append([name, 1])

    maxName = namesWithValues[0][0]
    maxValue = namesWithValues[0][1]
    for nameWithValue in namesWithValues:
        if nameWithValue[1] > maxValue:
            maxName = nameWithValue[0]
            maxValue = nameWithValue[1]
    return (maxName, maxValue)
