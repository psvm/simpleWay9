# Task 9
# Insert after three maximum members of fractional sequence terms the values of their half-sum
import copy
import fractions


def find_three_max(sequence_of_fractions):
    copy_sequence_of_fractions = copy.copy(sequence_of_fractions)
    indexes_of_max_elements = []
    values_of_max_elements = []

    for i in range(0, 3):
        values_of_max_elements.append(max(copy_sequence_of_fractions))
        indexes_of_max_elements.append(copy_sequence_of_fractions.index(values_of_max_elements[i]))
        copy_sequence_of_fractions[indexes_of_max_elements[i]] = min(copy_sequence_of_fractions) - \
                                                                 values_of_max_elements[i]

    indexes_of_max_elements = reversed(sorted(indexes_of_max_elements))
    half_sum = sum(values_of_max_elements) / 2
    for i in indexes_of_max_elements:
        sequence_of_fractions.insert(i + 1, half_sum)
    return sequence_of_fractions


sequence_of_fractions = [fractions.Fraction(4, 5), fractions.Fraction(1, 3),
                         fractions.Fraction(4, 3), fractions.Fraction(10, 7)]
print(find_three_max(sequence_of_fractions))
