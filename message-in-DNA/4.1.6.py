def Normalize(Probabilities):
    # your code here
    freq = sum([Probabilities[i] for i in Probabilities.keys()])
    return ({i: Probabilities[i]/freq for i in Probabilities.keys()})

print(Normalize({'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}))