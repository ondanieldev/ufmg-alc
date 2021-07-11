def nota_media_aluno(dictionary, subjects, name):
    student = dictionary.get(name)
    sumValues = 0
    count = 0
    for subject in student.items():
        if subject[0] in subjects:
            sumValues += subject[1]
            count += 1
    return sumValues/count
