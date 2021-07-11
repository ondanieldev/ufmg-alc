from bhaskara import bhaskara
from circleRadius import raio_circ
from biggestGrade import maior_nota
from averageGrade import nota_media_aluno
from mostCommonName import nome_mais_comum
from mostCommonAlgarism import algarismo_mais_comum

print(bhaskara(1, 0, -9))
print(raio_circ(78.5))
print(maior_nota({"matematica": 85, "geografia": 75, "portugues": 60}))
print(nota_media_aluno({
    "Joao": {
        "matematica": 85,
        "geografia": 75,
        "portugues": 60
    },
    "Gustavo": {
        "matematica": 71,
        "geografia": 88,
        "portugues": 95
    },
    "Ana": {
        "matematica": 98,
        "geografia": 70,
        "portugues": 55
    }
},  ['matematica', 'geografia'], 'Joao'))
print(nome_mais_comum(['Joao', 'Gustavo', 'Ana', 'Joao']))
print(algarismo_mais_comum([0, 12, 22, 0]))
