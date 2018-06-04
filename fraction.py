# Task 9
# Insert after three maximum members of fractional sequence terms the values of their half-sum
import copy
import fractions


def find_three_max(sequence_of_fractions):
    indexes_of_max_elements = []
    values_of_max_elements = []

    for i in range(0, 3):
        values_of_max_elements.append(max(sequence_of_fractions))
        indexes_of_max_elements.append(sequence_of_fractions.index(values_of_max_elements[i]))
        sequence_of_fractions.remove(values_of_max_elements[i])

    for i in range(0, 3):
        sequence_of_fractions.insert(indexes_of_max_elements[i], values_of_max_elements[i])

    half_sum = sum(values_of_max_elements) / 2
    for i in reversed(sorted(indexes_of_max_elements)):
        sequence_of_fractions.insert(i + 1, half_sum)
    return sequence_of_fractions


sequence_of_fractions = [fractions.Fraction(4, 5), fractions.Fraction(1, 3),
                         fractions.Fraction(4, 3), fractions.Fraction(10, 7)]
print(find_three_max(sequence_of_fractions))
