class term:
    def __init__(self,coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent


class polynomial:
    def __init__(self, n):
        self.n = n
        self.terms = []


polynomial1 = polynomial(3)
polynomial1.terms.append(term(2, 3))  # 2x^3
polynomial1.terms.append(term(3, 2))  # 3x^2
polynomial1.terms.append(term(4, 1))  # 4x^1
polynomial1.terms.append(term(5, 0))  # 5x^0
polynomial2 = polynomial(3)
polynomial2.terms.append(term(1, 3))  # 1x^3
polynomial2.terms.append(term(2, 2))  # 2x^2
polynomial2.terms.append(term(3, 1))  # 3x^1
polynomial2.terms.append(term(4, 0))  # 4x^0

print("Polynomial 1:")
for t in polynomial1.terms:
    print(f"{t.coefficient}x^{t.exponent}", end=" + ")