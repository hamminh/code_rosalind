def expected_dominant_offspring(couples):
    # Assign the probabilities of dominant phenotype for each genotype pairing
    probabilities = [1, 1, 1, 0.75, 0.5, 0]
    
    # Calculate the expected number of dominant phenotype offspring
    expected_offspring = 0
    for i in range(6):
        expected_offspring += couples[i] * probabilities[i] * 2
    
    return expected_offspring

couples = [19981, 16550, 19679, 18064, 16012, 19089]

# Calculate the expected number of dominant offspring
result = expected_dominant_offspring(couples)
print(result)
