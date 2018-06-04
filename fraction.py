# Task 9
# Insert after three maximum members of fractional sequence terms the values of their half-sum
import copy
import fractions


def find_three_max(sequence):
    indexes_of_max_elements = []
    values_of_max_elements = []

    for i in range(0, 3):
        values_of_max_elements.append(max(sequence))
        indexes_of_max_elements.append(sequence.index(values_of_max_elements[i]))
        sequence.remove(values_of_max_elements[i])

    for i in range(0, 3):
        sequence.insert(indexes_of_max_elements[i], values_of_max_elements[i])

    half_sum = sum(values_of_max_elements) / 2
    for i in reversed(sorted(indexes_of_max_elements)):
        sequence.insert(i + 1, half_sum)
    return sequence


sequence_of_fractions = [fractions.Fraction(4, 5), fractions.Fraction(1, 3),
                         fractions.Fraction(4, 3), fractions.Fraction(10, 7)]
print(find_three_max(sequence_of_fractions))
