def pascal_triangle(number: int):
    """
    Pascal's Triangle is a kind of number pattern. Pascal's Triangle is the triangular arrangement of numbers that
    gives the coefficients in the expansion of any binomial expression. This function follows the concept of a
    Binomial Coefficient. The idea is to calculate C(line, i) using C(line, i-1) in all lines. ->
    C(line, i) = C(line, i-1) * (line - i + 1) / i.
    """
    output = []
    if number > 0:
        for i in range(1, number + 1):
            c = 1
            b = []
            for j in range(1, i + 1):
                b.append(c)
                c = c * (i - j) // j
            output.append(b)
    return output
