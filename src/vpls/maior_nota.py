def maior_nota(subjects):
    maxKey = ''
    maxValue = -100
    for subject in subjects.items():
        if subject[1] > maxValue:
            maxKey = subject[0]
            maxValue = subject[1]
    return (maxKey, maxValue)
